import React from 'react';
import { Link } from 'react-router-dom';
import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Clock, Flame, Wallet } from 'lucide-react';
import { motion } from 'framer-motion';

const categoryLabels = {
  quick_meal: 'Nhanh gọn',
  low_fat: 'Ít dầu mỡ',
  weight_loss: 'Giảm cân',
  gym: 'Gym',
  healthy: 'Lành mạnh',
  budget: 'Tiết kiệm',
  vegetarian: 'Chay',
};

export default function RecipeCard({ recipe, index = 0 }) {
  const formatCost = (cost) => {
    if (!cost) return '';
    return new Intl.NumberFormat('vi-VN').format(cost) + 'đ';
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: index * 0.05 }}
    >
      <Link to={`/recipes/${recipe.id}`}>
        <Card className="group overflow-hidden border-border/50 hover:shadow-xl hover:shadow-primary/5 transition-all duration-500 cursor-pointer">
          <div className="relative aspect-[4/3] overflow-hidden">
            <img
              src={recipe.image_url || 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=600&h=450&fit=crop'}
              alt={recipe.title}
              className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700"
            />
            <div className="absolute inset-0 bg-gradient-to-t from-black/50 via-transparent to-transparent" />
            {recipe.category && (
              <Badge className="absolute top-3 left-3 bg-card/90 text-foreground backdrop-blur-sm border-0 text-xs">
                {categoryLabels[recipe.category] || recipe.category}
              </Badge>
            )}
            {recipe.cook_time && (
              <div className="absolute bottom-3 left-3 flex items-center gap-1.5 text-white text-sm font-medium">
                <Clock className="w-3.5 h-3.5" />
                {recipe.cook_time} phút
              </div>
            )}
          </div>
          <div className="p-4">
            <h3 className="font-semibold text-foreground group-hover:text-primary transition-colors mb-2 line-clamp-1">
              {recipe.title}
            </h3>
            {recipe.description && (
              <p className="text-sm text-muted-foreground line-clamp-2 mb-3">{recipe.description}</p>
            )}
            <div className="flex items-center gap-4 text-xs text-muted-foreground">
              {recipe.calories > 0 && (
                <span className="flex items-center gap-1">
                  <Flame className="w-3.5 h-3.5 text-secondary" />
                  {recipe.calories} kcal
                </span>
              )}
              {recipe.cost > 0 && (
                <span className="flex items-center gap-1">
                  <Wallet className="w-3.5 h-3.5 text-primary" />
                  {formatCost(recipe.cost)}
                </span>
              )}
              {recipe.servings > 0 && (
                <span>{recipe.servings} người</span>
              )}
            </div>
          </div>
        </Card>
      </Link>
    </motion.div>
  );
}