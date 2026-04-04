// src/api/base44Client.ts

// =========================================================================
// MOCK LOCALSTORAGE BACKEND
// Tệp này giả lập toàn bộ API của Base44 SDK lưu bằng trình duyệt cục bộ.
// Giúp app hoạt động độc lập không cần backend cloud hay cơ sở dữ liệu.
// =========================================================================

const DB_PREFIX = 'mealwise_db_';

const generateId = () => Math.random().toString(36).substring(2, 11);

const loadFromDB = (entityName: string) => {
  try {
    const data = localStorage.getItem(DB_PREFIX + entityName);
    return data ? JSON.parse(data) : [];
  } catch (e) {
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
        // Giả lập API trả về công thức JSON cho tính năng tạo meal plan tự động
        return {
          meals: [
            { day: "Thứ 2", breakfast: "Phở bò", lunch: "Cơm sườn", dinner: "Canh chua cá lóc" },
            { day: "Thứ 3", breakfast: "Xôi gấc", lunch: "Bún chả", dinner: "Thịt luộc cà pháo" },
            { day: "Thứ 4", breakfast: "Bánh mì pate", lunch: "Cơm gà xối mỡ", dinner: "Salad cá ngừ" },
            { day: "Thứ 5", breakfast: "Miến gà", lunch: "Mì ý xào thịt băm", dinner: "Đậu nhồi thịt" },
            { day: "Thứ 6", breakfast: "Bánh bao", lunch: "Phở cuốn", dinner: "Cá kho tộ" },
            { day: "Thứ 7", breakfast: "Cháo sườn", lunch: "Bánh xèo", dinner: "Gà rán" },
            { day: "Chủ nhật", breakfast: "Bánh cuốn", lunch: "Lẩu thái hải sản", dinner: "Trái cây nhẹ nhàng" }
          ],
          shopping_list: [
            { name: "Thịt bò", amount: "500g" },
            { name: "Thịt lợn", amount: "1.5 kg" },
            { name: "Gà ta", amount: "1 con" },
            { name: "Hải sản các loại", amount: "2 kg" },
            { name: "Rau củ lẩu + Salad", amount: "2 kg" },
            { name: "Gia vị + hành tỏi", amount: "Theo nhu cầu" }
          ],
          total_cost: 1250000
        };
      }
    }
  }
};
