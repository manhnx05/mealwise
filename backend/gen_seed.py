import requests, urllib.parse, json

recipes = [
    {
        "title":"Ức gà luộc xé phay",
        "description":"Món ăn kinh điển cho người tập Gym, giàu protein.",
        "cook_time":15,"servings":2,"cost":40000,"calories":180,"protein":30,"fat":4,"fiber":2,"carbs":5,"category":"Gym","tags":["Gym", "Giảm cân", "Ít dầu mỡ", "Lành mạnh"],
        "ingredients": [
            {"name": "Ức gà", "amount": "300g"},
            {"name": "Gừng", "amount": "1 củ nhỏ"},
            {"name": "Hành lá", "amount": "2 nhánh"},
            {"name": "Muối", "amount": "1 muỗng cafe"}
        ],
        "steps": [
            {"step_number": 1, "instruction": "Ức gà rửa sạch, sát muối mỏng để khử mùi."},
            {"step_number": 2, "instruction": "Cho ức gà vào nồi nước lạnh, thêm gừng thái lát và hành lá, luộc chín trong 12 phút."},
            {"step_number": 3, "instruction": "Vớt ức gà ra ngâm vào thố nước đá để thịt săn lại."},
            {"step_number": 4, "instruction": "Dùng tay xé phay thịt gà thành sợi vừa ăn. Thưởng thức với muối tiêu chanh."}
        ]
    },
    {
        "title":"Salad ức gà",
        "description":"Rau xanh kết hợp ức gà nướng nhanh.",
        "cook_time":15,"servings":2,"cost":45000,"calories":250,"protein":28,"fat":8,"fiber":6,"carbs":10,"category":"Giảm cân","tags":["Giảm cân", "Gym", "Nhanh gọn"],
        "ingredients": [
            {"name": "Xà lách", "amount": "200g"},
            {"name": "Ức gà", "amount": "200g"},
            {"name": "Cà chua bi", "amount": "100g"},
            {"name": "Dầu olive", "amount": "1 muỗng canh"},
            {"name": "Sốt mè rang", "amount": "2 muỗng canh"}
        ],
        "steps": [
            {"step_number": 1, "instruction": "Ức gà ướp chút muối tiêu, áp chảo với dầu olive mỗi mặt 3 phút cho chín vàng."},
            {"step_number": 2, "instruction": "Rửa sạch xà lách, ngắt khúc vừa ăn. Cà chua bi cắt đôi."},
            {"step_number": 3, "instruction": "Ức gà nguội bớt, thái lát mỏng."},
            {"step_number": 4, "instruction": "Trộn đều xà lách, cà chua, gà và rưới nước xốt mè rang lên trên."}
        ]
    },
    {
        "title":"Thăn bò nướng măng tây",
        "description":"Nhiều đạm tạo cơ, măng tây bổ sung vitamin.","cook_time":20,"servings":2,"cost":90000,"calories":350,"protein":35,"fat":15,"fiber":5,"carbs":8,"category":"Gym","tags":["Gym", "Lành mạnh"],
        "ingredients": [
            {"name": "Thịt thăn bò", "amount": "300g"},
            {"name": "Măng tây", "amount": "200g"},
            {"name": "Tỏi", "amount": "3 tép"},
            {"name": "Bơ lạt", "amount": "10g"},
            {"name": "Tiêu đen hạt", "amount": "1 muỗng cafe"}
        ],
        "steps": [
            {"step_number": 1, "instruction": "Bò ướp với muối, tiêu xay nghiền và tỏi băm. Cắt bỏ rễ già của măng tây."},
            {"step_number": 2, "instruction": "Làm nóng chảo, cho bơ vào đun chảy. Cho thăn bò vào áp chảo, mỗi mặt 2-3 phút cho chín vừa (Medium rare)."},
            {"step_number": 3, "instruction": "Lấy thịt bò ra để nghỉ 5 phút. Dùng chảo đó xào nhanh măng tây tỏi thơm trong 3 phút."},
            {"step_number": 4, "instruction": "Thái lát thịt bò dọn dùng kèm măng tây xào."}
        ]
    },
    {
        "title":"Cơm gạo lứt thịt băm",
        "description":"Carb chậm giúp no lâu, giảm mỡ.","cook_time":30,"servings":2,"cost":35000,"calories":380,"protein":22,"fat":10,"fiber":8,"carbs":45,"category":"Giảm cân","tags":["Giảm cân", "Gym", "Tiết kiệm"],
        "ingredients": [
            {"name": "Gạo lứt đỏ", "amount": "100g"},
            {"name": "Thịt heo nạc băm", "amount": "150g"},
            {"name": "Cà rốt băm", "amount": "50g"},
            {"name": "Hành lá", "amount": "2 nhánh"}
        ],
        "steps": [
            {"step_number": 1, "instruction": "Ngâm gạo lứt 2 tiếng trước khi nấu. Nấu chín thành cơm gạo lứt tơi xốp."},
            {"step_number": 2, "instruction": "Làm nóng 1 chút xíu dầu ăn, phi thơm hành lá."},
            {"step_number": 3, "instruction": "Cho thịt nạc băm và cà rốt vào đảo xém vàng, nêm chút hạt nêm và tiêu rí."},
            {"step_number": 4, "instruction": "Xúc cơm dọn ra bát, rưới thịt băm xào lên ăn nóng."}
        ]
    },
    {
        "title":"Đậu hũ non xốt cà chua",
        "description":"Thanh đạm, ít calo, dễ tiêu.","cook_time":12,"servings":3,"cost":15000,"calories":180,"protein":12,"fat":6,"fiber":4,"carbs":16,"category":"Chay","tags":["Chay", "Tiết kiệm", "Ít dầu mỡ", "Nhanh gọn"],
        "ingredients": [
            {"name": "Đậu hũ non", "amount": "2 hộp"},
            {"name": "Cà chua", "amount": "3 quả"},
            {"name": "Hành ngò", "amount": "1 mớ"},
            {"name": "Nước tương", "amount": "1 muỗng canh"}
        ],
        "steps": [
            {"step_number": 1, "instruction": "Đậu hũ non lấy ra khỏi hộp, cắt miếng vuông vuông."},
            {"step_number": 2, "instruction": "Cà chua khía chữ thập, luộc lột trần vỏ tước vứt đi, thái hạt lựu băm nhỏ."},
            {"step_number": 3, "instruction": "Đun nóng dầu ăn rắc hành phi, đổ vụn cà chua xào thành xốt đặc mịn. Nêm nước tương bột ngọt."},
            {"step_number": 4, "instruction": "Thả đậu non vào đun riu riu 3 phút cho thấm. Rắc hành ngò thái nhỏ lên."}
        ]
    },
    {
        "title":"Rau luộc kho quẹt chay",
        "description":"Kho quẹt làm từ nấm hương, ăn kèm bắp cải cà rốt luộc.",
        "cook_time":20,"servings":4,"cost":25000,"calories":150,"protein":5,"fat":2,"fiber":8,"carbs":25,"category":"Chay","tags":["Chay", "Lành mạnh", "Ít dầu mỡ"],
        "ingredients": [
            {"name": "Nấm hương khô", "amount": "50g"},
            {"name": "Đậu phộng rang", "amount": "30g"},
            {"name": "Rau bắp cải", "amount": "1/2 cái"},
            {"name": "Cà rốt", "amount": "1 củ"},
            {"name": "Xì dầu", "amount": "Tùy ý"}
        ],
        "steps": [
            {"step_number": 1, "instruction": "Rau bắp cải thái miếng vuông, cà rốt thái dọc khúc. Luộc chần với xíu muối."},
            {"step_number": 2, "instruction": "Nấm hương ngâm nở, xả kiệt nước rồi băm vụn nhuyễn."},
            {"step_number": 3, "instruction": "Phi dầu, cho nấm băm vào đảo cho khô xém, thêm xì dầu, đường thốt nốt đun sền sệt kẹo lại."},
            {"step_number": 4, "instruction": "Trộn thêm đậu phộng rang giã rối. Cạn nước sốt là thu được kho quẹt siêu keo chấm rau luộc."}
        ]
    },
    {
        "title":"Trứng rán ngải cứu",
        "description":"Bổ dưỡng, chi phí cực rẻ.",
        "cook_time":10,"servings":2,"cost":120000,"calories":210,"protein":12,"fat":16,"fiber":2,"carbs":3,"category":"Tiết kiệm","tags":["Tiết kiệm", "Nhanh gọn"],
        "ingredients": [
            {"name": "Trứng gà", "amount": "3 quả"},
            {"name": "Rau ngải cứu", "amount": "1 nắm lớn"},
            {"name": "Dầu ăn", "amount": "2 muỗng canh"},
            {"name": "Nước mắm", "amount": "1 muỗng cafe"}
        ],
        "steps": [
            {"step_number": 1, "instruction": "Ngải cứu lặt lá non, thái thật vụn cho tơi."},
            {"step_number": 2, "instruction": "Trứng gà đập tan ra bát, đổ ngải cứu vào, nêm thìa nhỏ nước mắm, đánh tung bọt."},
            {"step_number": 3, "instruction": "Đun nóng chảo dầu sôi già."},
            {"step_number": 4, "instruction": "Thả trứng ngải vào tráng đều, lật mặt khi ngửi thấy mùi thơm. Không đun quá lâu làm khô trứng."}
        ]
    },
    {
        "title":"Mướp xào giá đỗ",
        "description":"Món rau rẻ tiền siêu nhanh.",
        "cook_time":5,"servings":3,"cost":10000,"calories":60,"protein":3,"fat":1,"fiber":5,"carbs":8,"category":"Tiết kiệm","tags":["Tiết kiệm", "Nhanh gọn", "Ít dầu mỡ"],
        "ingredients": [
            {"name": "Mướp hương", "amount": "2 trái"},
            {"name": "Giá đỗ xanh", "amount": "200g"},
            {"name": "Tỏi lột vảy", "amount": "4 tép"}
        ],
        "steps": [
            {"step_number": 1, "instruction": "Mướp nạo bỏ vỏ xanh, thái xéo vát chanh dày cỡ nửa lóng tay."},
            {"step_number": 2, "instruction": "Dập tỏi, phi thơm trên chảo bằng dầu lửa lớn."},
            {"step_number": 3, "instruction": "Trút mướp thái miếng vào xào lướt 2 phút cho tái."},
            {"step_number": 4, "instruction": "Bỏ ngay giá đỗ vào xào nhanh tắt lửa luôn, nêm nếm gia vị ngay thì giá sẽ giòn ngọt mọng nước."}
        ]
    },
    {
        "title":"Cá hồi áp chảo sa kê",
        "description":"Omega-3 cực tốt cho tim mạch.",
        "cook_time":15,"servings":2,"cost":120000,"calories":320,"protein":25,"fat":18,"fiber":4,"carbs":8,"category":"Lành mạnh","tags":["Lành mạnh", "Nhanh gọn"],
        "ingredients": [
            {"name": "Nguyên miến cá hồi", "amount": "250g"},
            {"name": "Muối tiêu", "amount": "1 nhúm"},
            {"name": "Sake hoặc Vang trắng", "amount": "1 chén nhỏ"},
            {"name": "Bơ", "amount": "1 lát"}
        ],
        "steps": [
            {"step_number": 1, "instruction": "Cá hồi thấm khô bằng giấy bếp dính sạch rỉ nước, xát viền muối tiêu quanh thân."},
            {"step_number": 2, "instruction": "Áp chảo cá từ phần mặt da xuống dưới đun ở lửa nhỏ vừa cho da cá hồi chảy mỡ ra."},
            {"step_number": 3, "instruction": "Lật miếng cá khi mặt da đã giòn, thêm bơ lạt đun và rót chén rượu sake vào chảo để lấy vị."},
            {"step_number": 4, "instruction": "Cá chín tới tái hồng là gắp ra dùng nóng, đổ lớp sauce từ bơ rượu lên trên miến cá."}
        ]
    },
    {
        "title":"Bún bò Huế",
        "description":"Cay nồng vị Huế.",
        "cook_time":150,"servings":4,"cost":75000,"calories":480,"protein":30,"fat":14,"fiber":3,"carbs":58,"category":"Tất cả","tags":["Bò"],
        "ingredients": [
            {"name": "Bún sợi lớn", "amount": "500g"},
            {"name": "Thịt bò nạm", "amount": "200g"},
            {"name": "Giò heo", "amount": "4 khoanh"},
            {"name": "Sả cây", "amount": "5 cây"},
            {"name": "Mắm ruốc", "amount": "2 muỗng"}
        ],
        "steps": [
            {"step_number": 1, "instruction": "Hầm xương ống, giò heo, sả đập dập và dứa dập cho ngọt nước."},
            {"step_number": 2, "instruction": "Mắm ruốc khuấy nước để lóng cặn, chắt phần nước cốt ruốc trong vào nồi để lấy mùi thơm đầm."},
            {"step_number": 3, "instruction": "Phi điều màu đỏ thêm sả băm ớt băm mỡ tạo váng màu."},
            {"step_number": 4, "instruction": "Chan nước dùng vào bát bún sợi lớn đã chần, bỏ giò heo, nạm bò thái lát và hành tây."}
        ]
    },
    {
        "title":"Bánh mì Việt Nam",
        "description":"Nhanh gọn, đủ chất.",
        "cook_time":15,"servings":1,"cost":25000,"calories":380,"protein":18,"fat":16,"fiber":2,"carbs":42,"category":"Nhanh gọn","tags":["Nhanh gọn", "Tiết kiệm"],
        "ingredients": [
            {"name": "Ổ bánh mì đặc ruột", "amount": "1 cái"},
            {"name": "Pate gan heo", "amount": "2 muỗng"},
            {"name": "Thịt jambon đỏ/chả lụa", "amount": "4 lát"},
            {"name": "Dưa góp chua ngọt/rau mùi", "amount": "tùy thích"}
        ],
        "steps": [
            {"step_number": 1, "instruction": "Làm nóng áp chảo cho vỏ bánh mì nở phồng ròn rụm."},
            {"step_number": 2, "instruction": "Rạch dọc ổ bánh mỳ, quết dầy pate gan ở mặt trong đáy, rưới xì dầu/sốt cho đậm."},
            {"step_number": 3, "instruction": "Xếp dưa loong boong jambon chả lụa dàn đều theo thân bánh."},
            {"step_number": 4, "instruction": "Nhồi dưa chua, ngò rí, chan chút tương ớt Bắc và bóp kín hai mép."}
        ]
    },
    {
        "title":"Phở bò",
        "description":"Truyền thống, dùng nước hầm ngon.",
        "cook_time":180,"servings":4,"cost":80000,"calories":450,"protein":28,"fat":12,"fiber":2,"carbs":55,"category":"Tất cả","tags":["Bò"],
        "ingredients": [
            {"name": "Bánh phở mềm", "amount": "600g"},
            {"name": "Bò tái, nạm, gầu", "amount": "400g"},
            {"name": "Xương ống bò", "amount": "1kg"},
            {"name": "Gói gia vị thảo quả, hồi quế", "amount": "1 gói"},
            {"name": "Hành gừng nướng", "amount": "Nhiều"}
        ],
        "steps": [
            {"step_number": 1, "instruction": "Xương gáy bò ngâm muối luộc sơ đổ cặn. Rửa lại xương sạch tinh."},
            {"step_number": 2, "instruction": "Nướng đen gừng nguyên vỏ, hành củ, bóc lấy phần thịt thơm nhét vào hầm cùng xương cùng với gia vị phở rang khô trong 3 tiếng."},
            {"step_number": 3, "instruction": "Chần nước trong xương pha thêm nước nắm dặm. Thái mỏng bò tái xoa đi xoa lại."},
            {"step_number": 4, "instruction": "Xếp phở, chần bò đổ bát to chan nước đang sôi chảo vào là lên váng nhạt."}
        ]
    }
]

