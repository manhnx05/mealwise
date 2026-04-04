import fs from 'fs';
import path from 'path';

// Thư viện nguyên liệu và chế biến để ghép ngẫu nhiên
const proteins = ['Thịt Bò', 'Thịt Heo', 'Thịt Gà', 'Tôm', 'Mực', 'Cá Lóc', 'Cá Hồi', 'Đậu Hũ', 'Sườn Non'];
const veggies = ['Rau Muống', 'Măng Tây', 'Bông Cải Xanh', 'Cà Rốt', 'Hành Tây', 'Nấm Kim Châm', 'Rau Cải', 'Ớt Chuông'];
const methods = ['Xào', 'Nướng', 'Hấp', 'Chiên', 'Kho', 'Trộn Salad'];
const baseIngredients = ['Nước mắm', 'Tiêu', 'Đường', 'Bột nọt', 'Hành tím', 'Tỏi'];

const verbs = ['Ăn kèm cơm', 'Phù hợp ăn kiêng', 'Dành cho bữa tối', 'Tuyệt vời cho mùa mưa', 'Nhanh gọn lẹ', 'Đậm đà hương vị'];

const getRandomInt = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min;
const getRandomItem = (arr) => arr[Math.floor(Math.random() * arr.length)];
const generateId = () => Math.random().toString(36).substring(2, 11);

// Ảnh ngẫu nhiên về ẩm thực để demo (Một số link từ unsplash)
const images = [
  'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=600&auto=format&fit=crop', // Salad, healthy
  'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=600&auto=format&fit=crop', // Thịt nướng, BBQ
  'https://images.unsplash.com/photo-1563379926898-05f4575a401b?w=600&auto=format&fit=crop', // Món canh
  'https://images.unsplash.com/photo-1525351484163-7529414344d8?w=600&auto=format&fit=crop', // Trứng, sáng
  'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=600&auto=format&fit=crop', // Diet
  'https://images.unsplash.com/photo-1512058564366-18510be2db19?w=600&auto=format&fit=crop', // Steak
  'https://images.unsplash.com/photo-1534080564583-6be75777b70a?w=600&auto=format&fit=crop', // Cơm
  'https://images.unsplash.com/photo-1588166524941-3bf61a9c41db?w=600&auto=format&fit=crop', // Sushi
  'https://images.unsplash.com/photo-1569058242253-1cdfcc36c57f?w=600&auto=format&fit=crop', // Mì
];

const categories = ['quick_meal', 'budget', 'healthy', 'low_fat', 'weight_loss', 'gym', 'vegetarian'];

const generateRecipes = (count) => {
  const recipes = [];
  for (let i = 0; i < count; i++) {
    const protein = getRandomItem(proteins);
    const method = getRandomItem(methods);
    const veggie = getRandomItem(veggies);
    const title = `${protein} ${method} ${veggie}`;
    const cost = getRandomInt(30, 200) * 1000;
    const calories = getRandomInt(200, 800);
    const cook_time = getRandomInt(10, 60);

    // Quyết định danh mục
    let category = getRandomItem(categories);
    if (protein === 'Đậu Hũ') category = 'vegetarian';
    if (calories < 300) category = 'low_fat';
    if (cook_time <= 15) category = 'quick_meal';

    const ingredients = [
      { name: protein, amount: `${getRandomInt(200, 500)}g`, calories: getRandomInt(100, 400), cost: cost * 0.6 },
      { name: veggie, amount: `${getRandomInt(100, 300)}g`, calories: getRandomInt(20, 100), cost: cost * 0.2 },
      { name: getRandomItem(baseIngredients), amount: '1 muỗng', calories: 10, cost: 5000 }
    ];

    const steps = [
      { step_number: 1, instruction: `Sơ chế sạch sẽ ${protein} và ${veggie}. Cắt miếng vừa ăn.` },
      { step_number: 2, instruction: `Bắc chảo lên bếp, phi thơm hành tỏi. Cho ${protein} vào ${method} trước.` },
      { step_number: 3, instruction: `Thêm ${veggie} vào, nêm nếm gia vị vừa ăn. Sẵn sàng thưởng thức!` }
    ];

    recipes.push({
      id: generateId(),
      title,
      description: `Món ${title.toLowerCase()} vô cùng ${getRandomItem(verbs).toLowerCase()}. Mọi người cùng thử nhé!`,
      image_url: getRandomItem(images),
      cook_time,
      servings: getRandomInt(1, 6),
      cost,
      calories,
      protein: getRandomInt(10, 100),
      fat: getRandomInt(5, 50),
      carbs: getRandomInt(5, 50),
      fiber: getRandomInt(0, 20),
      category,
      ingredients,
      steps,
      created_date: new Date(Date.now() - getRandomInt(0, 30) * 86400000).toISOString()
    });
  }

  // Sắp xếp theo ngày giảm dần
  recipes.sort((a, b) => new Date(b.created_date) - new Date(a.created_date));

  return recipes;
};

// Generate 120 recipes
const recipes = generateRecipes(120);

// Write to raw file
const outputPath = path.resolve('./src/data/recipes.json');
fs.writeFileSync(outputPath, JSON.stringify(recipes, null, 2), 'utf-8');
console.log(`Generated ${recipes.length} recipes and saved to ${outputPath}`);
