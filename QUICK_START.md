# 🚀 Quick Start - MealWise App

## Bước 1: Cài đặt dependencies
```bash
npm install
```

## Bước 2: Cấu hình môi trường
Tạo file `.env.local` với nội dung:
```env
VITE_BASE44_APP_ID=your_app_id
VITE_BASE44_APP_BASE_URL=https://your-app.base44.app
```

## Bước 3: Khởi chạy dev server
```bash
npm run dev
```

## Bước 4: Seed dữ liệu mẫu

### Cách 1: Qua UI (Dễ nhất)
1. Mở trình duyệt: `http://localhost:5173`
2. Click vào menu "🌱 Seed Data" trên navbar
3. Click nút "Bắt đầu Seed"
4. Đợi hoàn tất!

### Cách 2: Qua command line
```bash
npm run seed
```

## Bước 5: Khám phá app
- **Trang chủ**: `/` - Giới thiệu tính năng
- **Công thức**: `/recipes` - Xem 6 món ăn mẫu
- **Tìm theo nguyên liệu**: `/search-ingredients` - Tìm món theo nguyên liệu có sẵn
- **Thực đơn tuần**: `/meal-planner` - Tạo thực đơn với AI
- **Cộng đồng**: `/community` - Xem 3 bài viết mẫu

## 📊 Dữ liệu mẫu
- ✅ 6 công thức nấu ăn (đa dạng category)
- ✅ 3 bài viết cộng đồng (có comments & rating)
- ✅ Đầy đủ thông tin dinh dưỡng, giá cả, bước làm

## 🛠️ Scripts có sẵn
```bash
npm run dev        # Chạy dev server
npm run build      # Build production
npm run preview    # Preview production build
npm run lint       # Check linting
npm run typecheck  # Check TypeScript
npm run seed       # Seed dữ liệu mẫu
```

## ⚠️ Lưu ý
- Hiện tại đang dùng dummy Base44 credentials
- Cần cập nhật `.env.local` với app thật để hoạt động đầy đủ
- Xem file `HUONG_DAN_SEED_DATA.md` để biết chi tiết

## 🎯 Các tính năng chính
1. ✅ Quản lý công thức nấu ăn
2. ✅ Tìm kiếm theo nguyên liệu
3. ✅ Lập kế hoạch thực đơn tuần (AI-powered)
4. ✅ Cộng đồng chia sẻ công thức
5. ✅ Tính toán dinh dưỡng & chi phí
6. ✅ Responsive design (mobile-friendly)

---

**Chúc bạn code vui vẻ! 🎉**
