import React from 'react';
import { Link } from 'react-router-dom';
import { base44 } from '@/api/base44Client';
import { useQuery } from '@tanstack/react-query';
import { Button } from "@/components/ui/button";
import { ArrowRight } from 'lucide-react';
import { Skeleton } from "@/components/ui/skeleton";
import RecipeCard from '../recipes/RecipeCard';

export default function QuickRecipes() {
  const { data: recipes = [], isLoading } = useQuery({
    queryKey: ['quick-recipes'],
    queryFn: () => base44.entities.Recipe.list('-created_date', 6),
  });

  return (
    <section className="max-w-7xl mx-auto px-4 sm:px-6 py-16">
      <div className="flex items-end justify-between mb-8">
        <div>
          <h2 className="font-display text-3xl font-bold text-foreground mb-2">
            Công thức nấu nhanh
          </h2>
          <p className="text-muted-foreground">
            Món ăn dễ nấu trong 10-15 phút, hoàn hảo cho người bận rộn
          </p>
        </div>
        <Link to="/recipes" className="hidden sm:block">
          <Button variant="ghost" className="gap-2">
            Xem tất cả <ArrowRight className="w-4 h-4" />
          </Button>
        </Link>
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
      ) : (
        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {recipes.map((recipe, i) => (
            <RecipeCard key={recipe.id} recipe={recipe} index={i} />
          ))}
        </div>
      )}

      <Link to="/recipes" className="block sm:hidden mt-6">
        <Button variant="outline" className="w-full gap-2">
          Xem tất cả công thức <ArrowRight className="w-4 h-4" />
        </Button>
      </Link>
    </section>
  );
}