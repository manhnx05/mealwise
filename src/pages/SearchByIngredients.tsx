import React, { useState } from 'react';
import { base44 } from '@/api/base44Client';
import { useQuery } from '@tanstack/react-query';
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Search, X, Plus } from 'lucide-react';
import { Skeleton } from "@/components/ui/skeleton";
import RecipeCard from '../components/recipes/RecipeCard';

export default function SearchByIngredients() {
  const [ingredientInput, setIngredientInput] = useState('');
  const [selectedIngredients, setSelectedIngredients] = useState<string[]>([]);
  const [maxBudget, setMaxBudget] = useState<number | ''>('');
  const [maxTime, setMaxTime] = useState<number | ''>('');

  const { data: recipes = [], isLoading } = useQuery({
    queryKey: ['recipes'],
    queryFn: () => base44.entities.Recipe.list('-created_date', 50),
  });

  const handleAddIngredient = () => {
    const trimmed = ingredientInput.trim();
    if (trimmed && !selectedIngredients.includes(trimmed)) {
      setSelectedIngredients([...selectedIngredients, trimmed]);
      setIngredientInput('');
    }
  };

  const handleRemoveIngredient = (ingredient: string) => {
    setSelectedIngredients(selectedIngredients.filter(i => i !== ingredient));
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      handleAddIngredient();
    }
  };

  const filtered = recipes.filter((recipe: any) => {
    if (selectedIngredients.length > 0) {
      const recipeIngredients = recipe.ingredients?.map((ing: any) => 
        typeof ing === 'string' ? ing.toLowerCase() : ing.name?.toLowerCase() || ''
      ) || [];
      
      const hasAllIngredients = selectedIngredients.every(selected => 
        recipeIngredients.some((ing: string) => ing.includes(selected.toLowerCase()))
      );
      if (!hasAllIngredients) return false;
    }

    if (maxBudget !== '' && recipe.cost > (maxBudget as number)) {
      return false;
    }

    if (maxTime !== '' && recipe.cook_time > (maxTime as number)) {
      return false;
    }

    return true;
  });

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 py-8 sm:py-12">
      <div className="mb-8">
        <h1 className="font-display text-3xl sm:text-4xl font-bold text-foreground mb-2">
          Gợi ý món ăn thông minh
        </h1>
        <p className="text-muted-foreground">
          Quyết định ăn gì hôm nay dựa trên ngân sách, nguyên liệu có sẵn và thời gian nấu
        </p>
      </div>

      <div className="bg-card border rounded-xl p-6 mb-8">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
          <div className="flex gap-2">
            <div className="relative flex-1">
              <Input
                placeholder="Nhập nguyên liệu (vd: thịt gà)"
                value={ingredientInput}
                onChange={(e) => setIngredientInput(e.target.value)}
                onKeyPress={handleKeyPress}
                className="rounded-full"
              />
            </div>
            <Button 
              onClick={handleAddIngredient}
              className="rounded-full gap-2 shrink-0"
              disabled={!ingredientInput.trim()}
            >
              <Plus className="w-4 h-4" /> Thêm
            </Button>
          </div>
          <div>
            <Input
              type="number"
              placeholder="Ngân sách tối đa (VNĐ)"
              value={maxBudget}
              onChange={(e) => setMaxBudget(e.target.value === '' ? '' : Number(e.target.value))}
              className="rounded-full"
            />
          </div>
          <div>
            <Input
              type="number"
              placeholder="Thời gian tối đa (Phút)"
              value={maxTime}
              onChange={(e) => setMaxTime(e.target.value === '' ? '' : Number(e.target.value))}
              className="rounded-full"
            />
          </div>
        </div>

        {selectedIngredients.length > 0 && (
          <div className="flex flex-wrap gap-2 mt-4 pt-4 border-t">
            {selectedIngredients.map(ingredient => (
              <Badge 
                key={ingredient} 
                variant="secondary" 
                className="gap-2 py-1.5 px-3 text-sm"
              >
                {ingredient}
                <button
                  onClick={() => handleRemoveIngredient(ingredient)}
                  className="hover:text-destructive transition-colors"
                >
                  <X className="w-3 h-3" />
                </button>
              </Badge>
            ))}
          </div>
        )}
      </div>

      <div className="mb-4">
        <p className="text-sm text-muted-foreground">
          {selectedIngredients.length === 0 
            ? 'Hiển thị tất cả công thức' 
            : `Tìm thấy ${filtered.length} công thức phù hợp`}
        </p>
      </div>

      {isLoading ? (
        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {[...Array(6)].map((_, i) => (
            <div key={i} className="space-y-3">
              <Skeleton className="aspect-[4/3] rounded-xl" />
              <Skeleton className="h-5 w-3/4" />
              <Skeleton className="h-4 w-1/2" />
            </div>
          ))}
        </div>
      ) : filtered.length === 0 ? (
        <div className="text-center py-20">
          <Search className="w-16 h-16 mx-auto text-muted-foreground/50 mb-4" />
          <p className="text-muted-foreground text-lg">Không tìm thấy món ăn nào</p>
          <p className="text-sm text-muted-foreground mt-2">
            Thử thêm ít nguyên liệu hơn hoặc thay đổi nguyên liệu khác
          </p>
        </div>
      ) : (
        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {filtered.map((recipe, i) => (
            <RecipeCard key={recipe.id} recipe={recipe} index={i} />
          ))}
        </div>
      )}
    </div>
  );
}
