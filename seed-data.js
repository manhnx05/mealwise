import { createClient } from '@base44/sdk';

// Get app params from environment
const appId = process.env.VITE_BASE44_APP_ID || 'dummy_app_id';
const appBaseUrl = process.env.VITE_BASE44_APP_BASE_URL || 'https://dummy.base44.app';

const base44 = createClient({
  appId,
  token: null,
  functionsVersion: null,
  serverUrl: '',
  requiresAuth: false,
  appBaseUrl
});

const sampleRecipes = [
  {
    title: "Cơm chiên dương châu",
    description: "Món cơm chiên thơm ngon, đầy đủ dinh dưỡng với tôm, xúc xích và rau củ",
    image_url: "https://images.unsplash.com/photo-1603133872878-684f208fb84b?w=800",
    cook_time: 20,
    servings: 2,
    cost: 45000,
    calories: 520,
    protein: 18,
    fat: 15,
    carbs: 75,
    fiber: 3,
    category: "quick_meal",
    tags: ["cơm", "chiên", "nhanh gọn"],
    ingredients: [
      { name: "Cơm nguội", amount: "2 bát", calories: 300, cost: 10000 },
      { name: "Tôm", amount: "100g", calories: 85, cost: 15000 },
      { name: "Xúc xích", amount: "2 cái", calories: 120, cost: 10000 },
      { name: "Trứng gà", amount: "2 quả", calories: 140, cost: 8000 },
      { name: "Hành tây", amount: "1/2 củ", calories: 20, cost: 2000 }
    ],
    steps: [
      { step_number: 1, instruction: "Đập trứng, đánh tan. Phi thom hành tây." },
      { step_number: 2, instruction: "Cho tôm, xúc xích vào xào chín." },
      { step_number: 3, instruction: "Thêm cơm, trứng vào đảo đều trên lửa lớn." },
      { step_number: 4, instruction: "Nêm nếm gia vị, rắc hành lá và tắt bếp." }
    ]
  },
  {
    title: "Salad ức gà",
    description: "Món salad giàu protein, ít calo, hoàn hảo cho người tập gym",
    image_url: "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=800",
    cook_time: 15,
    servings: 1,
    cost: 35000,
    calories: 280,
    protein: 35,
    fat: 8,
    carbs: 20,
    fiber: 5,
    category: "gym",
    tags: ["salad", "gà", "healthy", "protein"],
    ingredients: [
      { name: "Ức gà", amount: "150g", calories: 165, cost: 20000 },
      { name: "Xà lách", amount: "100g", calories: 15, cost: 5000 },
      { name: "Cà chua", amount: "1 quả", calories: 20, cost: 3000 },
      { name: "Dầu olive", amount: "1 thìa", calories: 40, cost: 2000 },
      { name: "Chanh", amount: "1/2 quả", calories: 5, cost: 2000 }
    ],
    steps: [
      { step_number: 1, instruction: "Luộc ức gà với chút muối, để nguội rồi xé nhỏ." },
      { step_number: 2, instruction: "Rửa sạch rau, cắt cà chua múi cau." },
      { step_number: 3, instruction: "Trộn tất cả nguyên liệu với dầu olive và nước chanh." },
      { step_number: 4, instruction: "Nêm nếm vừa ăn và thưởng thức ngay." }
    ]
  },
  {
    title: "Phở gà",
    description: "Món phở gà thanh đạm, ít dầu mỡ, phù hợp cho người ăn kiêng",
    image_url: "https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?w=800",
    cook_time: 45,
    servings: 2,
    cost: 50000,
    calories: 380,
    protein: 25,
    fat: 8,
    carbs: 55,
    fiber: 2,
    category: "low_fat",
    tags: ["phở", "gà", "ít dầu mỡ"],
    ingredients: [
      { name: "Thịt gà", amount: "300g", calories: 330, cost: 30000 },
      { name: "Bánh phở", amount: "200g", calories: 220, cost: 8000 },
      { name: "Hành tây", amount: "1 củ", calories: 40, cost: 3000 },
      { name: "Gừng", amount: "30g", calories: 10, cost: 2000 },
      { name: "Hành lá", amount: "1 bó", calories: 10, cost: 2000 }
    ],
    steps: [
      { step_number: 1, instruction: "Luộc gà với hành, gừng đập dập khoảng 30 phút." },
      { step_number: 2, instruction: "Vớt gà ra, để nguội rồi xé thịt." },
      { step_number: 3, instruction: "Nêm nước dùng vừa ăn." },
      { step_number: 4, instruction: "Trụng bánh phở, cho vào tô, xếp thịt gà, chan nước dùng." }
    ]
  },
  {
    title: "Canh chua chay",
    description: "Món canh chua thanh mát, hoàn toàn chay, giàu vitamin",
    image_url: "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=800",
    cook_time: 25,
    servings: 3,
    cost: 30000,
    calories: 120,
    protein: 3,
    fat: 2,
    carbs: 25,
    fiber: 4,
    category: "vegetarian",
    tags: ["canh", "chay", "rau củ"],
    ingredients: [
      { name: "Cà chua", amount: "3 quả", calories: 60, cost: 9000 },
      { name: "Dứa", amount: "1/4 quả", calories: 50, cost: 8000 },
      { name: "Đậu hũ", amount: "100g", calories: 80, cost: 5000 },
      { name: "Rau muống", amount: "1 bó", calories: 20, cost: 5000 },
      { name: "Me", amount: "2 thìa", calories: 30, cost: 3000 }
    ],
    steps: [
      { step_number: 1, instruction: "Cà chua cắt múi, dứa cắt miếng vừa ăn." },
      { step_number: 2, instruction: "Đun sôi nước, cho cà chua, dứa vào nấu." },
      { step_number: 3, instruction: "Thêm đậu hũ, me, nêm nếm vừa ăn." },
      { step_number: 4, instruction: "Cho rau muống vào, đun sôi 1 phút rồi tắt bếp." }
    ]
  },
  {
    title: "Mì xào bò",
    description: "Món mì xào thơm ngon, nhanh gọn cho bữa trưa",
    image_url: "https://images.unsplash.com/photo-1612929633738-8fe44f7ec841?w=800",
    cook_time: 18,
    servings: 2,
    cost: 55000,
    calories: 480,
    protein: 22,
    fat: 18,
    carbs: 60,
    fiber: 3,
    category: "quick_meal",
    tags: ["mì", "bò", "xào"],
    ingredients: [
      { name: "Mì trứng", amount: "200g", calories: 280, cost: 12000 },
      { name: "Thịt bò", amount: "150g", calories: 180, cost: 30000 },
      { name: "Cải thảo", amount: "100g", calories: 15, cost: 5000 },
      { name: "Cà rót", amount: "1 quả", calories: 25, cost: 3000 },
      { name: "Tỏi", amount: "3 tép", calories: 15, cost: 2000 }
    ],
    steps: [
      { step_number: 1, instruction: "Luộc mì qua nước, để ráo." },
      { step_number: 2, instruction: "Phi thơm tỏi, xào thịt bò đến chín." },
      { step_number: 3, instruction: "Cho rau vào xào, thêm mì và gia vị." },
      { step_number: 4, instruction: "Đảo đều trên lửa lớn 2 phút rồi tắt bếp." }
    ]
  },
  {
    title: "Súp bí đỏ",
    description: "Món súp bí đỏ béo ngậy, giàu vitamin A, tốt cho sức khỏe",
    image_url: "https://images.unsplash.com/photo-1476718406336-bb5a9690ee2a?w=800",
    cook_time: 30,
    servings: 4,
    cost: 40000,
    calories: 180,
    protein: 4,
    fat: 8,
    carbs: 28,
    fiber: 3,
    category: "healthy",
    tags: ["súp", "bí đỏ", "healthy"],
    ingredients: [
      { name: "Bí đỏ", amount: "500g", calories: 130, cost: 20000 },
      { name: "Hành tây", amount: "1 củ", calories: 40, cost: 3000 },
      { name: "Sữa tươi", amount: "200ml", calories: 120, cost: 12000 },
      { name: "Bơ", amount: "1 thìa", calories: 100, cost: 5000 }
    ],
    steps: [
      { step_number: 1, instruction: "Bí đỏ gọt vỏ, cắt miếng, hấp chín." },
      { step_number: 2, instruction: "Phi thơm hành tây với bơ." },
      { step_number: 3, instruction: "Xay nhuyễn bí đỏ với hành tây và sữa." },
      { step_number: 4, instruction: "Đun nhỏ lửa, nêm nếm vừa ăn." }
    ]
  }
];

