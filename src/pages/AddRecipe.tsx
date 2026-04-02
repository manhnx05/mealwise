import React, { useState } from 'react';
import { base44 } from '@/api/base44Client';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '@/lib/AuthContext';
import { useQuery } from '@tanstack/react-query';
import { Button } from "@/components/ui/button";

const ADMIN_EMAIL = 'nguyetuyetak2005@gmail.com';
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { Card } from "@/components/ui/card";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { ArrowLeft, Plus, Trash2, Image, Loader2 } from 'lucide-react';

const categories = [
  { value: 'quick_meal', label: 'Nhanh gọn' },
  { value: 'budget', label: 'Tiết kiệm' },
  { value: 'healthy', label: 'Lành mạnh' },
  { value: 'low_fat', label: 'Ít dầu mỡ' },
  { value: 'weight_loss', label: 'Giảm cân' },
  { value: 'gym', label: 'Gym' },
  { value: 'vegetarian', label: 'Chay' },
];

export default function AddRecipe() {
  const navigate = useNavigate();
  const { user: ctxUser } = useAuth();
  const { data: currentUser } = useQuery({
    queryKey: ['current-user'],
    queryFn: () => base44.auth.me(),
    retry: false,
  });
  const user = ctxUser || currentUser;
  const [saving, setSaving] = useState(false);
  const [uploading, setUploading] = useState(false);

  const [form, setForm] = useState({
    title: '',
    description: '',
    image_url: '',
    cook_time: '',
    servings: '',
    cost: '',
    calories: '',
    protein: '',
    fat: '',
    carbs: '',
    fiber: '',
    category: '',
  });

  const [ingredients, setIngredients] = useState([{ name: '', amount: '', calories: '', cost: '' }]);
  const [steps, setSteps] = useState([{ step_number: 1, instruction: '' }]);

  if (user && user.email !== ADMIN_EMAIL) {
    return (
      <div className="max-w-xl mx-auto px-4 py-20 text-center">
        <p className="text-2xl mb-3">🔒</p>
        <h2 className="text-xl font-semibold mb-2">Không có quyền truy cập</h2>
        <p className="text-muted-foreground mb-6">Chỉ admin mới có thể thêm công thức.</p>
        <button onClick={() => navigate('/recipes')} className="text-primary underline text-sm">Quay lại</button>
      </div>
    );
  }


  const set = (key, val) => setForm(f => ({ ...f, [key]: val }));

  const handleImageUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;
    setUploading(true);
    const { file_url } = await base44.integrations.Core.UploadFile({ file });
    set('image_url', file_url);
    setUploading(false);
  };

  const addIngredient = () => setIngredients([...ingredients, { name: '', amount: '', calories: '', cost: '' }]);
  const removeIngredient = (i) => setIngredients(ingredients.filter((_, idx) => idx !== i));
  const updateIngredient = (i, key, val) => {
    const updated = [...ingredients];
    updated[i] = { ...updated[i], [key]: val };
    setIngredients(updated);
  };

  const addStep = () => setSteps([...steps, { step_number: steps.length + 1, instruction: '' }]);
  const removeStep = (i) => setSteps(steps.filter((_, idx) => idx !== i).map((s, idx) => ({ ...s, step_number: idx + 1 })));
  const updateStep = (i, val) => {
    const updated = [...steps];
    updated[i] = { ...updated[i], instruction: val };
    setSteps(updated);
  };

  const handleSave = async () => {
    if (!form.title || !form.cook_time) return;
    setSaving(true);
    const payload = {
      ...form,
      cook_time: Number(form.cook_time),
      servings: form.servings ? Number(form.servings) : undefined,
      cost: form.cost ? Number(form.cost) : undefined,
      calories: form.calories ? Number(form.calories) : undefined,
      protein: form.protein ? Number(form.protein) : undefined,
      fat: form.fat ? Number(form.fat) : undefined,
      carbs: form.carbs ? Number(form.carbs) : undefined,
      fiber: form.fiber ? Number(form.fiber) : undefined,
      ingredients: ingredients.filter(i => i.name).map(i => ({
        ...i,
        calories: i.calories ? Number(i.calories) : 0,
        cost: i.cost ? Number(i.cost) : 0,
      })),
      steps: steps.filter(s => s.instruction),
    };
    await base44.entities.Recipe.create(payload);
    setSaving(false);
    navigate('/recipes');
  };

  return (
    <div className="max-w-3xl mx-auto px-4 sm:px-6 py-8">
      <button onClick={() => navigate('/recipes')} className="flex items-center gap-2 text-sm text-muted-foreground hover:text-foreground mb-6 transition-colors">
        <ArrowLeft className="w-4 h-4" /> Quay lại công thức
      </button>

      <h1 className="font-display text-3xl font-bold text-foreground mb-8">Thêm công thức mới</h1>

      {/* Basic Info */}
      <Card className="p-6 mb-6 space-y-4">
        <h2 className="font-semibold text-lg">Thông tin cơ bản</h2>
        <Input
          placeholder="Tên món ăn *"
          value={form.title}
          onChange={e => set('title', e.target.value)}
        />
        <Textarea
          placeholder="Mô tả ngắn về món ăn"
          value={form.description}
          onChange={e => set('description', e.target.value)}
          rows={3}
        />
        <div>
          <label className="flex items-center gap-2 cursor-pointer text-sm text-muted-foreground hover:text-foreground transition-colors">
            <Image className="w-4 h-4" />
            {uploading ? 'Đang tải...' : form.image_url ? 'Đổi ảnh' : 'Tải ảnh món ăn'}
            <input type="file" accept="image/*" className="hidden" onChange={handleImageUpload} disabled={uploading} />
          </label>
          {form.image_url && (
            <img src={form.image_url} alt="" className="mt-3 rounded-xl h-48 w-full object-cover" />
          )}
        </div>
        <Select value={form.category} onValueChange={v => set('category', v)}>
          <SelectTrigger>
            <SelectValue placeholder="Phân loại món ăn" />
          </SelectTrigger>
          <SelectContent>
            {categories.map(c => (
              <SelectItem key={c.value} value={c.value}>{c.label}</SelectItem>
            ))}
          </SelectContent>
        </Select>
      </Card>

      {/* Numbers */}
      <Card className="p-6 mb-6">
        <h2 className="font-semibold text-lg mb-4">Thời gian & Chi phí</h2>
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
          <div>
            <label className="text-xs text-muted-foreground mb-1 block">Thời gian (phút) *</label>
            <Input type="number" placeholder="10" value={form.cook_time} onChange={e => set('cook_time', e.target.value)} />
          </div>
          <div>
            <label className="text-xs text-muted-foreground mb-1 block">Số người ăn</label>
            <Input type="number" placeholder="2" value={form.servings} onChange={e => set('servings', e.target.value)} />
          </div>
          <div>
            <label className="text-xs text-muted-foreground mb-1 block">Chi phí (VNĐ)</label>
            <Input type="number" placeholder="20000" value={form.cost} onChange={e => set('cost', e.target.value)} />
          </div>
          <div>
            <label className="text-xs text-muted-foreground mb-1 block">Calo (kcal)</label>
            <Input type="number" placeholder="350" value={form.calories} onChange={e => set('calories', e.target.value)} />
          </div>
        </div>
      </Card>

      {/* Nutrition */}
      <Card className="p-6 mb-6">
        <h2 className="font-semibold text-lg mb-4">Dinh dưỡng (không bắt buộc)</h2>
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
          {[['protein', 'Protein (g)'], ['fat', 'Chất béo (g)'], ['carbs', 'Carbs (g)'], ['fiber', 'Chất xơ (g)']].map(([key, label]) => (
            <div key={key}>
              <label className="text-xs text-muted-foreground mb-1 block">{label}</label>
              <Input type="number" placeholder="0" value={form[key]} onChange={e => set(key, e.target.value)} />
            </div>
          ))}
        </div>
      </Card>

      {/* Ingredients */}
      <Card className="p-6 mb-6">
        <div className="flex items-center justify-between mb-4">
          <h2 className="font-semibold text-lg">Nguyên liệu</h2>
          <Button variant="outline" size="sm" onClick={addIngredient} className="gap-1">
            <Plus className="w-3.5 h-3.5" /> Thêm
          </Button>
        </div>
        <div className="space-y-3">
          {ingredients.map((ing, i) => (
            <div key={i} className="flex gap-2 items-center">
              <Input placeholder="Tên nguyên liệu" value={ing.name} onChange={e => updateIngredient(i, 'name', e.target.value)} className="flex-[2]" />
              <Input placeholder="Lượng (VD: 200g)" value={ing.amount} onChange={e => updateIngredient(i, 'amount', e.target.value)} className="flex-1" />
              <Input type="number" placeholder="Calo" value={ing.calories} onChange={e => updateIngredient(i, 'calories', e.target.value)} className="w-20 hidden sm:block" />
              <button onClick={() => removeIngredient(i)} className="text-muted-foreground hover:text-destructive transition-colors shrink-0">
                <Trash2 className="w-4 h-4" />
              </button>
            </div>
          ))}
        </div>
      </Card>

      {/* Steps */}
      <Card className="p-6 mb-8">
        <div className="flex items-center justify-between mb-4">
          <h2 className="font-semibold text-lg">Các bước nấu</h2>
          <Button variant="outline" size="sm" onClick={addStep} className="gap-1">
            <Plus className="w-3.5 h-3.5" /> Thêm bước
          </Button>
        </div>
        <div className="space-y-3">
          {steps.map((step, i) => (
            <div key={i} className="flex gap-3 items-start">
              <div className="w-8 h-8 rounded-full bg-primary text-primary-foreground flex items-center justify-center text-sm font-bold shrink-0 mt-1">
                {step.step_number}
              </div>
              <Textarea
                placeholder={`Hướng dẫn bước ${step.step_number}...`}
                value={step.instruction}
                onChange={e => updateStep(i, e.target.value)}
                rows={2}
                className="flex-1"
              />
              {steps.length > 1 && (
                <button onClick={() => removeStep(i)} className="text-muted-foreground hover:text-destructive transition-colors mt-2 shrink-0">
                  <Trash2 className="w-4 h-4" />
                </button>
              )}
            </div>
          ))}
        </div>
      </Card>

      <div className="flex gap-3 justify-end">
        <Button variant="outline" onClick={() => navigate('/recipes')}>Hủy</Button>
        <Button onClick={handleSave} disabled={!form.title || !form.cook_time || saving} className="gap-2 px-8">
          {saving ? <><Loader2 className="w-4 h-4 animate-spin" /> Đang lưu...</> : 'Đăng công thức'}
        </Button>
      </div>
    </div>
  );
}