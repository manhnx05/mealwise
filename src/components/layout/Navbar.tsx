import React, { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { Button } from "@/components/ui/button";
import { Sheet, SheetContent, SheetTrigger } from "@/components/ui/sheet";
import { Menu, ChefHat, X } from 'lucide-react';

const navLinks = [
  { label: 'Trang chủ', path: '/' },
  { label: 'Công thức', path: '/recipes' },
  { label: 'Tìm theo nguyên liệu', path: '/search-ingredients' },
  { label: 'Thực đơn tuần', path: '/meal-planner' },
  { label: 'Sức khỏe', path: '/healthy' },
  { label: 'Cộng đồng', path: '/community' },
  { label: 'Đã lưu', path: '/saved' },
];

export default function Navbar() {
  const location = useLocation();
  const [open, setOpen] = useState(false);

  return (
    <nav className="sticky top-0 z-50 bg-white/80 backdrop-blur-xl border-b border-black/5">
      <div className="max-w-7xl mx-auto px-4 sm:px-6">
        <div className="flex items-center justify-between h-16">
          <Link to="/" className="flex items-center gap-2.5">
            <div className="w-9 h-9 rounded-xl bg-[#2e8b57] flex items-center justify-center">
              <ChefHat className="w-5 h-5 text-white" />
            </div>
            <span className="font-display text-xl font-bold text-slate-900">CookSimple</span>
          </Link>

          <div className="hidden lg:flex items-center gap-2">
            {navLinks.map((link) => (
              <Link
                key={link.path}
                to={link.path}
                className={`px-3 py-2 rounded-lg text-sm font-medium transition-colors ${
                  location.pathname === link.path
                    ? 'bg-[#2e8b57]/10 text-[#2e8b57]'
                    : 'text-slate-500 hover:text-slate-900 hover:bg-slate-50'
                }`}
              >
                {link.label}
              </Link>
            ))}
          </div>

          <div className="hidden lg:flex items-center gap-3">
             <div className="flex items-center gap-2 px-3 py-1.5 hover:bg-slate-50 rounded-full cursor-pointer transition-colors">
               <div className="w-7 h-7 rounded-full bg-[#2e8b57] flex items-center justify-center text-xs font-bold text-white shadow-sm ring-2 ring-white">
                 M
               </div>
               <span className="text-sm font-medium text-slate-700 truncate w-24">Mạnh Nguy...</span>
             </div>
          </div>

          <Sheet open={open} onOpenChange={setOpen}>
            <SheetTrigger asChild className="lg:hidden">
              <Button variant="ghost" size="icon">
                <Menu className="w-5 h-5" />
              </Button>
            </SheetTrigger>
            <SheetContent side="right" className="w-72 p-0">
              <div className="flex flex-col p-6 gap-1">
                <div className="flex items-center gap-2 mb-6">
                  <div className="w-8 h-8 rounded-lg bg-[#2e8b57] flex items-center justify-center">
                    <ChefHat className="w-4 h-4 text-white" />
                  </div>
                  <span className="font-display text-lg font-bold text-slate-900">CookSimple</span>
                </div>
                {navLinks.map((link) => (
                  <Link
                    key={link.path}
                    to={link.path}
                    onClick={() => setOpen(false)}
                    className={`px-4 py-3 rounded-lg text-sm font-medium transition-colors ${
                      location.pathname === link.path
                        ? 'bg-[#2e8b57]/10 text-[#2e8b57]'
                        : 'text-slate-500 hover:text-slate-900 hover:bg-slate-50'
                    }`}
                  >
                    {link.label}
                  </Link>
                ))}
              </div>
            </SheetContent>
          </Sheet>
        </div>
      </div>
    </nav>
  );
}