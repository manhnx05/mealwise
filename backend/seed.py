"""
Script seeding dữ liệu mẫu món Việt Nam vào database Neon.
Chạy: cd backend && .\venv\Scripts\python seed.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app import create_app
from app import db
from app.models import Recipe, CommunityPost, SavedRecipe

app = create_app()

RECIPES = [
  {
    "title": "Ức gà luộc xé phay",
    "description": "Món ăn kinh điển cho người tập Gym, giàu protein.",
    "cook_time": 15,
    "servings": 2,
    "cost": 40000,
    "calories": 180,
    "protein": 30,
    "fat": 4,
    "fiber": 2,
    "carbs": 5,
    "category": "Gym",
    "tags": [
      "Gym",
      "Giảm cân",
      "Ít dầu mỡ",
      "Lành mạnh"
    ],
    "image_url": "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?w=600",
    "ingredients": [
      {
        "name": "Nguyên liệu",
        "amount": "vừa đủ"
      }
    ],
    "steps": [
      {
        "step_number": 1,
        "instruction": "Nấu và thưởng thức."
      }
    ]
  },
  {
    "title": "Salad ức gà",
    "description": "Rau xanh kết hợp ức gà nướng nhanh.",
    "cook_time": 15,
    "servings": 2,
    "cost": 45000,
    "calories": 250,
    "protein": 28,
    "fat": 8,
    "fiber": 6,
    "carbs": 10,
    "category": "Giảm cân",
    "tags": [
      "Giảm cân",
      "Gym",
      "Nhanh gọn"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Salad_platter.jpg/330px-Salad_platter.jpg",
    "ingredients": [
      {
        "name": "Nguyên liệu",
        "amount": "vừa đủ"
      }
    ],
    "steps": [
      {
        "step_number": 1,
        "instruction": "Nấu và thưởng thức."
      }
    ]
  },
  {
    "title": "Thăn bò nướng măng tây",
    "description": "Nhiều đạm tạo cơ, măng tây bổ sung vitamin.",
    "cook_time": 20,
    "servings": 2,
    "cost": 90000,
    "calories": 350,
    "protein": 35,
    "fat": 15,
    "fiber": 5,
    "carbs": 8,
    "category": "Gym",
    "tags": [
      "Gym",
      "Lành mạnh"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Saigon_Pho_with_pork.jpg/330px-Saigon_Pho_with_pork.jpg",
    "ingredients": [
      {
        "name": "Nguyên liệu",
        "amount": "vừa đủ"
      }
    ],
    "steps": [
      {
        "step_number": 1,
        "instruction": "Nấu và thưởng thức."
      }
    ]
  },
  {
    "title": "Cơm gạo lứt thịt băm",
    "description": "Carb chậm giúp no lâu, giảm mỡ.",
    "cook_time": 30,
    "servings": 2,
    "cost": 35000,
    "calories": 380,
    "protein": 22,
    "fat": 10,
    "fiber": 8,
    "carbs": 45,
    "category": "Giảm cân",
    "tags": [
      "Giảm cân",
      "Gym",
      "Tiết kiệm"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Sushi_%2826478755502%29.jpg/330px-Sushi_%2826478755502%29.jpg",
    "ingredients": [
      {
        "name": "Nguyên liệu",
        "amount": "vừa đủ"
      }
    ],
    "steps": [
      {
        "step_number": 1,
        "instruction": "Nấu và thưởng thức."
      }
    ]
  },
  {
    "title": "Đậu hũ non xốt cà chua",
    "description": "Thanh đạm, ít calo, dễ tiêu.",
    "cook_time": 12,
    "servings": 3,
    "cost": 15000,
    "calories": 180,
    "protein": 12,
    "fat": 6,
    "fiber": 4,
    "carbs": 16,
    "category": "Chay",
    "tags": [
      "Chay",
      "Tiết kiệm",
      "Ít dầu mỡ",
      "Nhanh gọn"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Canhchua2.jpg/330px-Canhchua2.jpg",
    "ingredients": [
      {
        "name": "Nguyên liệu",
        "amount": "vừa đủ"
      }
    ],
    "steps": [
      {
        "step_number": 1,
        "instruction": "Nấu và thưởng thức."
      }
    ]
  },
  {
    "title": "Rau luộc kho quẹt chay",
    "description": "Kho quẹt làm từ nấm hương, ăn kèm bắp cải cà rốt luộc.",
    "cook_time": 20,
    "servings": 4,
    "cost": 25000,
    "calories": 150,
    "protein": 5,
    "fat": 2,
    "fiber": 8,
    "carbs": 25,
    "category": "Chay",
    "tags": [
      "Chay",
      "Lành mạnh",
      "Ít dầu mỡ"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Saigon_Pho_with_pork.jpg/330px-Saigon_Pho_with_pork.jpg",
    "ingredients": [
      {
        "name": "Nguyên liệu",
        "amount": "vừa đủ"
      }
    ],
    "steps": [
      {
        "step_number": 1,
        "instruction": "Nấu và thưởng thức."
      }
    ]
  },
  {
    "title": "Canh rong biển đậu non",
    "description": "Giải nhiệt, nấu trong 5 phút.",
    "cook_time": 5,
    "servings": 2,
    "cost": 20000,
    "calories": 80,
    "protein": 6,
    "fat": 1,
    "fiber": 3,
    "carbs": 10,
    "category": "Nhanh gọn",
    "tags": [
      "Nhanh gọn",
      "Chay",
      "Ít dầu mỡ"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Breakfast_at_Tamahan_Ryokan%2C_Kyoto.jpg/330px-Breakfast_at_Tamahan_Ryokan%2C_Kyoto.jpg",
    "ingredients": [
      {
        "name": "Nguyên liệu",
        "amount": "vừa đủ"
      }
    ],
    "steps": [
      {
        "step_number": 1,
        "instruction": "Nấu và thưởng thức."
      }
    ]
  },
  {
    "title": "Trứng rán ngải cứu",
    "description": "Bổ dưỡng, chi phí cực rẻ.",
    "cook_time": 10,
    "servings": 2,
    "cost": 120000,
    "calories": 210,
    "protein": 12,
    "fat": 16,
    "fiber": 2,
    "carbs": 3,
    "category": "Tiết kiệm",
    "tags": [
      "Tiết kiệm",
      "Nhanh gọn"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Cha_gio.jpg/330px-Cha_gio.jpg",
    "ingredients": [
      {
        "name": "Nguyên liệu",
        "amount": "vừa đủ"
      }
    ],
    "steps": [
      {
        "step_number": 1,
        "instruction": "Nấu và thưởng thức."
      }
    ]
  },
  {
    "title": "Mướp xào giá đỗ",
    "description": "Món rau rẻ tiền siêu nhanh.",
    "cook_time": 5,
    "servings": 3,
    "cost": 10000,
    "calories": 60,
    "protein": 3,
    "fat": 1,
    "fiber": 5,
    "carbs": 8,
    "category": "Tiết kiệm",
    "tags": [
      "Tiết kiệm",
      "Nhanh gọn",
      "Ít dầu mỡ"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Bittergourd.jpg/330px-Bittergourd.jpg",
    "ingredients": [
      {
        "name": "Nguyên liệu",
        "amount": "vừa đủ"
      }
    ],
    "steps": [
      {
        "step_number": 1,
        "instruction": "Nấu và thưởng thức."
      }
    ]
  },
  {
    "title": "Cá hồi áp chảo sa kê",
    "description": "Omega-3 cực tốt cho tim mạch.",
    "cook_time": 15,
    "servings": 2,
    "cost": 120000,
    "calories": 320,
    "protein": 25,
    "fat": 18,
    "fiber": 4,
    "carbs": 8,
    "category": "Lành mạnh",
    "tags": [
      "Lành mạnh",
      "Nhanh gọn"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Da_Lat_-_Viet_Nam.jpg/330px-Da_Lat_-_Viet_Nam.jpg",
    "ingredients": [
      {
        "name": "Nguyên liệu",
        "amount": "vừa đủ"
      }
    ],
    "steps": [
      {
        "step_number": 1,
        "instruction": "Nấu và thưởng thức."
      }
    ]
  },
  {
    "title": "Yến mạch trộn sữa chua trái cây",
    "description": "Bữa sáng hoàn hảo đốt mỡ.",
    "cook_time": 5,
    "servings": 1,
    "cost": 30000,
    "calories": 250,
    "protein": 10,
    "fat": 5,
    "fiber": 6,
    "carbs": 40,
    "category": "Giảm cân",
    "tags": [
      "Giảm cân",
      "Nhanh gọn",
      "Lành mạnh"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Baobob_tree.jpg/330px-Baobob_tree.jpg",
    "ingredients": [
      {
        "name": "Nguyên liệu",
        "amount": "vừa đủ"
      }
    ],
    "steps": [
      {
        "step_number": 1,
        "instruction": "Nấu và thưởng thức."
      }
    ]
  },
  {
    "title": "Bún bò xào xả ớt",
    "description": "Hương vị đậm đà không ngán.",
    "cook_time": 20,
    "servings": 2,
    "cost": 50000,
    "calories": 450,
    "protein": 25,
    "fat": 15,
    "fiber": 4,
    "carbs": 50,
    "category": "Gym",
    "tags": [
      "Thịt bò",
      "Nhanh gọn"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Ph%E1%BB%9F_b%C3%B2%2C_C%E1%BA%A7u_Gi%E1%BA%A5y%2C_H%C3%A0_N%E1%BB%99i.jpg/330px-Ph%E1%BB%9F_b%C3%B2%2C_C%E1%BA%A7u_Gi%E1%BA%A5y%2C_H%C3%A0_N%E1%BB%99i.jpg",
    "ingredients": [
      {
        "name": "Nguyên liệu",
        "amount": "vừa đủ"
      }
    ],
    "steps": [
      {
        "step_number": 1,
        "instruction": "Nấu và thưởng thức."
      }
    ]
  },
  {
    "title": "Canh khổ qua nhồi thịt",
    "description": "Giúp thanh lọc cơ thể.",
    "cook_time": 45,
    "servings": 4,
    "cost": 60000,
    "calories": 200,
    "protein": 18,
    "fat": 10,
    "fiber": 4,
    "carbs": 8,
    "category": "Lành mạnh",
    "tags": [
      "Lành mạnh",
      "Ít dầu mỡ"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Canh_kh%E1%BB%95_qua.JPG/330px-Canh_kh%E1%BB%95_qua.JPG",
    "ingredients": [
      {
        "name": "Nguyên liệu",
        "amount": "vừa đủ"
      }
    ],
    "steps": [
      {
        "step_number": 1,
        "instruction": "Nấu và thưởng thức."
      }
    ]
  },
  {
    "title": "Nấm tiên xào sả ớt",
    "description": "Nấm giòn sần sật chay.",
    "cook_time": 15,
    "servings": 3,
    "cost": 25000,
    "calories": 120,
    "protein": 8,
    "fat": 4,
    "fiber": 5,
    "carbs": 12,
    "category": "Chay",
    "tags": [
      "Chay",
      "Nhanh gọn"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Saigon_Pho_with_pork.jpg/330px-Saigon_Pho_with_pork.jpg",
    "ingredients": [
      {
        "name": "Nguyên liệu",
        "amount": "vừa đủ"
      }
    ],
    "steps": [
      {
        "step_number": 1,
        "instruction": "Nấu và thưởng thức."
      }
    ]
  },
  {
    "title": "Cháo yến mạch ức gà băm",
    "description": "Cháo dễ thuỷ phân nhanh, ấm bụng buổi sáng.",
    "cook_time": 10,
    "servings": 1,
    "cost": 25000,
    "calories": 280,
    "protein": 22,
    "fat": 6,
    "fiber": 7,
    "carbs": 30,
    "category": "Giảm cân",
    "tags": [
      "Giảm cân",
      "Gym",
      "Nhanh gọn"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Flaming_wok_by_KellyB_in_Bountiful%2C_Utah.jpg/330px-Flaming_wok_by_KellyB_in_Bountiful%2C_Utah.jpg",
    "ingredients": [
      {
        "name": "Nguyên liệu",
        "amount": "vừa đủ"
      }
    ],
    "steps": [
      {
        "step_number": 1,
        "instruction": "Nấu và thưởng thức."
      }
    ]
  },
  {
    "title": "Phở bò",
    "description": "Truyền thống, dùng nước hầm ngon.",
    "cook_time": 180,
    "servings": 4,
    "cost": 80000,
    "calories": 450,
    "protein": 28,
    "fat": 12,
    "fiber": 2,
    "carbs": 55,
    "category": "Tất cả",
    "tags": [
      "Bò"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Ph%E1%BB%9F_b%C3%B2%2C_C%E1%BA%A7u_Gi%E1%BA%A5y%2C_H%C3%A0_N%E1%BB%99i.jpg/330px-Ph%E1%BB%9F_b%C3%B2%2C_C%E1%BA%A7u_Gi%E1%BA%A5y%2C_H%C3%A0_N%E1%BB%99i.jpg",
    "ingredients": [
      {
        "name": "Nguyên liệu",
        "amount": "vừa đủ"
      }
    ],
    "steps": [
      {
        "step_number": 1,
        "instruction": "Nấu và thưởng thức."
      }
    ]
  },
  {
    "title": "Bún bò Huế",
    "description": "Cay nồng vị Huế.",
    "cook_time": 150,
    "servings": 4,
    "cost": 75000,
    "calories": 480,
    "protein": 30,
    "fat": 14,
    "fiber": 3,
    "carbs": 58,
    "category": "Tất cả",
    "tags": [
      "Bò"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Bun-Bo-Hue-from-Huong-Giang-2011.jpg/330px-Bun-Bo-Hue-from-Huong-Giang-2011.jpg",
    "ingredients": [
      {
        "name": "Nguyên liệu",
        "amount": "vừa đủ"
      }
    ],
    "steps": [
      {
        "step_number": 1,
        "instruction": "Nấu và thưởng thức."
      }
    ]
  },
  {
    "title": "Bánh mì Việt Nam",
    "description": "Nhanh gọn, đủ chất.",
    "cook_time": 15,
    "servings": 1,
    "cost": 25000,
    "calories": 380,
    "protein": 18,
    "fat": 16,
    "fiber": 2,
    "carbs": 42,
    "category": "Nhanh gọn",
    "tags": [
      "Nhanh gọn",
      "Tiết kiệm"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/B%C3%A1nh_m%C3%AC_th%E1%BB%8Bt_n%C6%B0%E1%BB%9Bng.png/330px-B%C3%A1nh_m%C3%AC_th%E1%BB%8Bt_n%C6%B0%E1%BB%9Bng.png",
    "ingredients": [
      {
        "name": "Nguyên liệu",
        "amount": "vừa đủ"
      }
    ],
    "steps": [
      {
        "step_number": 1,
        "instruction": "Nấu và thưởng thức."
      }
    ]
  },
  {
    "title": "Gỏi cuốn",
    "description": "Bánh tráng cuộn tôm thịt tươi mát không dầu ăn.",
    "cook_time": 30,
    "servings": 4,
    "cost": 50000,
    "calories": 180,
    "protein": 14,
    "fat": 4,
    "fiber": 3,
    "carbs": 25,
    "category": "Lành mạnh",
    "tags": [
      "Lành mạnh",
      "Ít dầu mỡ",
      "Giảm cân"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Summer_roll.jpg/330px-Summer_roll.jpg",
    "ingredients": [
      {
        "name": "Nguyên liệu",
        "amount": "vừa đủ"
      }
    ],
    "steps": [
      {
        "step_number": 1,
        "instruction": "Nấu và thưởng thức."
      }
    ]
  },
  {
    "title": "Rau muống xào tỏi",
    "description": "Quen thuộc của mọi gia đình.",
    "cook_time": 10,
    "servings": 2,
    "cost": 15000,
    "calories": 80,
    "protein": 4,
    "fat": 6,
    "fiber": 3,
    "carbs": 8,
    "category": "Tiết kiệm",
    "tags": [
      "Tiết kiệm",
      "Nhanh gọn",
      "Chay"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Ipomoea_aquatica_%282%29.JPG/330px-Ipomoea_aquatica_%282%29.JPG",
    "ingredients": [
      {
        "name": "Nguyên liệu",
        "amount": "vừa đủ"
      }
    ],
    "steps": [
      {
        "step_number": 1,
        "instruction": "Nấu và thưởng thức."
      }
    ]
  }
]

COMMUNITY_POSTS = [
  {
    "title": "Bữa ăn 15k sinh viên cuối tháng",
    "description": "Không cần tốn nhiều tiền, chỉ với 15k là có ngay món ăn ngon miệng sạch sẽ!",
    "author_name": "Tuấn Kiệt",
    "rating": 4.8,
    "rating_count": 129,
    "image_url": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=600",
    "recipe_text": "Tất nhiên là đậu phụ xào sả ớt rồi. Các bạn mua 5k tiền đậu..."
  },
  {
    "title": "Kinh nghiệm giảm 3kg trong 1 tháng",
    "description": "Mình chỉ ăn theo thực đơn trên web này và bỏ cơm trắng. Mọi người tham khảo nhé.",
    "author_name": "Cô ba Gym",
    "rating": 5.0,
    "rating_count": 532,
    "image_url": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=600",
    "recipe_text": "Bí quyết là ăn ức gà luộc, salad..."
  },
  {
    "title": "Mâm cơm chay cúng rằm mùng 1 đầy đủ ý nghĩa",
    "description": "Nấu 4 món chay siêu nhanh nhờ sắp xếp thông minh.",
    "author_name": "Hương Sen",
    "rating": 4.9,
    "rating_count": 80,
    "image_url": "https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=600",
    "recipe_text": "Món 1 là nấm xào..."
  }
]

def seed():
    with app.app_context():
        # Clear old rows
        SavedRecipe.query.delete()
        Recipe.query.delete()
        CommunityPost.query.delete()
        db.session.commit()

        created_recipes = []
        for data in RECIPES:
            recipe = Recipe(
                title=data["title"],
                description=data["description"],
                image_url=data.get("image_url"),
                cook_time=data.get("cook_time"),
                servings=data.get("servings"),
                cost=data.get("cost"),
                calories=data.get("calories"),
                protein=data.get("protein"),
                fat=data.get("fat"),
                fiber=data.get("fiber"),
                carbs=data.get("carbs"),
                category=data.get("category"),
                ingredients=data.get("ingredients", []),
                steps=data.get("steps", []),
                tags=data.get("tags", []),
            )
            created_recipes.append(recipe)
            db.session.add(recipe)

        for post_data in COMMUNITY_POSTS:
            post = CommunityPost(**post_data)
            db.session.add(post)

        db.session.flush() # flush to get recipe IDs
        
        # Save top 5 recipes
        for i in range(min(5, len(created_recipes))):
            sr = SavedRecipe(recipe_id=created_recipes[i].id)
            db.session.add(sr)

        db.session.commit()
        print("Success! Seeded recipes, posts, and saved recipes.")

if __name__ == "__main__":
    seed()