const sampleCommunityPosts = [
  {
    title: "Bún chả Hà Nội",
    description: "Công thức bún chả truyền thống của gia đình tôi",
    recipe_text: "Ướp thịt với nước mắm, đường, tiêu. Nướng than hoa cho thơm. Nước chấm pha chua ngọt vừa ăn.",
    image_url: "https://images.unsplash.com/photo-1559314809-0d155014e29e?w=800",
    rating: 4.8,
    rating_count: 24,
    author_name: "Minh Anh",
    comments: [
      { author: "Hương", text: "Ngon quá! Cảm ơn bạn đã chia sẻ", date: "2024-01-15" },
      { author: "Tuấn", text: "Tôi đã thử và rất thành công", date: "2024-01-16" }
    ]
  },
  {
    title: "Bánh mì chảo",
    description: "Món ăn sáng nhanh gọn, đầy đủ dinh dưỡng",
    recipe_text: "Đập trứng vào chảo, cho bánh mì vào, rắc phô mai. Đậy nắp đến khi trứng chín.",
    image_url: "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=800",
    rating: 4.5,
    rating_count: 18,
    author_name: "Thu Hà",
    comments: [
      { author: "Nam", text: "Đơn giản mà ngon!", date: "2024-01-14" }
    ]
  },
  {
    title: "Gỏi cuốn tôm thịt",
    description: "Món ăn nhẹ, healthy, dễ làm",
    recipe_text: "Luộc tôm, thịt. Chuẩn bị rau sống. Cuốn bánh tráng với tất cả nguyên liệu. Chấm nước mắm chua ngọt.",
    image_url: "https://images.unsplash.com/photo-1559847844-5315695dadae?w=800",
    rating: 4.9,
    rating_count: 32,
    author_name: "Lan Phương",
    comments: []
  }
];

async function seedData() {
  console.log('🌱 Bắt đầu seed dữ liệu...\n');

  try {
    // Seed Recipes
    console.log('📝 Đang tạo công thức nấu ăn...');
    for (const recipe of sampleRecipes) {
      try {
        await base44.entities.Recipe.create(recipe);
        console.log(`✅ Đã tạo: ${recipe.title}`);
      } catch (error) {
        console.log(`❌ Lỗi khi tạo ${recipe.title}:`, error.message);
      }
    }

    // Seed Community Posts
    console.log('\n💬 Đang tạo bài viết cộng đồng...');
    for (const post of sampleCommunityPosts) {
      try {
        await base44.entities.CommunityPost.create(post);
        console.log(`✅ Đã tạo: ${post.title}`);
      } catch (error) {
        console.log(`❌ Lỗi khi tạo ${post.title}:`, error.message);
      }
    }

    console.log('\n✨ Hoàn thành seed dữ liệu!');
    console.log(`📊 Tổng cộng: ${sampleRecipes.length} công thức và ${sampleCommunityPosts.length} bài viết`);
  } catch (error) {
    console.error('❌ Lỗi khi seed dữ liệu:', error);
  }
}

seedData();
