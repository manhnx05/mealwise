import React, { useState } from 'react';
import { base44 } from '@/api/base44Client';
import { useQueryClient } from '@tanstack/react-query';
import { Card } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Badge } from "@/components/ui/badge";
import { Star, MessageCircle, Send } from 'lucide-react';
import { motion } from 'framer-motion';
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog";

export default function CommunityPostCard({ post, index = 0 }) {
  const [showDetail, setShowDetail] = useState(false);
  const [comment, setComment] = useState('');
  const [myRating, setMyRating] = useState(0);
  const queryClient = useQueryClient();

  const handleRate = async (rating) => {
    setMyRating(rating);
    const newCount = (post.rating_count || 0) + 1;
    const newRating = ((post.rating || 0) * (post.rating_count || 0) + rating) / newCount;
    await base44.entities.CommunityPost.update(post.id, {
      rating: Math.round(newRating * 10) / 10,
      rating_count: newCount,
    });
    queryClient.invalidateQueries({ queryKey: ['community-posts'] });
  };

  const handleComment = async () => {
    if (!comment.trim()) return;
    const comments = [...(post.comments || []), {
      author: 'Bạn',
      text: comment,
      date: new Date().toISOString(),
    }];
    await base44.entities.CommunityPost.update(post.id, { comments });
    setComment('');
    queryClient.invalidateQueries({ queryKey: ['community-posts'] });
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: index * 0.05 }}
    >
      <Dialog open={showDetail} onOpenChange={setShowDetail}>
        <DialogTrigger asChild>
          <Card className="group overflow-hidden cursor-pointer hover:shadow-lg transition-all duration-300">
            <div className="relative aspect-[4/3] overflow-hidden bg-muted">
              {post.image_url ? (
                <img
                  src={post.image_url}
                  alt={post.title}
                  className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700"
                />
              ) : (
                <div className="w-full h-full flex items-center justify-center text-4xl">🍳</div>
              )}
            </div>
            <div className="p-4">
              <h3 className="font-semibold text-foreground mb-1 line-clamp-1">{post.title}</h3>
              {post.description && (
                <p className="text-sm text-muted-foreground line-clamp-2 mb-3">{post.description}</p>
              )}
              <div className="flex items-center justify-between text-xs text-muted-foreground">
                <div className="flex items-center gap-1">
                  <Star className="w-3.5 h-3.5 text-secondary fill-secondary" />
                  <span>{post.rating || 0}</span>
                  <span>({post.rating_count || 0})</span>
                </div>
                <div className="flex items-center gap-1">
                  <MessageCircle className="w-3.5 h-3.5" />
                  <span>{post.comments?.length || 0}</span>
                </div>
              </div>
            </div>
          </Card>
        </DialogTrigger>

        <DialogContent className="max-w-lg max-h-[85vh] overflow-y-auto">
          <DialogHeader className="">
            <DialogTitle>{post.title}</DialogTitle>
          </DialogHeader>
          {post.image_url && (
            <img src={post.image_url} alt="" className="rounded-xl w-full max-h-64 object-cover" />
          )}
          {post.description && <p className="text-muted-foreground">{post.description}</p>}
          {post.recipe_text && (
            <div className="bg-muted rounded-xl p-4">
              <p className="text-sm whitespace-pre-wrap">{post.recipe_text}</p>
            </div>
          )}

          {/* Rating */}
          <div>
            <p className="text-sm font-medium mb-2">Đánh giá món ăn:</p>
            <div className="flex gap-1">
              {[1, 2, 3, 4, 5].map((star) => (
                <button key={star} onClick={() => handleRate(star)}>
                  <Star
                    className={`w-6 h-6 transition-colors ${
                      star <= myRating ? 'text-secondary fill-secondary' : 'text-muted-foreground'
                    }`}
                  />
                </button>
              ))}
            </div>
          </div>

          {/* Comments */}
          <div>
            <p className="text-sm font-medium mb-3">
              Bình luận ({post.comments?.length || 0})
            </p>
            <div className="space-y-3 mb-4 max-h-48 overflow-y-auto">
              {(post.comments || []).map((c, i) => (
                <div key={i} className="bg-muted rounded-lg p-3">
                  <p className="text-xs font-medium text-primary mb-1">{c.author}</p>
                  <p className="text-sm">{c.text}</p>
                </div>
              ))}
            </div>
            <div className="flex gap-2">
              <Input
                placeholder="Viết bình luận..."
                value={comment}
                onChange={(e) => setComment(e.target.value)}
                onKeyDown={(e) => e.key === 'Enter' && handleComment()}
              />
              <Button size="icon" onClick={handleComment} disabled={!comment.trim()}>
                <Send className="w-4 h-4" />
              </Button>
            </div>
          </div>
        </DialogContent>
      </Dialog>
    </motion.div>
  );
}