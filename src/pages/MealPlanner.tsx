import React, { useState } from 'react';
import { base44 } from '@/api/base44Client';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { Checkbox } from "@/components/ui/checkbox";
import { Badge } from "@/components/ui/badge";
import { Calendar, ShoppingCart, Sparkles, Loader2, RefreshCw, Printer } from 'lucide-react';
import { motion } from 'framer-motion';

const defaultDays = ['Thứ 2', 'Thứ 3', 'Thứ 4', 'Thứ 5', 'Thứ 6', 'Thứ 7', 'Chủ nhật'];

export default function MealPlanner() {
  const [isGenerating, setIsGenerating] = useState(false);
  const queryClient = useQueryClient();

  const { data: plans = [] } = useQuery({
    queryKey: ['meal-plans'],
    queryFn: () => base44.entities.MealPlan.list('-created_date', 1),
  });

  const currentPlan = plans[0];

  const generatePlan = async () => {
    setIsGenerating(true);
    try {
      const response = await base44.integrations.Core.InvokeLLM({
        prompt: `Tạo thực đơn ăn uống cho 7 ngày (Thứ 2 đến Chủ nhật) cho gia đình Việt Nam. 
        Mỗi ngày có bữa sáng, trưa, tối. Món ăn đơn giản, dễ nấu, tiết kiệm.
        Cũng tạo danh sách đi chợ cho cả tuần.
        Trả về JSON theo format:`,
        response_json_schema: {
          type: "object",
          properties: {
            meals: {
              type: "array",
              items: {
                type: "object",
                properties: {
                  day: { type: "string" },
                  breakfast: { type: "string" },
                  lunch: { type: "string" },
                  dinner: { type: "string" }
                }
              }
            },
            shopping_list: {
              type: "array",
              items: {
                type: "object",
                properties: {
                  name: { type: "string" },
                  amount: { type: "string" }
                }
              }
            },
            total_cost: { type: "number" }
          }
        }
      });

      const responseData = typeof response === 'string' ? JSON.parse(response) : response;

      const planData = {
        week_start: new Date().toISOString().split('T')[0],
        meals: responseData.meals || [],
        shopping_list: (responseData.shopping_list || []).map((item: any) => ({ ...item, checked: false })),
        total_cost: responseData.total_cost || 0,
      };

      if (currentPlan) {
        await base44.entities.MealPlan.update(currentPlan.id, planData);
      } else {
        await base44.entities.MealPlan.create(planData);
      }

      queryClient.invalidateQueries({ queryKey: ['meal-plans'] });
    } catch (err: any) {
      console.error('Lỗi tạo thực đơn:', err);
      const backendMessage = err.message || '';
      if (backendMessage.includes('exceeded') || backendMessage.includes('RESOURCE_EXHAUSTED')) {
         alert('API Key của bạn đã hết lượt giới hạn (Quota Exceeded). Vui lòng đổi API Key mới trong file .env và khởi động lại dịch vụ.');
      } else {
         alert(`Không thể tạo thực đơn lúc này. Chi tiết lỗi: ${backendMessage}\n\nVui lòng kiểm tra cấu hình.`);
      }
    } finally {
      setIsGenerating(false);
    }
  };

  const toggleShoppingItem = async (index) => {
    if (!currentPlan) return;
    const newList = [...currentPlan.shopping_list];
    newList[index] = { ...newList[index], checked: !newList[index].checked };
    await base44.entities.MealPlan.update(currentPlan.id, { shopping_list: newList });
    queryClient.invalidateQueries({ queryKey: ['meal-plans'] });
  };

  const formatCost = (cost) => {
    if (!cost) return '0đ';
    return new Intl.NumberFormat('vi-VN').format(cost) + 'đ';
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 py-8 sm:py-12">
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 mb-8">
        <div>
          <h1 className="font-display text-3xl sm:text-4xl font-bold text-foreground mb-2">
            Thực đơn cả tuần
          </h1>
          <p className="text-muted-foreground">
            Gợi ý menu 7 ngày, không cần nghĩ hôm nay ăn gì
          </p>
        </div>
        <Button
          onClick={generatePlan}
          disabled={isGenerating}
          className="rounded-full gap-2"
        >
          {isGenerating ? (
            <><Loader2 className="w-4 h-4 animate-spin" /> Đang tạo...</>
          ) : currentPlan ? (
            <><RefreshCw className="w-4 h-4" /> Tạo lại thực đơn</>
          ) : (
            <><Sparkles className="w-4 h-4" /> Tạo thực đơn AI</>
          )}
        </Button>
      </div>

      {!currentPlan && !isGenerating && (
        <Card className="p-12 text-center">
          <Calendar className="w-12 h-12 text-muted-foreground mx-auto mb-4" />
          <h3 className="text-lg font-semibold mb-2">Chưa có thực đơn</h3>
          <p className="text-muted-foreground mb-6">Nhấn "Tạo thực đơn AI" để hệ thống gợi ý menu cả tuần cho bạn</p>
        </Card>
      )}

      {isGenerating && (
        <Card className="p-12 text-center">
          <Loader2 className="w-10 h-10 text-primary animate-spin mx-auto mb-4" />
          <p className="text-muted-foreground">Đang tạo thực đơn thông minh...</p>
        </Card>
      )}

      {currentPlan && !isGenerating && (
        <div className="grid lg:grid-cols-3 gap-8">
          <div className="lg:col-span-2">
            <div className="flex items-center gap-2 mb-4">
              <Calendar className="w-5 h-5 text-primary" />
              <h2 className="text-lg font-semibold">Menu 7 ngày</h2>
              {currentPlan.total_cost > 0 && (
                <Badge variant="secondary" className="ml-auto">
                  Tổng: ~{formatCost(currentPlan.total_cost)}
                </Badge>
              )}
            </div>
            <div className="space-y-3">
              {(currentPlan.meals || []).map((meal, i) => (
                <motion.div
                  key={i}
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: i * 0.05 }}
                >
                  <Card className="p-4">
                    <div className="flex flex-col sm:flex-row sm:items-center gap-3">
                      <Badge variant="secondary" className="bg-primary text-primary-foreground w-fit">{meal.day}</Badge>
                      <div className="flex-1 grid sm:grid-cols-3 gap-2 text-sm">
                        <div>
                          <span className="text-muted-foreground">Sáng: </span>
                          <span className="font-medium">{meal.breakfast}</span>
                        </div>
                        <div>
                          <span className="text-muted-foreground">Trưa: </span>
                          <span className="font-medium">{meal.lunch}</span>
                        </div>
                        <div>
                          <span className="text-muted-foreground">Tối: </span>
                          <span className="font-medium">{meal.dinner}</span>
                        </div>
                      </div>
                    </div>
                  </Card>
                </motion.div>
              ))}
            </div>
          </div>

          <div>
            <div className="flex items-center gap-2 mb-4">
              <ShoppingCart className="w-5 h-5 text-secondary" />
              <h2 className="text-lg font-semibold">Danh sách đi chợ</h2>
            </div>
            <Card className="p-4">
              <div className="space-y-3">
                {(currentPlan.shopping_list || []).map((item, i) => (
                  <div
                    key={i}
                    className="flex items-center gap-3 cursor-pointer"
                    onClick={() => toggleShoppingItem(i)}
                  >
                    <Checkbox checked={item.checked} />
                    <span className={`flex-1 text-sm ${item.checked ? 'line-through text-muted-foreground' : ''}`}>
                      {item.name}
                    </span>
                    <span className="text-xs text-muted-foreground">{item.amount}</span>
                  </div>
                ))}
              </div>
              {currentPlan.shopping_list?.length > 0 && (
                <div className="mt-4 pt-4 border-t">
                  <p className="text-xs text-muted-foreground text-center">
                    {currentPlan.shopping_list.filter(i => i.checked).length}/{currentPlan.shopping_list.length} đã mua
                  </p>
                </div>
              )}
            </Card>
          </div>
        </div>
      )}
    </div>
  );
}