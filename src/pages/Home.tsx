import React from 'react';
import { Link } from 'react-router-dom';
import { Button } from "@/components/ui/button";
import { ArrowRight, Clock, Wallet, Sparkles, Search, Calendar, ShoppingCart, Heart, Users, Flame } from 'lucide-react';
import { motion } from 'framer-motion';
import { useQuery } from '@tanstack/react-query';
import { base44 } from '@/api/base44Client';
import { formatDistanceToNow } from 'date-fns';
import { vi } from 'date-fns/locale';

const features = [
  {
    icon: Search,
    title: 'Tìm theo nguyên liệu',
    desc: 'Nhập nguyên liệu có sẵn, web gợi ý món ăn phù hợp',
    color: 'text-green-600',
    bg: 'bg-green-50'
  },
  {
    icon: Calendar,
    title: 'Thực đơn cả tuần',
    desc: 'Gợi ý menu 7 ngày, không cần nghĩ hôm nay ăn gì',
    color: 'text-orange-500',
    bg: 'bg-orange-50'
  },
  {
    icon: ShoppingCart,
    title: 'Danh sách đi chợ',
    desc: 'Tự động tạo shopping list khi chọn món ăn',
    color: 'text-green-600',
    bg: 'bg-green-50'
  },
  {
    icon: Heart,
    title: 'Món ăn sức khỏe',
    desc: 'Món ít dầu mỡ, giảm cân, cho người tập gym',
    color: 'text-rose-500',
    bg: 'bg-rose-50'
  },
  {
    icon: Users,
    title: 'Cộng đồng nấu ăn',
    desc: 'Chia sẻ công thức, đánh giá và bình luận',
    color: 'text-orange-500',
    bg: 'bg-orange-50'
  },
  {
    icon: Flame,
    title: 'Tính calo chi tiết',
    desc: 'Xem protein, chất béo, chất xơ của từng món',
    color: 'text-green-600',
    bg: 'bg-green-50'
  }
];

