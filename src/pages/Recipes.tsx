import React, { useState } from 'react';
import { base44 } from '@/api/base44Client';
import { useQuery } from '@tanstack/react-query';
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Tabs, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Search, Plus } from 'lucide-react';
import { Skeleton } from "@/components/ui/skeleton";
import { Link } from 'react-router-dom';
import { useAuth } from '@/lib/AuthContext';
import RecipeCard from '../components/recipes/RecipeCard';

const ADMIN_EMAIL = 'nguyetuyetak2005@gmail.com';

const categories = [
  { value: 'all', label: 'Tất cả' },
  { value: 'quick_meal', label: 'Nhanh gọn' },
  { value: 'budget', label: 'Tiết kiệm' },
  { value: 'healthy', label: 'Lành mạnh' },
  { value: 'low_fat', label: 'Ít dầu mỡ' },
  { value: 'weight_loss', label: 'Giảm cân' },
  { value: 'gym', label: 'Gym' },
  { value: 'vegetarian', label: 'Chay' },
];

export default function Recipes() {
  const { user: ctxUser } = useAuth();
  const { data: currentUser } = useQuery({
    queryKey: ['current-user'],
    queryFn: () => base44.auth.me(),
    retry: false,
  });
  const user = ctxUser || currentUser;
  const isAdmin = user?.email === ADMIN_EMAIL;
  const [search, setSearch] = useState('');
  const [category, setCategory] = useState('all');

  const { data: recipes = [], isLoading } = useQuery({
    queryKey: ['recipes'],
    queryFn: () => base44.entities.Recipe.list('-created_date', 50),
  });

  const filtered = recipes.filter(r => {
    const matchSearch = !search || r.title?.toLowerCase().includes(search.toLowerCase());
    const matchCat = category === 'all' || r.category === category;
    return matchSearch && matchCat;
  });

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 py-8 sm:py-12">
      <div className="flex items-start justify-between mb-8">
        <div>
          <h1 className="font-display text-3xl sm:text-4xl font-bold text-foreground mb-2">
            Công thức nấu ăn
          </h1>
          <p className="text-muted-foreground">
            Khám phá hàng trăm món ăn đơn giản, nhanh gọn với hướng dẫn chi tiết
          </p>
        </div>
        {isAdmin && (
          <Link to="/add-recipe">
            <Button className="rounded-full gap-2 shrink-0">
              <Plus className="w-4 h-4" /> Thêm công thức
            </Button>
          </Link>
        )}
      </div>

      <div className="flex flex-col sm:flex-row gap-4 mb-6">
        <div className="relative flex-1">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-muted-foreground" />
          <Input
            placeholder="Tìm kiếm món ăn..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="pl-10 rounded-full"
          />
        </div>
      </div>

      <div className="mb-8 overflow-x-auto">
        <Tabs value={category} onValueChange={setCategory}>
          <TabsList className="bg-muted/50 h-auto p-1 flex-nowrap">
            {categories.map(c => (
              <TabsTrigger key={c.value} value={c.value} className="text-sm whitespace-nowrap">
                {c.label}
              </TabsTrigger>
            ))}
          </TabsList>
        </Tabs>
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
          <p className="text-muted-foreground text-lg">Không tìm thấy món ăn nào</p>
          <p className="text-sm text-muted-foreground mt-2">Thử tìm kiếm với từ khóa khác</p>
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