community_posts = [
  {"title":"Bữa ăn 15k sinh viên cuối tháng","description":"Không cần tốn nhiều tiền, chỉ với 15k là có ngay món ăn ngon miệng sạch sẽ!","author_name":"Tuấn Kiệt","rating":4.8,"rating_count":129,"image_url":"https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=600","recipe_text":"Tất nhiên là đậu phụ xào sả ớt rồi. Các bạn mua 5k tiền đậu non, 2k sả, mắm đường có sẵn. Làm tơi xả băm phi lên cho đậu nát vào đảo cho cháy xém đáy nồi là hao 3 bát cơm!"},
  {"title":"Kinh nghiệm giảm 3kg trong 1 tháng","description":"Mình chỉ ăn theo thực đơn trên web này và bỏ cơm trắng. Mọi người tham khảo nhé.","author_name":"Cô ba Gym","rating":5.0,"rating_count":532,"image_url":"https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=600","recipe_text":"Bí quyết là ăn ức gà luộc, salad 5 ngày mỗi tuần. Cứ xé phay gà luộc với bắp xú trộn dầu dấm và giấm táo, bảo đảm eo thu gọn lỳ luôn!"},
  {"title":"Mâm cơm chay cúng rằm mùng 1 đầy đủ ý nghĩa","description":"Nấu 4 món chay siêu nhanh nhờ sắp xếp thông minh.","author_name":"Hương Sen","rating":4.9,"rating_count":80,"image_url":"https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=600","recipe_text":"Món 1 là nấm đùi gà kho quẹt xì phở. Món 2 là canh rau dền loang lính. Bạn luộc nấm sau đó tận dụng nước chần để luộc rau nhé. Trắng sạch lại ngon mâm đầy."}
]

