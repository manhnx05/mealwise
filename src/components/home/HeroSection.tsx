import React from 'react';
import { Link } from 'react-router-dom';
import { Button } from "@/components/ui/button";
import { Clock, Wallet, Sparkles, ArrowRight } from 'lucide-react';
import { motion } from 'framer-motion';

const features = [
  { icon: Clock, label: 'Nấu trong 10-15 phút', color: 'text-primary' },
  { icon: Wallet, label: 'Tiết kiệm chi phí', color: 'text-secondary' },
  { icon: Sparkles, label: 'Công thức đơn giản', color: 'text-primary' },
];

export default function HeroSection() {
  return (
    <section className="relative overflow-hidden">
      <div className="absolute inset-0 bg-gradient-to-br from-primary/5 via-transparent to-secondary/5" />
      <div className="absolute top-20 right-10 w-72 h-72 bg-primary/10 rounded-full blur-3xl" />
      <div className="absolute bottom-10 left-10 w-96 h-96 bg-secondary/10 rounded-full blur-3xl" />

      <div className="relative max-w-7xl mx-auto px-4 sm:px-6 py-16 sm:py-24">
        <div className="grid lg:grid-cols-2 gap-12 items-center">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.7 }}
          >
            <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-primary/10 text-primary text-sm font-medium mb-6">
              <Sparkles className="w-4 h-4" />
              WEB COOKSIMPLE
            </div>
            <h1 className="font-display text-4xl sm:text-5xl lg:text-6xl font-bold text-foreground leading-tight mb-6">
              Giúp bạn nấu ăn{' '}
              <span className="text-primary">nhanh hơn</span>,{' '}
              <span className="text-secondary">rẻ hơn</span> và{' '}
              dễ hơn mỗi ngày
            </h1>
            <p className="text-lg text-muted-foreground mb-8 max-w-lg">
              Khám phá hàng trăm công thức nấu ăn đơn giản, tiết kiệm thời gian với hướng dẫn từng bước bằng hình ảnh và video.
            </p>

            <div className="flex flex-wrap gap-3 mb-10">
              <Link to="/recipes">
                <Button size="lg" className="rounded-full text-base px-8 gap-2">
                  Khám phá công thức <ArrowRight className="w-4 h-4" />
                </Button>
              </Link>
              <Link to="/search-ingredients">
                <Button size="lg" variant="outline" className="rounded-full text-base px-8">
                  Tìm theo nguyên liệu
                </Button>
              </Link>
            </div>

            <div className="flex flex-wrap gap-6">
              {features.map((f, i) => (
                <motion.div
                  key={i}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 0.3 + i * 0.1 }}
                  className="flex items-center gap-2 text-sm text-muted-foreground"
                >
                  <div className="w-8 h-8 rounded-lg bg-muted flex items-center justify-center">
                    <f.icon className={`w-4 h-4 ${f.color}`} />
                  </div>
                  {f.label}
                </motion.div>
              ))}
            </div>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.7, delay: 0.2 }}
            className="relative hidden lg:block"
          >
            <div className="relative rounded-3xl overflow-hidden shadow-2xl aspect-square">
              <img
                src="https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=800&h=800&fit=crop"
                alt="Nấu ăn đơn giản"
                className="w-full h-full object-cover"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-black/30 to-transparent" />
            </div>
            <motion.div
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: 0.6 }}
              className="absolute -bottom-4 -left-4 bg-card rounded-2xl shadow-xl p-4 border border-border"
            >
              <div className="flex items-center gap-3">
                <div className="w-12 h-12 rounded-xl bg-primary/10 flex items-center justify-center">
                  <Clock className="w-6 h-6 text-primary" />
                </div>
                <div>
                  <p className="text-2xl font-bold text-foreground">10-15p</p>
                  <p className="text-xs text-muted-foreground">Thời gian nấu</p>
                </div>
              </div>
            </motion.div>
            <motion.div
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: 0.8 }}
              className="absolute -top-4 -right-4 bg-card rounded-2xl shadow-xl p-4 border border-border"
            >
              <div className="flex items-center gap-3">
                <div className="w-12 h-12 rounded-xl bg-secondary/10 flex items-center justify-center">
                  <Wallet className="w-6 h-6 text-secondary" />
                </div>
                <div>
                  <p className="text-2xl font-bold text-foreground">15K</p>
                  <p className="text-xs text-muted-foreground">Chi phí/món</p>
                </div>
              </div>
            </motion.div>
          </motion.div>
        </div>
      </div>
    </section>
  );
}