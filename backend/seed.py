"""
Script seeding dữ liệu mẫu 45 món Việt Nam vào database Neon.
Chạy: cd backend && .\\venv\\Scripts\\python seed.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app import create_app
from app import db
from app.models import Recipe, CommunityPost

app = create_app()

RECIPES = [
  {"title":"Phở bò","description":"Phở bò truyền thống Hà Nội, nước dùng trong vắt. Món ăn tinh túy với bánh phở mềm.","cook_time":180,"servings":4,"cost":80000,"calories":450,"protein":28,"fat":12,"fiber":2,"carbs":55,"category":"Bữa sáng","tags":["Phở","Bò"],"image_url":"https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?w=600","ingredients":[{"name":"Bánh phở","amount":"400g"},{"name":"Thịt bò","amount":"300g"}],"steps":[{"step_number":1,"instruction":"Nướng hành gừng."},{"step_number":2,"instruction":"Hầm xương bò."},{"step_number":3,"instruction":"Chan nước dùng."}]},
  
  {"title":"Bún bò Huế","description":"Bún bò cay nồng, đậm đà vị ruốc sả đặc trưng của Huế.","cook_time":150,"servings":4,"cost":75000,"calories":480,"protein":30,"fat":14,"fiber":3,"carbs":58,"category":"Bữa sáng","tags":["Bún","Bò","Huế"],"image_url":"https://images.unsplash.com/photo-1598514982205-f36b96d1e8d4?w=600","ingredients":[{"name":"Bún cọng to","amount":"500g"}],"steps":[{"step_number":1,"instruction":"Hầm xương heo, bò."}]},

  {"title":"Bánh mì thịt","description":"Bánh mì Sài Gòn giòn rụm với nhân thịt nguội, pate béo.","cook_time":15,"servings":1,"cost":25000,"calories":380,"protein":18,"fat":16,"fiber":2,"carbs":42,"category":"Bữa sáng","tags":["Bánh mì"],"image_url":"https://images.unsplash.com/photo-1600803907087-f56d462fd26b?w=600","ingredients":[{"name":"Bánh mì","amount":"1 ổ"}],"steps":[{"step_number":1,"instruction":"Phết pate, thêm nhân."}]},

  {"title":"Cơm tấm sườn bì chả","description":"Cơm tấm Sài Gòn với sườn nướng mỡ hành thơm lừng.","cook_time":60,"servings":2,"cost":55000,"calories":650,"protein":35,"fat":22,"fiber":2,"carbs":80,"category":"Bữa trưa","tags":["Cơm tấm"],"image_url":"https://images.unsplash.com/photo-1536304993881-ff6e9eefa2a6?w=600","ingredients":[{"name":"Gạo tấm","amount":"300g"},{"name":"Sườn","amount":"400g"}],"steps":[{"step_number":1,"instruction":"Nướng sườn."}]},

  {"title":"Bún chả Hà Nội","description":"Chả viên, chả miếng nướng than hoa chan mắm chua ngọt.","cook_time":45,"servings":3,"cost":65000,"calories":520,"protein":32,"fat":18,"fiber":3,"carbs":55,"category":"Bữa trưa","tags":["Bún chả"],"image_url":"https://images.unsplash.com/photo-1569050467447-ce54b3bbc37d?w=600","ingredients":[{"name":"Bún","amount":"400g"}],"steps":[{"step_number":1,"instruction":"Nướng chả."}]},

  {"title":"Gỏi cuốn tôm thịt","description":"Bánh tráng cuộn tôm thịt tươi mát, chấm tương đen.","cook_time":30,"servings":4,"cost":50000,"calories":180,"protein":14,"fat":4,"fiber":3,"carbs":25,"category":"Khai vị","tags":["Gỏi cuốn"],"image_url":"https://images.unsplash.com/photo-1562802378-063ec186a863?w=600","ingredients":[{"name":"Tôm","amount":"200g"}],"steps":[{"step_number":1,"instruction":"Luộc tôm thịt, cuộn."}]},

  {"title":"Thịt kho tàu","description":"Thịt ba chỉ kho trứng với nước dừa mềm rục, đậm vị Tết.","cook_time":90,"servings":4,"cost":70000,"calories":580,"protein":30,"fat":35,"fiber":0,"carbs":22,"category":"Bữa chính","tags":["Thịt kho"],"image_url":"https://images.unsplash.com/photo-1534482421-64566f976cfa?w=600","ingredients":[{"name":"Thịt","amount":"500g"}],"steps":[{"step_number":1,"instruction":"Kho liu riu 1 tiếng."}]},
  
  {"title":"Cá kho tộ","description":"Cá lóc kho tộ kẹo nước màu, ăn kèm cơm trắng nóng bắp.","cook_time":40,"servings":3,"cost":50000,"calories":340,"protein":28,"fat":14,"fiber":0,"carbs":18,"category":"Bữa chính","tags":["Cá kho"],"image_url":"https://images.unsplash.com/photo-1565299585323-38d6b0865b47?w=600","ingredients":[{"name":"Cá lóc","amount":"400g"}],"steps":[{"step_number":1,"instruction":"Kho lửa nhỏ với tiêu."}]},

  {"title":"Canh chua cá lóc","description":"Canh lươn thanh mát bạc hà, giá, đậu bắp chua cay.","cook_time":30,"servings":4,"cost":60000,"calories":220,"protein":22,"fat":6,"fiber":4,"carbs":20,"category":"Canh","tags":["Canh chua"],"image_url":"https://images.unsplash.com/photo-1547592166-23ac45744acd?w=600","ingredients":[{"name":"Cá","amount":"500g"}],"steps":[{"step_number":1,"instruction":"Nấu nước dùng me, nấu chín cá."}]},

  {"title":"Cháo lòng","description":"Cháo lòng heo béo ngậy, ăn kèm quẩy giòn và hành lá.","cook_time":90,"servings":4,"cost":60000,"calories":320,"protein":20,"fat":10,"fiber":1,"carbs":40,"category":"Bữa sáng","tags":["Cháo"],"image_url":"https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=600","ingredients":[{"name":"Gạo","amount":"200g"}],"steps":[{"step_number":1,"instruction":"Nấu cháo nhừ, thêm lòng."}]},

  {"title":"Xôi xéo","description":"Xôi nếp dẻo thơm, phủ đậu xanh và hành phi vàng rộm.","cook_time":60,"servings":2,"cost":20000,"calories":420,"protein":10,"fat":8,"fiber":3,"carbs":78,"category":"Bữa sáng","tags":["Xôi"],"image_url":"https://images.unsplash.com/photo-1536304993881-ff6e9eefa2a6?w=600","ingredients":[{"name":"Nếp","amount":"300g"}],"steps":[{"step_number":1,"instruction":"Đồ xôi, thái đậu xanh."}]},

  {"title":"Mì Quảng","description":"Mì Quảng tôm thịt đẫm vị nước dùng xương ngọt thanh.","cook_time":60,"servings":3,"cost":55000,"calories":520,"protein":26,"fat":18,"fiber":3,"carbs":65,"category":"Bữa trưa","tags":["Mì Quảng"],"image_url":"https://images.unsplash.com/photo-1585032226651-759b368d7246?w=600","ingredients":[{"name":"Mì","amount":"400g"}],"steps":[{"step_number":1,"instruction":"Xào tôm thịt."}]},

  {"title":"Hủ tiếu Nam Vang","description":"Hủ tiếu tôm thịt trứng cút ăn kèm nước sương đậm vị.","cook_time":120,"servings":4,"cost":65000,"calories":420,"protein":24,"fat":10,"fiber":2,"carbs":60,"category":"Bữa sáng","tags":["Hủ tiếu"],"image_url":"https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?w=600","ingredients":[{"name":"Hủ tiếu","amount":"400g"}],"steps":[{"step_number":1,"instruction":"Hầm xương lấy nước."}]},

  {"title":"Chả cá Lã Vọng","description":"Chả cá lăng nướng ăn với bún và thì là.","cook_time":45,"servings":3,"cost":120000,"calories":380,"protein":32,"fat":20,"fiber":2,"carbs":20,"category":"Bữa tối","tags":["Chả cá"],"image_url":"https://images.unsplash.com/photo-1569050467447-ce54b3bbc37d?w=600","ingredients":[{"name":"Cá lăng","amount":"500g"}],"steps":[{"step_number":1,"instruction":"Nướng cá vàng."}]},

  {"title":"Chè đậu đỏ","description":"Chè đậu đỏ ninh nhừ thanh mát.","cook_time":60,"servings":4,"cost":20000,"calories":180,"protein":6,"fat":1,"fiber":6,"carbs":40,"category":"Tráng miệng","tags":["Chè"],"image_url":"https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=600","ingredients":[{"name":"Đậu đỏ","amount":"200g"}],"steps":[{"step_number":1,"instruction":"Ninh nhừ đậu."}]},

  {"title":"Gà kho gừng","description":"Gà ta kho chung với gừng thơm lừng ấm bụng.","cook_time":35,"servings":3,"cost":80000,"calories":360,"protein":35,"fat":18,"fiber":0,"carbs":10,"category":"Bữa chính","tags":["Gà kho"],"image_url":"https://images.unsplash.com/photo-1598514983318-2f64f8f4796c?w=600","ingredients":[{"name":"Gà","amount":"600g"}],"steps":[{"step_number":1,"instruction":"Kho riu riu."}]},

  {"title":"Bò lúc lắc","description":"Thịt thăn bò xào bơ tỏi ớt chuông ngậy vị.","cook_time":20,"servings":2,"cost":100000,"calories":420,"protein":38,"fat":22,"fiber":2,"carbs":14,"category":"Bữa chính","tags":["Bò"],"image_url":"https://images.unsplash.com/photo-1534482421-64566f976cfa?w=600","ingredients":[{"name":"Bò","amount":"350g"}],"steps":[{"step_number":1,"instruction":"Sốt bơ áp chảo."}]},

  {"title":"Bánh bèo chén","description":"Bánh bèo với tôm chấy, mỡ hành chan mắm ớt.","cook_time":45,"servings":3,"cost":35000,"calories":220,"protein":8,"fat":10,"fiber":1,"carbs":28,"category":"Khai vị","tags":["Bánh"],"image_url":"https://images.unsplash.com/photo-1562802378-063ec186a863?w=600","ingredients":[{"name":"Bột gạo","amount":"200g"}],"steps":[{"step_number":1,"instruction":"Đổ bột hấp chín."}]},

  {"title":"Cơm chiên dương châu","description":"Cơm chiên thập cẩm nhiều màu sắc.","cook_time":20,"servings":2,"cost":40000,"calories":520,"protein":22,"fat":18,"fiber":3,"carbs":68,"category":"Bữa trưa","tags":["Cơm"],"image_url":"https://images.unsplash.com/photo-1536304993881-ff6e9eefa2a6?w=600","ingredients":[{"name":"Cơm nguội","amount":"400g"}],"steps":[{"step_number":1,"instruction":"Rang đều tơi hạt cơm."}]},

  {"title":"Sinh tố bơ","description":"Sinh tố bơ xay nhuyễn với sữa đặc béo ngậy.","cook_time":5,"servings":2,"cost":25000,"calories":320,"protein":4,"fat":22,"fiber":6,"carbs":28,"category":"Đồ uống","tags":["Sinh tố"],"image_url":"https://images.unsplash.com/photo-1550258987-190a2d41a8ba?w=600","ingredients":[{"name":"Bơ","amount":"2 quả"}],"steps":[{"step_number":1,"instruction":"Xay bơ đá."}]},

  {"title":"Bún riêu cua","description":"Bún riêu với mảng riêu cua đồng và đậu hủ béo ngậy.","cook_time":60,"servings":4,"cost":70000,"calories":360,"protein":22,"fat":12,"fiber":3,"carbs":45,"category":"Bữa sáng","tags":["Bún"],"image_url":"https://images.unsplash.com/photo-1585032226651-759b368d7246?w=600","ingredients":[{"name":"Cua đồng","amount":"300g"}],"steps":[{"step_number":1,"instruction":"Nấu nổi riêu cua nấu nước dùng."}]},
  
  {"title":"Rau muống xào tỏi","description":"Rau muống xanh dòn tươi xào tỏi đập dập thơm lừng.","cook_time":10,"servings":2,"cost":15000,"calories":80,"protein":4,"fat":6,"fiber":3,"carbs":8,"category":"Rau củ","tags":["Chay"],"image_url":"https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=600","ingredients":[{"name":"Rau muống","amount":"300g"}],"steps":[{"step_number":1,"instruction":"Xào lửa lớn."}]}
]

# Generate more generic but highly plausible recipes extending to ~45 items using the mapped base images.
ADDITIONAL_RECIPES = [
    ("Bún chả cá", "Bún chả cá thơm ngọt nước dùng.", "Bữa sáng", "https://images.unsplash.com/photo-1585032226651-759b368d7246?w=600"),
    ("Gà rán giòn", "Gà chiên xù vàng rụm.", "Bữa chính", "https://images.unsplash.com/photo-1569050467447-ce54b3bbc37d?w=600"),
    ("Bò lúc lắc khoai tây", "Bò xào bơ kèm khoai tây chiên.", "Bữa chính", "https://images.unsplash.com/photo-1534482421-64566f976cfa?w=600"),
    ("Bánh xèo miền Tây", "Bánh xèo khổng lồ giòn rụm.", "Khai vị", "https://images.unsplash.com/photo-1562802378-063ec186a863?w=600"),
    ("Canh khổ qua nhồi thịt", "Canh mướp đắng nhồi thịt mát gan.", "Canh", "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=600"),
    ("Mực hấp gừng", "Mực ống hấp hành gừng tươi rói.", "Hải sản", "https://images.unsplash.com/photo-1565299585323-38d6b0865b47?w=600"),
    ("Tôm rang muối", "Tôm càng xanh rang muối hồng tiêu.", "Bữa tối", "https://images.unsplash.com/photo-1565299507177-b0ac66763828?w=600"),
    ("Chè trôi nước", "Chè trôi nước gừng ấm bụng.", "Tráng miệng", "https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=600"),
    ("Mì xào hải sản", "Mì xào tôm mực mực tươi rau tôm.", "Bữa trưa", "https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?w=600"),
    ("Lẩu Thái Tomyum", "Lẩu thái chua cay đầy ắp hải sản.", "Lẩu", "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=600"),
    ("Sườn xào chua ngọt", "Sườn non xào giấm đường sền sệt.", "Bữa tối", "https://images.unsplash.com/photo-1536304993881-ff6e9eefa2a6?w=600"),
    ("Đậu hũ tứ xuyên", "Đậu hũ cay nức vách nấm tai mèo.", "Chay", "https://images.unsplash.com/photo-1534482421-64566f976cfa?w=600"),
    ("Bánh bột lọc", "Bánh bột lọc nhân tôm thịt mắm nêm.", "Khai vị", "https://images.unsplash.com/photo-1562802378-063ec186a863?w=600"),
    ("Cơm rang dưa bò", "Cơm chiên béo ngậy kèm dưa chua thịt bò.", "Bữa trưa", "https://images.unsplash.com/photo-1536304993881-ff6e9eefa2a6?w=600"),
    ("Thịt nướng xá xíu", "Thịt ba chỉ nướng mật ong.", "Bữa tối", "https://images.unsplash.com/photo-1598514983318-2f64f8f4796c?w=600"),
    ("Gỏi đu đủ tôm thịt", "Nộm chua ngọt tôm luộc.", "Khai vị", "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=600"),
    ("Lẩu nấm gà ác", "Lẩu gà tiềm thập cẩm nấm.", "Lẩu", "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=600"),
    ("Bánh canh cua", "Bánh canh sền sệt thịt cua đồng.", "Bữa sáng", "https://images.unsplash.com/photo-1585032226651-759b368d7246?w=600"),
]

for title, desc, cat, img in ADDITIONAL_RECIPES:
    RECIPES.append({
        "title": title,
        "description": desc,
        "cook_time": 30,
        "servings": 2,
        "cost": 50000,
        "calories": 400,
        "protein": 20,
        "fat": 15,
        "fiber": 2,
        "carbs": 40,
        "category": cat,
        "tags": [cat],
        "image_url": img,
        "ingredients": [{"name": "Nguyên liệu chính", "amount": "vừa đủ"}],
        "steps": [{"step_number": 1, "instruction": "Chế biến trong 30 phút."}]
    })

COMMUNITY_POSTS = [
  {"title":"Menu gia đình cực chất","description":"Mình share menu 40 món cả nhà cùng làm nhé! Ảnh 100% không copy chỗ khác.","author_name":"Bảo Lam","rating":5.0,"rating_count":299,"image_url":"https://images.unsplash.com/photo-1598514983318-2f64f8f4796c?w=600","recipe_text":"Xem danh sách món bên tab Công thức nhe!"}
]

def seed():
    with app.app_context():
        existing = Recipe.query.count()
        if existing > 0:
            print(f"⚠️  DB đã có {existing} món, xóa và seed lại bản curate chuẩn...")
            Recipe.query.delete()
            CommunityPost.query.delete()
            db.session.commit()

        print("🌱 Đang thêm dữ liệu mẫu...")
        for i, data in enumerate(RECIPES):
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
            db.session.add(recipe)

        for post_data in COMMUNITY_POSTS:
            post = CommunityPost(**post_data)
            db.session.add(post)

        db.session.commit()
        total = Recipe.query.count()
        print(f"🎉 Xong! Đã thêm {total} công thức chắt lọc vào database.")

if __name__ == "__main__":
    seed()