fallback_unsplashes = {
    "gà": "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?w=600",
    "bò": "https://images.unsplash.com/photo-1529692236671-f1f6cf9683ba?w=600",
    "rau": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=600",
    "đậu": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=600",
    "trứng": "https://images.unsplash.com/photo-1525385133512-2f3bdd039054?w=600",
    "cá": "https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?w=600",
    "yến mạch": "https://images.unsplash.com/photo-1517673132405-a56a62b18caf?w=600"
}

headers = {'User-Agent': 'MealWiseApp/1.0 vinh@example.com python-requests/2.x'}

final_recipes = []
for r in recipes:
    image_url = None
    q = r["title"]
    try:
        search_url = f"https://vi.wikipedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(q)}&utf8=&format=json"
        res = requests.get(search_url, headers=headers).json()
        if res.get('query', {}).get('search'):
            title = res['query']['search'][0]['title']
            url = f"https://vi.wikipedia.org/api/rest_v1/page/summary/{urllib.parse.quote(title)}"
            summary = requests.get(url, headers=headers).json()
            if 'thumbnail' in summary:
                image_url = summary['thumbnail']['source']
    except Exception as e:
        pass
    
    if not image_url:
        target_lower = q.lower()
        for k, v in fallback_unsplashes.items():
            if k in target_lower:
                image_url = v
                break
        if not image_url:
            image_url = "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=600"
            
    r["image_url"] = image_url
    final_recipes.append(r)

out_text = f'''"""
Script seeding dữ liệu mẫu món Việt Nam vào database Neon.
Chạy: cd backend && .\\venv\\Scripts\\python seed.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app import create_app
from app import db
from app.models import Recipe, CommunityPost, SavedRecipe

app = create_app()

RECIPES = {json.dumps(final_recipes, indent=2, ensure_ascii=False)}

COMMUNITY_POSTS = {json.dumps(community_posts, indent=2, ensure_ascii=False)}

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
        print("Success! Seeded comprehensive detailed recipes, posts, and saved recipes.")

if __name__ == "__main__":
    seed()
'''

with open("seed.py", "w", encoding="utf-8") as f:
    f.write(out_text)
