import os, sys, random, urllib.parse
sys.path.insert(0, os.path.dirname(__file__))

from app import create_app, db
from app.models import Recipe, CommunityPost

app = create_app()

IMAGE_MAP = {
    "Phở": "https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?w=600",
    "Bún bò": "https://images.unsplash.com/photo-1598514982205-f36b96d1e8d4?w=600",
    "Bánh mì": "https://images.unsplash.com/photo-1600803907087-f56d462fd26b?w=600",
    "Bún chả": "https://images.unsplash.com/photo-1569050467447-ce54b3bbc37d?w=600",
    "Nem rán": "https://images.unsplash.com/photo-1562802378-063ec186a863?w=600",
    "Chả giò": "https://images.unsplash.com/photo-1562802378-063ec186a863?w=600",
    "Cơm tấm": "https://images.unsplash.com/photo-1598514983318-2f64f8f4796c?w=600",
    "Cơm chiên": "https://images.unsplash.com/photo-1536304993881-ff6e9eefa2a6?w=600",
    "Cháo": "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=600",
    "Canh": "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=600",
    "Lẩu": "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=600",
    "Salad": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=600",
    "Gỏi": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=600",
    "Thịt kho": "https://images.unsplash.com/photo-1534482421-64566f976cfa?w=600",
    "Cá kho": "https://images.unsplash.com/photo-1565299585323-38d6b0865b47?w=600",
    "Chè": "https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=600",
    "Sinh tố": "https://images.unsplash.com/photo-1550258987-190a2d41a8ba?w=600"
}

def get_image_for(title):
    for key, url in IMAGE_MAP.items():
        if key.lower() in title.lower():
            return url
    encoded = urllib.parse.quote(title)
    return f"https://placehold.co/600x400/2e8b57/FFFFFF/png?text={encoded}"

BASE_RECIPES = [
    ("Phở bò Hà Nội", "Phở bò truyền thống, nước dùng thanh ngọt", "Bữa sáng", ["Bò", "Phở"]),
    ("Bún bò Huế", "Bún bò cay nồng đặc trưng miền Trung", "Bữa sáng", ["Bò", "Bún", "Cay"]),
    ("Bánh mì thịt nướng", "Bánh mì Sài Gòn giòn rụm nhân thịt nướng", "Bữa sáng", ["Bánh mì", "Thịt heo"]),
    ("Cơm tấm sườn bì chả", "Cơm tấm đặc sản Sài Gòn", "Bữa trưa", ["Cơm", "Sườn"]),
    ("Bún chả Hà Nội", "Bún chả thịt nướng than hoa", "Bữa trưa", ["Bún", "Thịt nướng"]),
    ("Cá kho tộ", "Cá kho tộ đậm đà miền Tây", "Bữa tối", ["Cá", "Kho"]),
    ("Thịt kho hột vịt", "Thịt kho tàu ngày Tết", "Bữa tối", ["Thịt", "Kho"]),
    ("Canh chua cá lóc", "Canh chua thanh mát", "Canh", ["Canh", "Cá", "Chua"]),
    ("Gỏi cuốn tôm thịt", "Gỏi cuốn thanh mát kèm tương đen", "Khai vị", ["Gỏi", "Tôm", "Healthy"]),
    ("Mì Quảng tôm thịt", "Mì Quảng đậm đà đặc sản Quảng Nam", "Bữa trưa", ["Mì", "Tôm", "Thịt"]),
    ("Bánh xèo miền Tây", "Bánh xèo giòn rụm nhân tôm thịt", "Bữa tối", ["Bánh xèo", "Tôm"]),
    ("Chả giò tôm thịt", "Chả giò chiên giòn", "Khai vị", ["Chả giò", "Chiên"]),
    ("Bò lúc lắc", "Bò lúc lắc xào bơ tỏi", "Bữa tối", ["Bò", "Xào"]),
    ("Lẩu thái hải sản", "Lẩu Thái chua cay hải sản", "Lẩu", ["Lẩu", "Hải sản", "Cay"]),
    ("Chè đậu đỏ", "Chè đậu đỏ ngọt thanh", "Tráng miệng", ["Chè", "Ngọt"]),
]

