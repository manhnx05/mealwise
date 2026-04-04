/// <reference types="vite/client" />
// src/api/base44Client.ts

// =========================================================================
// MOCK LOCALSTORAGE BACKEND
// Tệp này giả lập toàn bộ API của Base44 SDK lưu bằng trình duyệt cục bộ.
// Giúp app hoạt động độc lập không cần backend cloud hay cơ sở dữ liệu.
// =========================================================================

import defaultRecipes from '../data/recipes.json';

const DB_PREFIX = 'mealwise_db_';

const generateId = () => Math.random().toString(36).substring(2, 11);

const loadFromDB = (entityName: string) => {
  try {
    const dataStr = localStorage.getItem(DB_PREFIX + entityName);
    const localData = dataStr ? JSON.parse(dataStr) : [];
    
    // Fallback data for Vercel/new users
    if (entityName === 'Recipe') {
      // Kết hợp dữ liệu tĩnh (hàng trăm món) vào với dữ liệu cục bộ
      const localIds = new Set(localData.map((r: any) => r.id));
      const addedDefaults = defaultRecipes.filter((r: any) => !localIds.has(r.id));
      return [...localData, ...addedDefaults];
    }
    return localData;
  } catch (e) {
    if (entityName === 'Recipe') return defaultRecipes;
    return [];
  }
};

const saveToDB = (entityName: string, data: any[]) => {
  try {
    localStorage.setItem(DB_PREFIX + entityName, JSON.stringify(data));
  } catch (e) {
    console.error("Lỗi khi lưu vào LocalStorage (có thể file quá lớn):", e);
  }
};

const createMockEntity = (entityName: string) => {
  return {
    list: async (sortBy: string = '-created_date', limit?: number) => {
      const data = loadFromDB(entityName);
      if (sortBy.startsWith('-')) {
        data.reverse();
      }
      return limit ? data.slice(0, limit) : data;
    },
    filter: async (conditions: any) => {
      const data = loadFromDB(entityName);
      return data.filter((item: any) => {
        for (const key in conditions) {
          if (item[key] !== conditions[key]) return false;
        }
        return true;
      });
    },
    create: async (payload: any) => {
      const data = loadFromDB(entityName);
      const newItem = {
        ...payload,
        id: generateId(),
        created_date: new Date().toISOString(),
      };
      data.push(newItem);
      saveToDB(entityName, data);
      return newItem;
    },
    update: async (id: string, payload: any) => {
      const data = loadFromDB(entityName);
      const index = data.findIndex((item: any) => item.id === id);
      if (index !== -1) {
        data[index] = { ...data[index], ...payload, updated_date: new Date().toISOString() };
        saveToDB(entityName, data);
        return data[index];
      }
      throw new Error(`Item với ID ${id} không tồn tại`);
    },
    delete: async (id: string) => {
      const data = loadFromDB(entityName);
      const filtered = data.filter((item: any) => item.id !== id);
      saveToDB(entityName, filtered);
      return true;
    }
  };
};

export const base44 = {
  auth: {
    me: async () => ({
      id: "admin-local-1",
      email: "nguyetuyetak2005@gmail.com", // Trùng email admin để bypass phân quyền
      full_name: "Admin Nội Bộ",
    }),
    logout: () => {
      console.log("Mocked: Đã đăng xuất");
    },
    redirectToLogin: () => {
      console.log("Mocked: Yêu cầu đăng nhập");
    }
  },
  entities: {
    Recipe: createMockEntity('Recipe'),
    CommunityPost: createMockEntity('CommunityPost'),
    MealPlan: createMockEntity('MealPlan'),
  },
  integrations: {
    Core: {
      UploadFile: async ({ file }: { file: File }) => {
        // Chuyển file ảnh thành chuỗi Data URI (Base64) để lưu ngay xuống LocalStorage
        return new Promise((resolve) => {
          if (!file) resolve({ file_url: '' });
          const reader = new FileReader();
          reader.onloadend = () => {
             resolve({ file_url: reader.result as string });
          };
          reader.onerror = () => {
             // Fallback link mặc định nếu lỗi
             resolve({ file_url: "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=400" });
          };
          reader.readAsDataURL(file);
        });
      },
      InvokeLLM: async (args: any) => {
        const apiKey = import.meta.env.VITE_API_GEMINI_KEY;
        if (!apiKey) {
          throw new Error("Không tìm thấy VITE_API_GEMINI_KEY trong file .env");
        }

        const prompt = args.prompt || "";
        const schema = args.response_json_schema;

        const body: any = {
          contents: [{ parts: [{ text: prompt }] }],
          generationConfig: {}
        };
        
        if (schema) {
          body.generationConfig.responseMimeType = "application/json";
          body.generationConfig.responseSchema = schema;
        }

        const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${apiKey}`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(body)
        });

        if (!response.ok) {
          const errorText = await response.text();
          throw new Error(`Lỗi từ Gemini API: ${errorText}`);
        }

        const data = await response.json();
        const textContent = data.candidates?.[0]?.content?.parts?.[0]?.text;
        
        if (!textContent) {
          throw new Error("Gemini không trả về kết quả hợp lệ");
        }

        if (schema) {
          try {
            return typeof textContent === 'string' ? JSON.parse(textContent) : textContent;
          } catch (e) {
            console.error("Không thể parse JSON từ Gemini", textContent);
            throw new Error("Dữ liệu Gemini trả về không đúng định dạng JSON");
          }
        }

        return textContent;
      }
    }
  }
};