export default function Home() {
  const { data: quickRecipes = [] } = useQuery({
    queryKey: ['quick-recipes'],
    queryFn: () => base44.entities.Recipe.list('-created_date', 3),
  });

  return (
    <div className="flex flex-col min-h-screen bg-[#fafaf8]">
      {/* Hero Section */}
      <section className="relative px-4 pt-20 pb-24 sm:px-6 lg:px-8 max-w-7xl mx-auto w-full">
        <div className="absolute inset-0 max-w-7xl mx-auto">
          <div className="absolute top-0 right-0 w-[800px] h-[800px] bg-gradient-to-l from-green-50/50 via-green-50/20 to-transparent rounded-full blur-3xl -z-10 opacity-70 mix-blend-multiply" />
          <div className="absolute top-0 left-0 w-[600px] h-[600px] bg-gradient-to-r from-orange-50/40 to-transparent rounded-full blur-3xl -z-10 opacity-50 mix-blend-multiply" />
        </div>

        <div className="grid lg:grid-cols-2 gap-12 lg:gap-8 items-center relative z-10">
          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}
            className="flex flex-col items-start"
          >
            <div className="inline-flex items-center justify-center gap-2 px-3 py-1.5 rounded-full bg-[#2e8b57]/10 text-[#2e8b57] text-sm font-semibold mb-6">
              <Sparkles className="w-4 h-4" />
              WEB COOKSIMPLE
            </div>

            <h1 className="text-5xl lg:text-7xl font-display font-bold leading-[1.1] text-slate-900 mb-6">
              Giúp bạn nấu ăn <br/>
              <span className="text-[#2e8b57]">nhanh hơn</span>, <span className="text-orange-500">rẻ hơn</span> và<br /> 
              dễ hơn mỗi ngày
            </h1>

            <p className="text-lg text-slate-600 mb-10 max-w-lg leading-relaxed">
              Khám phá hàng trăm công thức nấu ăn đơn giản, tiết kiệm thời gian với hướng dẫn từng bước bằng hình ảnh và video.
            </p>

            <div className="flex flex-wrap items-center gap-4 mb-12">
              <Link to="/recipes">
                <Button size="lg" className="h-14 px-8 text-base rounded-full bg-[#2e8b57] hover:bg-[#2e8b57]/90 text-white gap-2">
                  Khám phá công thức <ArrowRight className="w-5 h-5" />
                </Button>
              </Link>
              <Link to="/search-ingredients">
                <Button size="lg" variant="outline" className="h-14 px-8 text-base rounded-full border-slate-200 hover:bg-slate-50 text-slate-700">
                  Tìm theo nguyên liệu
                </Button>
              </Link>
            </div>

            <div className="flex items-center gap-8 text-sm font-medium text-slate-500">
              <div className="flex items-center gap-2">
                <Clock className="w-4 h-4 text-[#2e8b57]" />
                Nấu trong 10-15 phút
              </div>
              <div className="flex items-center gap-2">
                <Wallet className="w-4 h-4 text-orange-500" />
                Tiết kiệm chi phí
              </div>
              <div className="flex items-center gap-2">
                <Sparkles className="w-4 h-4 text-[#2e8b57]" />
                Công thức đơn giản
              </div>
            </div>
          </motion.div>

          <motion.div 
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.6, delay: 0.2 }}
            className="relative lg:ml-auto"
          >
            <div className="relative w-full max-w-[500px] aspect-[4/5] rounded-[2.5rem] overflow-hidden shadow-2xl">
              <img 
                src="https://images.unsplash.com/photo-1556910103-1c02745aae4d?q=80&w=2070&auto=format&fit=crop" 
                alt="Couple cooking together" 
                className="w-full h-full object-cover"
              />
            </div>

            {/* Floating Card 1 */}
            <motion.div 
              initial={{ y: 20, opacity: 0 }}
              animate={{ y: 0, opacity: 1 }}
              transition={{ delay: 0.8, type: "spring" }}
              className="absolute top-12 -right-12 bg-white p-4 rounded-2xl shadow-xl flex items-center gap-4"
            >
              <div className="w-12 h-12 bg-orange-50 rounded-xl flex items-center justify-center">
                <Wallet className="w-6 h-6 text-orange-500" />
              </div>
              <div>
                <p className="text-xl font-bold text-slate-900">15K</p>
                <p className="text-xs text-slate-500 font-medium">Chi phí/món</p>
              </div>
            </motion.div>

            {/* Floating Card 2 */}
            <motion.div 
              initial={{ y: -20, opacity: 0 }}
              animate={{ y: 0, opacity: 1 }}
              transition={{ delay: 1, type: "spring" }}
              className="absolute bottom-12 -left-12 bg-white p-4 rounded-2xl shadow-xl flex items-center gap-4"
            >
              <div className="w-12 h-12 bg-green-50 rounded-xl flex items-center justify-center">
                <Clock className="w-6 h-6 text-[#2e8b57]" />
              </div>
              <div>
                <p className="text-xl font-bold text-slate-900">10-15p</p>
                <p className="text-xs text-slate-500 font-medium">Thời gian nấu</p>
              </div>
            </motion.div>
          </motion.div>
        </div>
      </section>

      {/* Recipes Section */}
      <section className="bg-white py-24">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex flex-col sm:flex-row sm:items-end justify-between mb-12">
            <div>
              <h2 className="text-3xl font-display font-bold text-slate-900 mb-2">Công thức nấu nhanh</h2>
              <p className="text-slate-500">Món ăn dễ nấu trong 10-15 phút, hoàn hảo cho người bận rộn</p>
            </div>
            <Link to="/recipes" className="text-sm font-semibold text-slate-900 mt-4 sm:mt-0 flex items-center gap-1 hover:text-[#2e8b57] transition-colors">
              Xem tất cả <ArrowRight className="w-4 h-4" />
            </Link>
          </div>

          <div className="grid md:grid-cols-3 gap-8">
            {quickRecipes.map((recipe: any) => (
              <Link key={recipe.id} to={`/recipes/${recipe.id}`} className="group block">
                <div className="relative aspect-[4/3] rounded-3xl overflow-hidden mb-5">
                  <img src={recipe.image_url} alt={recipe.title} className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
                  <div className="absolute top-4 left-4 bg-white/90 backdrop-blur-md px-3 py-1.5 rounded-full text-xs font-semibold text-slate-900">
                    {recipe.category || 'Món ngon'}
                  </div>
                </div>
                <h3 className="font-display text-xl font-bold text-slate-900 mb-2 group-hover:text-[#2e8b57] transition-colors">{recipe.title}</h3>
                <p className="text-slate-500 text-sm line-clamp-2 mb-4">{recipe.description}</p>
                <div className="flex items-center gap-4 text-xs font-medium text-slate-600">
                  <div className="flex items-center gap-1">
                    <Clock className="w-4 h-4 text-slate-400" /> {recipe.cook_time} phút
                  </div>
                  <div className="flex items-center gap-1">
                    <Wallet className="w-4 h-4 text-slate-400" /> {new Intl.NumberFormat('vi-VN').format(recipe.cost || 0)}đ 
                  </div>
                </div>
              </Link>
            ))}
            {quickRecipes.length === 0 && (
              <div className="col-span-3 text-center py-12 text-slate-500">
                Chưa có công thức nào. Hãy thử chạy Seed Data.
              </div>
            )}
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-24 bg-[#fafaf8]">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 className="text-3xl font-display font-bold text-slate-900 mb-3">Tính năng nổi bật</h2>
          <p className="text-slate-500 mb-16">Mọi thứ bạn cần để nấu ăn đơn giản, tiết kiệm và khoa học</p>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {features.map((feature, idx) => {
              const Icon = feature.icon;
              return (
                <div key={idx} className="bg-white p-8 rounded-[2rem] text-left hover:shadow-xl transition-shadow border border-slate-100">
                  <div className={`w-14 h-14 rounded-2xl ${feature.bg} flex items-center justify-center mb-6`}>
                    <Icon className={`w-7 h-7 ${feature.color}`} />
                  </div>
                  <h3 className="text-xl font-bold text-slate-900 mb-2">{feature.title}</h3>
                  <p className="text-slate-500">{feature.desc}</p>
                </div>
              );
            })}
          </div>
        </div>
      </section>
    </div>
  );
}
