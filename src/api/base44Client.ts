/// <reference types="vite/client" />
// src/api/base44Client.ts

// =========================================================================
// FLASK BACKEND ADAPTER
// Đã thay thế giả lập LocalStorage bằng API RESTful chuẩn để kết nối với Flask Backend Python
// =========================================================================

const API_BASE = import.meta.env.VITE_API_URL || '/api';

const fetchAPI = async (endpoint: string, options: RequestInit = {}) => {
  const url = `${API_BASE}${endpoint}`;
  const response = await fetch(url, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      ...(options.headers || {}),
    },
  });

  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(`API Error ${response.status}: ${errorText}`);
  }

  return response.json();
};

const createRestEntity = (entityPath: string) => {
  return {
    list: async (sortBy: string = '-created_date', limit?: number) => {
      // API hiện tại tự động sắp xếp theo created_at giảm dần.
      const data = await fetchAPI(entityPath);
      return limit ? data.slice(0, limit) : data;
    },
    filter: async (conditions: any = {}) => {
      const params = new URLSearchParams(conditions).toString();
      return fetchAPI(`${entityPath}?${params}`);
    },
    create: async (payload: any) => {
      return fetchAPI(entityPath, {
        method: 'POST',
        body: JSON.stringify(payload),
      });
    },
    update: async (id: string | number, payload: any) => {
      return fetchAPI(`${entityPath}/${id}`, {
        method: 'PUT',
        body: JSON.stringify(payload),
      });
    },
    delete: async (id: string | number) => {
      return fetchAPI(`${entityPath}/${id}`, {
        method: 'DELETE',
      });
    }
  };
};

export const base44 = {
  auth: {
    me: async () => ({
      id: "admin-local-1",
      email: "nguyetuyetak2005@gmail.com",
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
    Recipe: createRestEntity('/recipes'),
    CommunityPost: createRestEntity('/community'),
    MealPlan: createRestEntity('/meal-plans'),
  },
  integrations: {
    Core: {
      UploadFile: async ({ file }: { file: File }) => {
        const formData = new FormData();
        formData.append('file', file);

        const response = await fetch(`${API_BASE}/upload`, {
          method: 'POST',
          body: formData, // Không set Content-Type vì trình duyệt sẽ tự gán boundary cho multipart
        });

        if (!response.ok) {
          throw new Error('Upload failed');
        }

        return response.json(); // Trả về { file_url: "..." }
      },
      InvokeLLM: async (args: any) => {
        const body = {
          prompt: args.prompt || "",
          response_json_schema: args.response_json_schema
        };

        const result = await fetchAPI('/generate-meal-plan', {
          method: 'POST',
          body: JSON.stringify(body)
        });

        return result; // Hàm backend Flask giờ đã trả về trực tiếp dict/list đã qua json.loads()
      }
    }
  }
};
