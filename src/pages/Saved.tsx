import React from 'react';
import { Link } from 'react-router-dom';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { base44 } from '@/api/base44Client';
import { Card } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Bookmark, Clock, Trash2, ChefHat, ArrowLeft } from 'lucide-react';
import { motion } from 'framer-motion';
import { useToast } from '@/components/ui/use-toast';

export default function Saved() {
  const queryClient = useQueryClient();
  const { toast } = useToast();

  const { data: savedList = [], isLoading } = useQuery({
    queryKey: ['saved-recipes'],
    queryFn: () => fetch('/api/saved-recipes').then(r => r.json()),
  });

  const unsaveMutation = useMutation({
    mutationFn: (recipeId: number) =>
      fetch(`/api/saved-recipes/${recipeId}`, { method: 'DELETE' }).then(r => r.json()),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['saved-recipes'] });
      toast({ title: 'Đã bỏ lưu công thức', variant: 'default' });
    },
  });

  const formatCost = (cost: number | null) => {
    if (!cost) return '';
    return new Intl.NumberFormat('vi-VN').format(cost) + 'đ';
  };

  if (isLoading) {
    return (
      <div className="max-w-7xl mx-auto px-4 sm:px-6 py-12">
        <div className="grid sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          {Array.from({ length: 8 }).map((_, i) => (
            <div key={i} className="h-64 rounded-2xl bg-slate-100 animate-pulse" />
          ))}
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 py-8 sm:py-12">
      {/* Header */}
      <div className="mb-8">
        <Link to="/recipes" className="inline-flex items-center gap-1.5 text-sm text-slate-500 hover:text-slate-700 mb-4 transition-colors">
          <ArrowLeft className="w-4 h-4" />
          Trở về công thức
        </Link>
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-amber-100 flex items-center justify-center">
            <Bookmark className="w-5 h-5 text-amber-600" />
          </div>
          <div>
            <h1 className="font-display text-3xl sm:text-4xl font-bold text-slate-900">Đã lưu</h1>
            <p className="text-slate-500 mt-1">
              {savedList.length > 0
                ? `${savedList.length} công thức yêu thích của bạn`
                : 'Chưa có công thức nào được lưu'}
            </p>
          </div>
        </div>
      </div>

      {/* Empty State */}
      {savedList.length === 0 && (
        <Card className="p-16 text-center">
          <div className="w-16 h-16 rounded-2xl bg-amber-50 flex items-center justify-center mx-auto mb-4">
            <Bookmark className="w-8 h-8 text-amber-400" />
          </div>
          <h3 className="text-lg font-semibold text-slate-800 mb-2">Chưa có gì ở đây</h3>
          <p className="text-slate-500 mb-6 max-w-sm mx-auto">
            Khi bạn lưu một công thức, nó sẽ xuất hiện ở đây để bạn dễ dàng tìm lại.
          </p>
          <Button asChild variant="outline" className="rounded-full">
            <Link to="/recipes">Khám phá công thức</Link>
          </Button>
        </Card>
      )}

      {/* Recipe Grid */}
      {savedList.length > 0 && (
        <div className="grid sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          {savedList.map((item: any, i: number) => {
            const recipe = item.recipe || item;
            return (
              <motion.div
                key={item.id}
                initial={{ opacity: 0, y: 16 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: i * 0.04 }}
              >
                <Card className="group overflow-hidden rounded-2xl border-0 shadow-sm hover:shadow-lg transition-all duration-300">
                  {/* Image */}
                  <div className="relative h-48 bg-slate-100">
                    {recipe.image_url ? (
                      <img
                        src={recipe.image_url}
                        alt={recipe.title}
                        className="w-full h-full object-cover"
                      />
                    ) : (
                      <div className="w-full h-full flex items-center justify-center">
                        <ChefHat className="w-10 h-10 text-slate-300" />
                      </div>
                    )}
                    {/* Unsave button */}
                    <button
                      onClick={() => unsaveMutation.mutate(recipe.id)}
                      className="absolute top-3 right-3 w-8 h-8 rounded-full bg-white/90 backdrop-blur-sm flex items-center justify-center shadow-sm opacity-0 group-hover:opacity-100 transition-opacity hover:bg-red-50 hover:text-red-500"
                    >
                      <Trash2 className="w-3.5 h-3.5" />
                    </button>
                    {recipe.category && (
                      <Badge variant="secondary" className="absolute top-3 left-3 bg-white/90 text-slate-700 backdrop-blur-sm text-xs">
                        {recipe.category}
                      </Badge>
                    )}
                  </div>

                  {/* Info */}
                  <div className="p-4">
                    <Link to={`/recipes/${recipe.id}`}>
                      <h3 className="font-semibold text-slate-900 mb-1 line-clamp-2 hover:text-[#2e8b57] transition-colors">
                        {recipe.title}
                      </h3>
                    </Link>
                    <p className="text-sm text-slate-500 line-clamp-2 mb-3">{recipe.description}</p>
                    <div className="flex items-center gap-3 text-xs text-slate-400">
                      {recipe.cook_time && (
                        <span className="flex items-center gap-1">
                          <Clock className="w-3 h-3" />
                          {recipe.cook_time} phút
                        </span>
                      )}
                      {recipe.cost && (
                        <span className="ml-auto font-medium text-[#2e8b57]">
                          {formatCost(recipe.cost)}
                        </span>
                      )}
                    </div>
                  </div>
                </Card>
              </motion.div>
            );
          })}
        </div>
      )}
    </div>
  );
}
