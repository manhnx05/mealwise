import React from 'react';
import { ChefHat, Heart } from 'lucide-react';

export default function Footer() {
  return (
    <footer className="bg-card border-t border-border mt-auto">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 py-10">
        <div className="flex flex-col md:flex-row items-center justify-between gap-4">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 rounded-lg bg-primary flex items-center justify-center">
              <ChefHat className="w-4 h-4 text-primary-foreground" />
            </div>
            <span className="font-display text-lg font-bold">CookSimple</span>
          </div>
          <p className="text-sm text-muted-foreground flex items-center gap-1">
            Nấu ăn đơn giản mỗi ngày <Heart className="w-3.5 h-3.5 text-destructive fill-destructive" />
          </p>
          <p className="text-xs text-muted-foreground">© 2026 WEB COOKSIMPLE</p>
        </div>
      </div>
    </footer>
  );
}