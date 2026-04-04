import React, { useState } from 'react';
import { base44 } from '@/api/base44Client';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { Badge } from "@/components/ui/badge";
import { Skeleton } from "@/components/ui/skeleton";
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog";
import { Users, Plus, Star, MessageCircle, Image } from 'lucide-react';
import { motion } from 'framer-motion';
import CommunityPostCard from '../components/community/CommunityPostCard';

export default function Community() {
  const [showCreate, setShowCreate] = useState(false);
  const [newPost, setNewPost] = useState({ title: '', description: '', recipe_text: '', image_url: '' });
  const [uploading, setUploading] = useState(false);
  const queryClient = useQueryClient();

  const { data: posts = [], isLoading } = useQuery({
    queryKey: ['community-posts'],
    queryFn: () => base44.entities.CommunityPost.list('-created_date', 50),
  });

  const createMutation = useMutation({
    mutationFn: (data: any) => base44.entities.CommunityPost.create(data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['community-posts'] });
      setShowCreate(false);
      setNewPost({ title: '', description: '', recipe_text: '', image_url: '' });
    },
  });

  const handleImageUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;
    setUploading(true);
    const { file_url } = await base44.integrations.Core.UploadFile({ file });
    setNewPost({ ...newPost, image_url: file_url });
    setUploading(false);
  };

  const handleCreate = () => {
    if (!newPost.title) return;
    createMutation.mutate({
      ...newPost,
      rating: 0,
      rating_count: 0,
      comments: [],
    });
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 py-8 sm:py-12">
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 mb-8">
        <div>
          <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-primary/10 text-primary text-sm font-medium mb-3">
            <Users className="w-4 h-4" />
            Cộng đồng
          </div>
          <h1 className="font-display text-3xl sm:text-4xl font-bold text-foreground mb-2">
            Cộng đồng nấu ăn
          </h1>
          <p className="text-muted-foreground">
            Chia sẻ công thức, đánh giá và cùng nhau nấu ăn ngon hơn
          </p>
        </div>

        <Dialog open={showCreate} onOpenChange={setShowCreate}>
          <DialogTrigger asChild>
            <Button className="rounded-full gap-2">
              <Plus className="w-4 h-4" /> Chia sẻ công thức
            </Button>
          </DialogTrigger>
          <DialogContent className="max-w-lg">
            <DialogHeader className="">
              <DialogTitle>Chia sẻ công thức mới</DialogTitle>
            </DialogHeader>
            <div className="space-y-4 mt-4">
              <Input
                placeholder="Tên món ăn"
                value={newPost.title}
                onChange={(e) => setNewPost({ ...newPost, title: e.target.value })}
              />
              <Input
                placeholder="Mô tả ngắn"
                value={newPost.description}
                onChange={(e) => setNewPost({ ...newPost, description: e.target.value })}
              />
              <Textarea
                placeholder="Công thức nấu ăn chi tiết..."
                value={newPost.recipe_text}
                onChange={(e) => setNewPost({ ...newPost, recipe_text: e.target.value })}
                rows={5}
              />
              <div>
                <label className="flex items-center gap-2 cursor-pointer text-sm text-muted-foreground hover:text-foreground transition-colors">
                  <Image className="w-4 h-4" />
                  {uploading ? 'Đang tải...' : newPost.image_url ? 'Đã tải ảnh ✓' : 'Tải ảnh món ăn'}
                  <input type="file" accept="image/*" className="hidden" onChange={handleImageUpload} />
                </label>
                {newPost.image_url && (
                  <img src={newPost.image_url} alt="" className="mt-2 rounded-lg h-32 object-cover" />
                )}
              </div>
              <Button
                onClick={handleCreate}
                disabled={!newPost.title || createMutation.isPending}
                className="w-full"
              >
                {createMutation.isPending ? 'Đang đăng...' : 'Đăng bài'}
              </Button>
            </div>
          </DialogContent>
        </Dialog>
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
      ) : posts.length === 0 ? (
        <Card className="p-12 text-center">
          <Users className="w-10 h-10 text-muted-foreground mx-auto mb-3" />
          <h3 className="text-lg font-semibold mb-2">Chưa có bài viết nào</h3>
          <p className="text-muted-foreground mb-4">Hãy là người đầu tiên chia sẻ công thức!</p>
        </Card>
      ) : (
        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {posts.map((post, i) => (
            <CommunityPostCard key={post.id} post={post} index={i} />
          ))}
        </div>
      )}
    </div>
  );
}