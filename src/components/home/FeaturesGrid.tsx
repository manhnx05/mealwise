import React from 'react';
import { Link } from 'react-router-dom';
import { Search, Calendar, ShoppingCart, Heart, Users, Flame } from 'lucide-react';
import { motion } from 'framer-motion';

const features = [
  {
    icon: Search,
    title: 'Tìm theo nguyên liệu',
    desc: 'Nhập nguyên liệu có sẵn, web gợi ý món ăn phù hợp',
    link: '/search-ingredients',
    color: 'bg-primary/10 text-primary',
  },
  {
    icon: Calendar,
    title: 'Thực đơn cả tuần',
    desc: 'Gợi ý menu 7 ngày, không cần nghĩ hôm nay ăn gì',
    link: '/meal-planner',
    color: 'bg-secondary/10 text-secondary',
  },
  {
    icon: ShoppingCart,
    title: 'Danh sách đi chợ',
    desc: 'Tự động tạo shopping list khi chọn món ăn',
    link: '/meal-planner',
    color: 'bg-primary/10 text-primary',
  },
  {
    icon: Heart,
    title: 'Món ăn sức khỏe',
    desc: 'Món ít dầu mỡ, giảm cân, cho người tập gym',
    link: '/healthy',
    color: 'bg-destructive/10 text-destructive',
  },
  {
    icon: Users,
    title: 'Cộng đồng nấu ăn',
    desc: 'Chia sẻ công thức, đánh giá và bình luận',
    link: '/community',
    color: 'bg-secondary/10 text-secondary',
  },
  {
    icon: Flame,
    title: 'Tính calo chi tiết',
    desc: 'Xem protein, chất béo, chất xơ của từng món',
    link: '/recipes',
    color: 'bg-primary/10 text-primary',
  },
];

export default function FeaturesGrid() {
  return (
    <section className="bg-muted/50 py-16">
      <div className="max-w-7xl mx-auto px-4 sm:px-6">
        <div className="text-center mb-12">
          <h2 className="font-display text-3xl font-bold text-foreground mb-3">
            Tính năng nổi bật
          </h2>
          <p className="text-muted-foreground max-w-md mx-auto">
            Mọi thứ bạn cần để nấu ăn đơn giản, tiết kiệm và khoa học
          </p>
        </div>
        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-5">
          {features.map((f, i) => (
            <motion.div
              key={i}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.08 }}
            >
              <Link to={f.link}>
                <div className="group bg-card rounded-2xl p-6 border border-border/50 hover:shadow-lg hover:shadow-primary/5 transition-all duration-300 h-full">
                  <div className={`w-12 h-12 rounded-xl ${f.color} flex items-center justify-center mb-4 group-hover:scale-110 transition-transform`}>
                    <f.icon className="w-6 h-6" />
                  </div>
                  <h3 className="font-semibold text-foreground mb-2">{f.title}</h3>
                  <p className="text-sm text-muted-foreground">{f.desc}</p>
                </div>
              </Link>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}