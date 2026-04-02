import React from 'react';
import HeroSection from '../components/home/HeroSection';
import QuickRecipes from '../components/home/QuickRecipes';
import FeaturesGrid from '../components/home/FeaturesGrid';

export default function Home() {
  return (
    <div>
      <HeroSection />
      <QuickRecipes />
      <FeaturesGrid />
    </div>
  );
}