PROTEINS = ["Thịt bò", "Thịt heo", "Thịt gà", "Tôm", "Mực", "Cá", "Đậu hũ"]
METHODS = ["Xào", "Nướng", "Kho", "Hấp", "Chiên", "Luộc", "Sốt chua ngọt"]
VEGGIES = ["Rau muống", "Bông cải", "Cà chua", "Dưa leo", "Hành tây", "Nấm", "Rau bina"]

all_recipes = []

# Generate specific recipes
for title, desc, cat, tags in BASE_RECIPES:
    cost = random.randint(3, 10) * 10000
    all_recipes.append({
        "title": title,
        "description": desc,
        "image_url": get_image_for(title),
        "cook_time": random.randint(15, 60),
        "servings": random.randint(1, 4),
        "cost": cost,
        "calories": random.randint(200, 600),
        "protein": random.randint(10, 40),
        "fat": random.randint(5, 20),
        "fiber": random.randint(1, 10),
        "carbs": random.randint(20, 80),
        "category": cat,
        "tags": tags,
        "ingredients": [{"name": tags[0], "amount": "200g"}],
        "steps": [{"step_number": 1, "instruction": "Chuẩn bị nguyên liệu và nấu ăn."}]
    })

# Add generated recipes to reach ~100
for i in range(120):
    p = random.choice(PROTEINS)
    m = random.choice(METHODS)
    v = random.choice(VEGGIES)
    cat = random.choice(["Bữa trưa", "Bữa tối", "Bữa sáng", "Healthy", "Chay" if p == "Đậu hũ" else "Bữa chính"])
    title = f"{p} {m.lower()} {v.lower()}"
    cost = random.randint(20, 150) * 1000
    all_recipes.append({
        "title": title,
        "description": f"Món {title.lower()} thơm ngon hấp dẫn, phù hợp cho bữa ăn gia đình. Dễ làm và tiết kiệm thời gian.",
        "image_url": get_image_for(title),
        "cook_time": random.randint(10, 45),
        "servings": random.randint(2, 6),
        "cost": cost,
        "calories": random.randint(150, 700),
        "protein": random.randint(10, 60),
        "fat": random.randint(5, 30),
        "fiber": random.randint(2, 12),
        "carbs": random.randint(10, 60),
        "category": cat,
        "tags": [p, m, v],
        "ingredients": [
            {"name": p, "amount": f"{random.randint(100, 400)}g"},
            {"name": v, "amount": f"{random.randint(100, 300)}g"}
        ],
        "steps": [
            {"step_number": 1, "instruction": f"Sơ chế {p.lower()} và {v.lower()}."},
            {"step_number": 2, "instruction": f"Bắt đầu {m.lower()} với lửa vừa đến khi chín."},
            {"step_number": 3, "instruction": "Trình bày ra đĩa và thưởng thức."}
        ]
    })

def run_seed():
    with app.app_context():
        Recipe.query.delete()
        CommunityPost.query.delete()
        db.session.commit()
        
        for idx, recipe_data in enumerate(all_recipes):
            r = Recipe(**recipe_data)
            db.session.add(r)
        db.session.commit()
        
        post = CommunityPost(
            title="Thực đơn gia đình 100 món",
            description="Mình vừa cập nhật hơn 100 món ăn ngon với hình ảnh đúng thực tế, mọi người tham khảo nhé!",
            author_name="Admin",
            rating=5.0,
            rating_count=999,
            image_url="https://images.unsplash.com/photo-1598514983318-2f64f8f4796c?w=600",
            recipe_text="Nấu ăn theo thực đơn siêu mượt..."
        )
        db.session.add(post)
        db.session.commit()
        print(f"✅ Đã thêm thành công {len(all_recipes)} công thức vào DB.")

if __name__ == '__main__':
    run_seed()
