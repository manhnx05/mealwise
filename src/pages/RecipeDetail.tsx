import React from 'react';
import { base44 } from '@/api/base44Client';
import { useQuery } from '@tanstack/react-query';
import { Link } from 'react-router-dom';
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Card } from "@/components/ui/card";
import { Separator } from "@/components/ui/separator";
import { ArrowLeft, Clock, Flame, Wallet, Users, Beef, Droplets, Wheat } from 'lucide-react';
import { Skeleton } from "@/components/ui/skeleton";
import { motion } from 'framer-motion';

const categoryLabels = {
  quick_meal: 'Nhanh gọn', low_fat: 'Ít dầu mỡ', weight_loss: 'Giảm cân',
  gym: 'Gym', healthy: 'Lành mạnh', budget: 'Tiết kiệm', vegetarian: 'Chay',
};

export default function RecipeDetail() {
  const urlParams = new URLSearchParams(window.location.search);
  const pathParts = window.location.pathname.split('/');
  const recipeId = pathParts[pathParts.length - 1];

  const { data: recipes = [], isLoading } = useQuery({
    queryKey: ['recipe', recipeId],
    queryFn: () => base44.entities.Recipe.filter({ id: recipeId }),
    enabled: !!recipeId,
  });

  const recipe = recipes[0];

  const formatCost = (cost) => {
    if (!cost) return '';
    return new Intl.NumberFormat('vi-VN').format(cost) + 'đ';
  };

  if (isLoading) {
    return (
      <div className="max-w-4xl mx-auto px-4 sm:px-6 py-8">
        <Skeleton className="h-8 w-40 mb-6" />
        <Skeleton className="aspect-video rounded-2xl mb-6" />
        <Skeleton className="h-10 w-3/4 mb-4" />
        <Skeleton className="h-5 w-1/2" />
      </div>
    );
  }

  if (!recipe) {
    return (
      <div className="max-w-4xl mx-auto px-4 sm:px-6 py-20 text-center">
        <p className="text-muted-foreground text-lg">Không tìm thấy công thức</p>
        <Link to="/recipes">
          <Button variant="outline" className="mt-4">Quay lại danh sách</Button>
        </Link>
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 py-8">
      <Link to="/recipes">
        <Button variant="ghost" size="sm" className="gap-2 mb-6">
          <ArrowLeft className="w-4 h-4" /> Quay lại
        </Button>
      </Link>

      <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }}>
        <div className="relative aspect-video rounded-2xl overflow-hidden mb-8">
          <img
            src={recipe.image_url || 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=1200&h=675&fit=crop'}
            alt={recipe.title}
            className="w-full h-full object-cover"
          />
          {recipe.category && (
            <Badge className="absolute top-4 left-4 bg-card/90 text-foreground backdrop-blur-sm border-0">
              {categoryLabels[recipe.category]}
            </Badge>
          )}
        </div>

        <h1 className="font-display text-3xl sm:text-4xl font-bold text-foreground mb-3">
          {recipe.title}
        </h1>
        {recipe.description && (
          <p className="text-lg text-muted-foreground mb-6">{recipe.description}</p>
        )}

        <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 mb-8">
          {recipe.cook_time > 0 && (
            <Card className="p-4 text-center">
              <Clock className="w-5 h-5 text-primary mx-auto mb-2" />
              <p className="text-lg font-bold">{recipe.cook_time}p</p>
              <p className="text-xs text-muted-foreground">Thời gian</p>
            </Card>
          )}
          {recipe.calories > 0 && (
            <Card className="p-4 text-center">
              <Flame className="w-5 h-5 text-secondary mx-auto mb-2" />
              <p className="text-lg font-bold">{recipe.calories}</p>
              <p className="text-xs text-muted-foreground">Calo (kcal)</p>
            </Card>
          )}
          {recipe.cost > 0 && (
            <Card className="p-4 text-center">
              <Wallet className="w-5 h-5 text-primary mx-auto mb-2" />
              <p className="text-lg font-bold">{formatCost(recipe.cost)}</p>
              <p className="text-xs text-muted-foreground">Chi phí</p>
            </Card>
          )}
          {recipe.servings > 0 && (
            <Card className="p-4 text-center">
              <Users className="w-5 h-5 text-secondary mx-auto mb-2" />
              <p className="text-lg font-bold">{recipe.servings}</p>
              <p className="text-xs text-muted-foreground">Người ăn</p>
            </Card>
          )}
        </div>

        {/* Nutrition */}
        {(recipe.protein > 0 || recipe.fat > 0 || recipe.fiber > 0 || recipe.carbs > 0) && (
          <Card className="p-6 mb-8">
            <h2 className="font-semibold text-foreground mb-4">Thông tin dinh dưỡng</h2>
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
              {recipe.protein > 0 && (
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-lg bg-primary/10 flex items-center justify-center">
                    <Beef className="w-5 h-5 text-primary" />
                  </div>
                  <div>
                    <p className="font-semibold">{recipe.protein}g</p>
                    <p className="text-xs text-muted-foreground">Protein</p>
                  </div>
                </div>
              )}
              {recipe.fat > 0 && (
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-lg bg-secondary/10 flex items-center justify-center">
                    <Droplets className="w-5 h-5 text-secondary" />
                  </div>
                  <div>
                    <p className="font-semibold">{recipe.fat}g</p>
                    <p className="text-xs text-muted-foreground">Chất béo</p>
                  </div>
                </div>
              )}
              {recipe.carbs > 0 && (
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-lg bg-primary/10 flex items-center justify-center">
                    <Wheat className="w-5 h-5 text-primary" />
                  </div>
                  <div>
                    <p className="font-semibold">{recipe.carbs}g</p>
                    <p className="text-xs text-muted-foreground">Carbs</p>
                  </div>
                </div>
              )}
              {recipe.fiber > 0 && (
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-lg bg-accent flex items-center justify-center">
                    <Wheat className="w-5 h-5 text-accent-foreground" />
                  </div>
                  <div>
                    <p className="font-semibold">{recipe.fiber}g</p>
                    <p className="text-xs text-muted-foreground">Chất xơ</p>
                  </div>
                </div>
              )}
            </div>
          </Card>
        )}

        {/* Ingredients */}
        {recipe.ingredients?.length > 0 && (
          <div className="mb-8">
            <h2 className="font-display text-xl font-bold text-foreground mb-4">Nguyên liệu</h2>
            <Card className="divide-y divide-border">
              {recipe.ingredients.map((ing, i) => (
                <div key={i} className="flex items-center justify-between p-4">
                  <div className="flex items-center gap-3">
                    <div className="w-2 h-2 rounded-full bg-primary" />
                    <span className="font-medium">{ing.name}</span>
                  </div>
                  <div className="flex items-center gap-4 text-sm text-muted-foreground">
                    <span>{ing.amount}</span>
                    {ing.calories > 0 && <span>{ing.calories} kcal</span>}
                    {ing.cost > 0 && <span>{formatCost(ing.cost)}</span>}
                  </div>
                </div>
              ))}
            </Card>
          </div>
        )}

        {/* Steps */}
        {recipe.steps?.length > 0 && (
          <div className="mb-8">
            <h2 className="font-display text-xl font-bold text-foreground mb-4">Hướng dẫn nấu</h2>
            <div className="space-y-4">
              {recipe.steps.map((step, i) => (
                <Card key={i} className="p-5">
                  <div className="flex gap-4">
                    <div className="w-8 h-8 rounded-full bg-primary text-primary-foreground flex items-center justify-center text-sm font-bold shrink-0">
                      {step.step_number || i + 1}
                    </div>
                    <div className="flex-1">
                      <p className="text-foreground">{step.instruction}</p>
                      {step.image_url && (
                        <img src={step.image_url} alt="" className="mt-3 rounded-xl max-h-60 object-cover" />
                      )}
                    </div>
                  </div>
                </Card>
              ))}
            </div>
          </div>
        )}

        {/* Video */}
        {recipe.video_url && (
          <div className="mb-8">
            <h2 className="font-display text-xl font-bold text-foreground mb-4">Video hướng dẫn</h2>
            <div className="aspect-video rounded-2xl overflow-hidden bg-muted">
              <iframe
                src={recipe.video_url}
                className="w-full h-full"
                allowFullScreen
                title="Video hướng dẫn"
              />
            </div>
          </div>
        )}
      </motion.div>
    </div>
  );
}