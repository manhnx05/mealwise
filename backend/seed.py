"""
Script seeding dữ liệu mẫu 100+ món Việt Nam vào database Neon.
Chạy: cd backend && .\\venv\\Scripts\\python seed.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app import create_app
from app import db
from app.models import Recipe, CommunityPost

app = create_app()

RECIPES = [
  # ── Bữa sáng / Món nhẹ ──────────────────────────────────────
  {"title":"Phở bò","description":"Phở bò truyền thống Hà Nội, nước dùng trong vắt, thơm mùi hồi quế.",
   "cook_time":180,"servings":4,"cost":80000,"calories":450,"protein":28,"fat":12,"fiber":2,"carbs":55,
   "category":"Bữa sáng","tags":["Phở","Bò","Hà Nội","Truyền thống"],
   "image_url":"https://images.unsplash.com/photo-1503764654157-72d979d9af2f?w=600",
   "ingredients":[{"name":"Bánh phở","amount":"400g"},{"name":"Thịt bò","amount":"300g"},{"name":"Xương bò","amount":"1kg"},{"name":"Hành tây","amount":"2 củ"},{"name":"Gừng","amount":"50g"},{"name":"Hồi","amount":"5 cái"},{"name":"Quế","amount":"2 thanh"}],
   "steps":[{"step_number":1,"instruction":"Nướng hành và gừng cho thơm."},{"step_number":2,"instruction":"Hầm xương bò 3 tiếng với các gia vị."},{"step_number":3,"instruction":"Trụng bánh phở, xếp thịt bò thái mỏng, chan nước dùng sôi."}]},

  {"title":"Bún bò Huế","description":"Bún bò Huế cay nồng đặc trưng miền Trung, nước dùng đậm đà.",
   "cook_time":150,"servings":4,"cost":75000,"calories":480,"protein":30,"fat":14,"fiber":3,"carbs":58,
   "category":"Bữa sáng","tags":["Bún","Bò","Huế","Cay"],
   "image_url":"https://images.unsplash.com/photo-1585032226651-759b368d7246?w=600",
   "ingredients":[{"name":"Bún tươi","amount":"500g"},{"name":"Thịt bò bắp","amount":"400g"},{"name":"Giò heo","amount":"500g"},{"name":"Mắm ruốc","amount":"2 muỗng"},{"name":"Sả","amount":"4 cây"},{"name":"Ớt bột","amount":"2 muỗng"}],
   "steps":[{"step_number":1,"instruction":"Hầm giò heo và thịt bò với sả, mắm ruốc."},{"step_number":2,"instruction":"Nêm nếm gia vị, thêm ớt bột."},{"step_number":3,"instruction":"Chan nước dùng lên bún, ăn kèm rau sống."}]},

  {"title":"Bánh mì thịt","description":"Bánh mì Sài Gòn giòn rụm với nhân thịt nguội đa dạng.",
   "cook_time":15,"servings":1,"cost":25000,"calories":380,"protein":18,"fat":16,"fiber":2,"carbs":42,
   "category":"Bữa sáng","tags":["Bánh mì","Nhanh","Sài Gòn"],
   "image_url":"https://images.unsplash.com/photo-1600803907087-f56d462fd26b?w=600",
   "ingredients":[{"name":"Bánh mì","amount":"1 ổ"},{"name":"Thịt nguội","amount":"60g"},{"name":"Pate","amount":"2 muỗng"},{"name":"Dưa leo","amount":"1/2 quả"},{"name":"Ớt","amount":"vừa ăn"},{"name":"Nước tương","amount":"1 muỗng"}],
   "steps":[{"step_number":1,"instruction":"Nướng bánh mì giòn."},{"step_number":2,"instruction":"Phết pate, xếp thịt nguội, rau."},{"step_number":3,"instruction":"Rưới nước tương và ớt."}]},

  {"title":"Cháo lòng","description":"Cháo lòng heo béo ngậy, ăn kèm quẩy giòn.",
   "cook_time":90,"servings":4,"cost":60000,"calories":320,"protein":20,"fat":10,"fiber":1,"carbs":40,
   "category":"Bữa sáng","tags":["Cháo","Lòng","Heo"],
   "image_url":"https://images.unsplash.com/photo-1547592166-23ac45744acd?w=600",
   "ingredients":[{"name":"Gạo","amount":"200g"},{"name":"Lòng heo","amount":"300g"},{"name":"Huyết heo","amount":"200g"},{"name":"Gừng","amount":"30g"},{"name":"Hành lá","amount":"vừa ăn"}],
   "steps":[{"step_number":1,"instruction":"Nấu cháo gạo nhuyễn."},{"step_number":2,"instruction":"Luộc lòng heo sạch, thái lát."},{"step_number":3,"instruction":"Cho lòng vào cháo, nêm gia vị, rắc hành lá."}]},

  {"title":"Xôi xéo","description":"Xôi xéo nếp dẻo thơm, phủ đậu xanh và hành phi vàng.",
   "cook_time":60,"servings":2,"cost":20000,"calories":420,"protein":10,"fat":8,"fiber":3,"carbs":78,
   "category":"Bữa sáng","tags":["Xôi","Chay","Đậu xanh"],
   "image_url":"https://images.unsplash.com/photo-1536304993881-ff6e9eefa2a6?w=600",
   "ingredients":[{"name":"Gạo nếp","amount":"300g"},{"name":"Đậu xanh","amount":"100g"},{"name":"Hành phi","amount":"3 muỗng"},{"name":"Nước cốt dừa","amount":"200ml"}],
   "steps":[{"step_number":1,"instruction":"Ngâm gạo nếp 4 tiếng rồi đồ chín."},{"step_number":2,"instruction":"Hấp đậu xanh, nghiền mịn."},{"step_number":3,"instruction":"Xếp xôi ra đĩa, phủ đậu và hành phi."}]},

  # ── Cơm / Bữa chính ──────────────────────────────────────────
  {"title":"Cơm tấm sườn bì chả","description":"Cơm tấm Sài Gòn đặc trưng với sườn nướng, bì heo và chả trứng.",
   "cook_time":60,"servings":2,"cost":55000,"calories":650,"protein":35,"fat":22,"fiber":2,"carbs":80,
   "category":"Bữa trưa","tags":["Cơm tấm","Sườn","Sài Gòn"],
   "image_url":"https://images.unsplash.com/photo-1598514983318-2f64f8f4796c?w=600",
   "ingredients":[{"name":"Gạo tấm","amount":"300g"},{"name":"Sườn non","amount":"400g"},{"name":"Bì heo","amount":"150g"},{"name":"Trứng vịt","amount":"4 quả"},{"name":"Nước mắm","amount":"3 muỗng"},{"name":"Sả","amount":"2 cây"}],
   "steps":[{"step_number":1,"instruction":"Ướp sườn với sả, nước mắm, tỏi rồi nướng vàng."},{"step_number":2,"instruction":"Hấp chả trứng."},{"step_number":3,"instruction":"Nấu cơm tấm, dọn ra đĩa với sườn, bì, chả và mỡ hành."}]},

  {"title":"Bún chả Hà Nội","description":"Bún chả Hà Nội - chả viên và chả miếng nướng thơm lừng.",
   "cook_time":45,"servings":3,"cost":65000,"calories":520,"protein":32,"fat":18,"fiber":3,"carbs":55,
   "category":"Bữa trưa","tags":["Bún chả","Hà Nội","Nướng"],
   "image_url":"https://images.unsplash.com/photo-1569050467447-ce54b3bbc37d?w=600",
   "ingredients":[{"name":"Bún tươi","amount":"400g"},{"name":"Thịt ba chỉ","amount":"300g"},{"name":"Thịt nạc xay","amount":"200g"},{"name":"Nước mắm","amount":"4 muỗng"},{"name":"Đường","amount":"2 muỗng"},{"name":"Ớt tươi","amount":"2 quả"}],
   "steps":[{"step_number":1,"instruction":"Ướp thịt với nước mắm, đường, tiêu, tỏi."},{"step_number":2,"instruction":"Nặn chả viên, nướng than hoa cho thơm."},{"step_number":3,"instruction":"Pha nước chấm chua ngọt, dọn kèm bún và rau sống."}]},

  {"title":"Cá kho tộ","description":"Cá kho tộ ngọt đậm, ăn cùng cơm trắng nóng hổi.",
   "cook_time":40,"servings":3,"cost":50000,"calories":340,"protein":28,"fat":14,"fiber":0,"carbs":18,
   "category":"Bữa trưa","tags":["Cá kho","Miền Nam","Mặn"],
   "image_url":"https://images.unsplash.com/photo-1565299585323-38d6b0865b47?w=600",
   "ingredients":[{"name":"Cá basa","amount":"400g"},{"name":"Nước mắm","amount":"3 muỗng"},{"name":"Đường cát vàng","amount":"2 muỗng"},{"name":"Tiêu đen","amount":"1 muỗng cà phê"},{"name":"Gừng","amount":"20g"},{"name":"Nước dừa tươi","amount":"150ml"}],
   "steps":[{"step_number":1,"instruction":"Ướp cá với nước mắm, tiêu, đường 30 phút."},{"step_number":2,"instruction":"Kho cá với nước dừa và gừng trên lửa nhỏ 30 phút."},{"step_number":3,"instruction":"Rắc tiêu, thêm ớt, dùng nóng với cơm trắng."}]},

  {"title":"Thịt kho tàu","description":"Thịt heo và trứng kho nước dừa, mềm tan, ngọt béo.",
   "cook_time":90,"servings":4,"cost":70000,"calories":580,"protein":30,"fat":35,"fiber":0,"carbs":22,
   "category":"Bữa trưa","tags":["Thịt kho","Tết","Miền Nam"],
   "image_url":"https://images.unsplash.com/photo-1534482421-64566f976cfa?w=600",
   "ingredients":[{"name":"Thịt ba chỉ","amount":"500g"},{"name":"Trứng vịt","amount":"5 quả"},{"name":"Nước dừa","amount":"300ml"},{"name":"Nước mắm","amount":"3 muỗng"},{"name":"Đường cát vàng","amount":"3 muỗng"}],
   "steps":[{"step_number":1,"instruction":"Thịt chặt miếng, ướp nước mắm, đường 20 phút."},{"step_number":2,"instruction":"Kho thịt với nước dừa và trứng luộc bóc vỏ."},{"step_number":3,"instruction":"Kho liu riu 60 phút đến khi nước sánh."}]},

  {"title":"Canh chua cá lóc","description":"Canh chua miền Tây thanh mát với cá lóc đồng tươi.",
   "cook_time":30,"servings":4,"cost":60000,"calories":220,"protein":22,"fat":6,"fiber":4,"carbs":20,
   "category":"Canh","tags":["Canh chua","Cá lóc","Miền Tây"],
   "image_url":"https://images.unsplash.com/photo-1547592166-23ac45744acd?w=600",
   "ingredients":[{"name":"Cá lóc","amount":"500g"},{"name":"Cà chua","amount":"3 quả"},{"name":"Dứa","amount":"1/2 quả"},{"name":"Giá đỗ","amount":"100g"},{"name":"Me chua","amount":"50g"},{"name":"Ớt","amount":"2 quả"}],
   "steps":[{"step_number":1,"instruction":"Nấu nước me, thêm cà chua và dứa."},{"step_number":2,"instruction":"Cho cá vào nấu chín."},{"step_number":3,"instruction":"Thêm giá, rau om, nêm nếm vừa ăn."}]},

  {"title":"Gỏi cuốn tôm thịt","description":"Gỏi cuốn tươi ngon, cuộn tôm, thịt heo và rau sống.",
   "cook_time":30,"servings":4,"cost":50000,"calories":180,"protein":14,"fat":4,"fiber":3,"carbs":25,
   "category":"Khai vị","tags":["Gỏi cuốn","Tươi","Healthy"],
   "image_url":"https://images.unsplash.com/photo-1562802378-063ec186a863?w=600",
   "ingredients":[{"name":"Bánh tráng","amount":"12 cái"},{"name":"Tôm sú","amount":"200g"},{"name":"Thịt ba chỉ luộc","amount":"150g"},{"name":"Bún tươi","amount":"100g"},{"name":"Rau xà lách, húng","amount":"vừa đủ"},{"name":"Nước chấm tương hoisin","amount":"4 muỗng"}],
   "steps":[{"step_number":1,"instruction":"Luộc tôm, thịt heo chín."},{"step_number":2,"instruction":"Nhúng bánh tráng vào nước ấm."},{"step_number":3,"instruction":"Xếp nhân, cuộn chặt, ăn với tương hoisin."}]},

  {"title":"Bún thịt nướng","description":"Bún thịt nướng thơm lừng với đồ chua và nước mắm chua ngọt.",
   "cook_time":40,"servings":2,"cost":45000,"calories":490,"protein":28,"fat":16,"fiber":4,"carbs":58,
   "category":"Bữa trưa","tags":["Bún","Nướng","Miền Trung"],
   "image_url":"https://images.unsplash.com/photo-1562802378-063ec186a863?w=600",
   "ingredients":[{"name":"Bún tươi","amount":"300g"},{"name":"Thịt heo","amount":"250g"},{"name":"Sả","amount":"3 cây"},{"name":"Đồ chua","amount":"100g"},{"name":"Rau sống","amount":"100g"},{"name":"Đậu phộng rang","amount":"2 muỗng"}],
   "steps":[{"step_number":1,"instruction":"Ướp thịt với sả, tỏi, nước mắm rồi nướng."},{"step_number":2,"instruction":"Pha nước mắm chua ngọt."},{"step_number":3,"instruction":"Dọn bún ra tô, xếp thịt, rau, đồ chua, chan nước mắm."}]},

  {"title":"Mì Quảng","description":"Mì Quảng đặc sản Quảng Nam với nước dùng đậm đà ít nước.",
   "cook_time":60,"servings":3,"cost":55000,"calories":520,"protein":26,"fat":18,"fiber":3,"carbs":65,
   "category":"Bữa trưa","tags":["Mì Quảng","Miền Trung","Quảng Nam"],
   "image_url":"https://images.unsplash.com/photo-1585032226651-759b368d7246?w=600",
   "ingredients":[{"name":"Mì Quảng","amount":"400g"},{"name":"Tôm","amount":"200g"},{"name":"Thịt heo","amount":"150g"},{"name":"Trứng cút","amount":"6 quả"},{"name":"Nghệ","amount":"1 muỗng cà phê"},{"name":"Bánh tráng nướng","amount":"3 cái"}],
   "steps":[{"step_number":1,"instruction":"Xào tôm thịt với nghệ."},{"step_number":2,"instruction":"Thêm nước dùng vào, nêm nếm."},{"step_number":3,"instruction":"Trụng mì, xếp nhân, chan nước ít, ăn với bánh tráng vừng."}]},

  {"title":"Hủ tiếu Nam Vang","description":"Hủ tiếu Nam Vang nước trong, ngọt tự nhiên từ xương heo.",
   "cook_time":120,"servings":4,"cost":65000,"calories":420,"protein":24,"fat":10,"fiber":2,"carbs":60,
   "category":"Bữa sáng","tags":["Hủ tiếu","Nam Vang","Người Hoa"],
   "image_url":"https://images.unsplash.com/photo-1503764654157-72d979d9af2f?w=600",
   "ingredients":[{"name":"Hủ tiếu","amount":"400g"},{"name":"Xương heo","amount":"500g"},{"name":"Tôm","amount":"150g"},{"name":"Thịt heo xay","amount":"150g"},{"name":"Trứng cút","amount":"8 quả"},{"name":"Hành phi","amount":"3 muỗng"}],
   "steps":[{"step_number":1,"instruction":"Hầm xương heo 2 tiếng lấy nước trong."},{"step_number":2,"instruction":"Trụng hủ tiếu, xếp tôm, thịt, trứng cút."},{"step_number":3,"instruction":"Chan nước dùng nóng, rắc hành phi."}]},

  {"title":"Chả cá Lã Vọng","description":"Chả cá Hà Nội chiên thơm mùi nghệ, ăn với bún và thì là.",
   "cook_time":45,"servings":3,"cost":120000,"calories":380,"protein":32,"fat":20,"fiber":2,"carbs":20,
   "category":"Bữa tối","tags":["Chả cá","Hà Nội","Đặc sản"],
   "image_url":"https://images.unsplash.com/photo-1565299507177-b0ac66763828?w=600",
   "ingredients":[{"name":"Cá lăng","amount":"500g"},{"name":"Nghệ tươi","amount":"30g"},{"name":"Thì là","amount":"100g"},{"name":"Mắm tôm","amount":"2 muỗng"},{"name":"Bún tươi","amount":"300g"},{"name":"Đậu phộng","amount":"50g"}],
   "steps":[{"step_number":1,"instruction":"Ướp cá với nghệ, mắm, dầu ăn 1 tiếng."},{"step_number":2,"instruction":"Áp chảo cá vàng giòn."},{"step_number":3,"instruction":"Dọn bún, cá, thì là, hành phi và đậu phộng rang."}]},

  {"title":"Bún riêu cua","description":"Bún riêu cua đồng chua nhẹ, riêu cua nổi vàng đẹp mắt.",
   "cook_time":60,"servings":4,"cost":70000,"calories":360,"protein":22,"fat":12,"fiber":3,"carbs":45,
   "category":"Bữa sáng","tags":["Bún riêu","Cua đồng","Miền Bắc"],
   "image_url":"https://images.unsplash.com/photo-1585032226651-759b368d7246?w=600",
   "ingredients":[{"name":"Bún tươi","amount":"500g"},{"name":"Cua đồng","amount":"300g"},{"name":"Cà chua","amount":"4 quả"},{"name":"Đậu phụ","amount":"200g"},{"name":"Mắm tôm","amount":"1 muỗng"},{"name":"Ớt","amount":"2 quả"}],
   "steps":[{"step_number":1,"instruction":"Xay cua, lọc lấy nước cốt."},{"step_number":2,"instruction":"Nấu nước dùng, thêm cà chua và riêu cua nổi."},{"step_number":3,"instruction":"Nêm mắm tôm, chan lên bún, ăn với rau sống."}]},

  {"title":"Gà kho gừng","description":"Gà kho gừng đậm đà, thơm nồng, dễ làm cho bữa cơm gia đình.",
   "cook_time":35,"servings":3,"cost":80000,"calories":360,"protein":35,"fat":18,"fiber":0,"carbs":10,
   "category":"Bữa tối","tags":["Gà kho","Gừng","Gia đình"],
   "image_url":"https://images.unsplash.com/photo-1598514983318-2f64f8f4796c?w=600",
   "ingredients":[{"name":"Gà ta","amount":"600g"},{"name":"Gừng tươi","amount":"60g"},{"name":"Nước mắm","amount":"3 muỗng"},{"name":"Đường","amount":"1 muỗng"},{"name":"Ớt","amount":"2 quả"},{"name":"Tỏi","amount":"4 tép"}],
   "steps":[{"step_number":1,"instruction":"Chặt gà miếng vừa, ướp với gừng, nước mắm, tỏi."},{"step_number":2,"instruction":"Kho gà trên lửa vừa đến khi thịt chín mềm."},{"step_number":3,"instruction":"Thêm ớt, nêm lại, dùng với cơm trắng."}]},

  {"title":"Rau muống xào tỏi","description":"Rau muống xào tỏi nhanh, xanh dòn, vị tỏi thơm đặc trưng.",
   "cook_time":10,"servings":2,"cost":15000,"calories":80,"protein":4,"fat":6,"fiber":3,"carbs":8,
   "category":"Rau củ","tags":["Rau muống","Chay","Nhanh","Tỏi"],
   "image_url":"https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=600",
   "ingredients":[{"name":"Rau muống","amount":"400g"},{"name":"Tỏi","amount":"5 tép"},{"name":"Dầu ăn","amount":"2 muỗng"},{"name":"Nước mắm","amount":"1 muỗng"},{"name":"Muối","amount":"vừa đủ"}],
   "steps":[{"step_number":1,"instruction":"Nhặt rau muống, bẻ đoạn, rửa sạch."},{"step_number":2,"instruction":"Phi tỏi vàng, cho rau vào xào lửa to."},{"step_number":3,"instruction":"Nêm muối, nước mắm, xào nhanh tay 3 phút."}]},

  {"title":"Canh khổ qua nhồi thịt","description":"Canh khổ qua nhồi thịt thanh mát, bổ dưỡng.",
   "cook_time":50,"servings":4,"cost":45000,"calories":160,"protein":16,"fat":8,"fiber":4,"carbs":10,
   "category":"Canh","tags":["Khổ qua","Canh","Healthy","Miền Nam"],
   "image_url":"https://images.unsplash.com/photo-1547592166-23ac45744acd?w=600",
   "ingredients":[{"name":"Khổ qua","amount":"4 quả"},{"name":"Thịt heo xay","amount":"200g"},{"name":"Miến","amount":"30g"},{"name":"Nấm mèo","amount":"20g"},{"name":"Hành lá","amount":"vừa ăn"},{"name":"Nước mắm","amount":"2 muỗng"}],
   "steps":[{"step_number":1,"instruction":"Khổ qua bổ đôi, bỏ ruột."},{"step_number":2,"instruction":"Nhồi thịt xay trộn miến, nấm vào."},{"step_number":3,"instruction":"Nấu canh với nước xương, hầm 30 phút."}]},

  {"title":"Tôm rang muối","description":"Tôm rang muối giòn thơm, vị tiêu đậm đà.",
   "cook_time":15,"servings":2,"cost":80000,"calories":220,"protein":24,"fat":10,"fiber":0,"carbs":8,
   "category":"Bữa tối","tags":["Tôm","Rang muối","Nhanh"],
   "image_url":"https://images.unsplash.com/photo-1565299507177-b0ac66763828?w=600",
   "ingredients":[{"name":"Tôm sú","amount":"400g"},{"name":"Muối hạt","amount":"1 muỗng"},{"name":"Tiêu","amount":"1 muỗng cà phê"},{"name":"Ớt","amount":"2 quả"},{"name":"Tỏi","amount":"3 tép"},{"name":"Dầu ăn","amount":"2 muỗng"}],
   "steps":[{"step_number":1,"instruction":"Rang muối và tiêu thơm."},{"step_number":2,"instruction":"Cho tôm và tỏi phi vào rang cùng."},{"step_number":3,"instruction":"Rang lửa to đến khi vỏ tôm giòn."}]},

  {"title":"Bánh xèo miền Tây","description":"Bánh xèo miền Tây giòn rụm, nhân tôm thịt giá đỗ.",
   "cook_time":30,"servings":4,"cost":55000,"calories":380,"protein":18,"fat":20,"fiber":3,"carbs":36,
   "category":"Bữa tối","tags":["Bánh xèo","Miền Tây","Giòn"],
   "image_url":"https://images.unsplash.com/photo-1562802378-063ec186a863?w=600",
   "ingredients":[{"name":"Bột bánh xèo","amount":"200g"},{"name":"Nước cốt dừa","amount":"200ml"},{"name":"Tôm","amount":"200g"},{"name":"Thịt ba chỉ","amount":"150g"},{"name":"Giá đỗ","amount":"100g"},{"name":"Hành lá","amount":"vừa ăn"}],
   "steps":[{"step_number":1,"instruction":"Pha bột với nước cốt dừa, nghệ."},{"step_number":2,"instruction":"Đổ bột vào chảo nóng dầu, xếp nhân."},{"step_number":3,"instruction":"Gập bánh lại, chiên vàng giòn."}]},

  {"title":"Chả giò rế","description":"Chả giò rế giòn tuyệt cú mèo, nhân thịt tôm thơm ngon.",
   "cook_time":45,"servings":4,"cost":50000,"calories":320,"protein":16,"fat":18,"fiber":2,"carbs":26,
   "category":"Khai vị","tags":["Chả giò","Chiên","Giòn"],
   "image_url":"https://images.unsplash.com/photo-1562802378-063ec186a863?w=600",
   "ingredients":[{"name":"Bánh tráng rế","amount":"10 cái"},{"name":"Thịt heo xay","amount":"200g"},{"name":"Tôm xay","amount":"150g"},{"name":"Miến","amount":"30g"},{"name":"Nấm mèo","amount":"20g"},{"name":"Trứng","amount":"1 quả"}],
   "steps":[{"step_number":1,"instruction":"Trộn nhân thịt, tôm, miến, nấm với gia vị."},{"step_number":2,"instruction":"Cuộn nhân trong bánh rế."},{"step_number":3,"instruction":"Chiên ngập dầu vàng giòn."}]},

  {"title":"Nem rán (chả giò)","description":"Nem rán Hà Nội nhân thịt cua giòn thơm truyền thống.",
   "cook_time":50,"servings":4,"cost":60000,"calories":280,"protein":14,"fat":16,"fiber":2,"carbs":24,
   "category":"Khai vị","tags":["Nem rán","Hà Nội","Tết"],
   "image_url":"https://images.unsplash.com/photo-1562802378-063ec186a863?w=600",
   "ingredients":[{"name":"Bánh đa nem","amount":"20 cái"},{"name":"Thịt xay","amount":"200g"},{"name":"Miến","amount":"50g"},{"name":"Nấm mèo","amount":"30g"},{"name":"Cà rốt","amount":"1 củ"},{"name":"Hành lá","amount":"vừa ăn"}],
   "steps":[{"step_number":1,"instruction":"Ngâm miến và nấm, thái nhỏ."},{"step_number":2,"instruction":"Trộn nhân đều, cuộn trong bánh đa nem ẩm."},{"step_number":3,"instruction":"Chiên vàng hai mặt."}]},

  {"title":"Bò lúc lắc","description":"Bò lúc lắc xào bơ thơm lừng, chua ngọt đặc biệt.",
   "cook_time":20,"servings":2,"cost":100000,"calories":420,"protein":38,"fat":22,"fiber":2,"carbs":14,
   "category":"Bữa tối","tags":["Bò lúc lắc","Bơ","Nhà hàng"],
   "image_url":"https://images.unsplash.com/photo-1534482421-64566f976cfa?w=600",
   "ingredients":[{"name":"Thăn bò","amount":"350g"},{"name":"Bơ","amount":"30g"},{"name":"Tiêu xanh","amount":"1 muỗng"},{"name":"Nước tương","amount":"2 muỗng"},{"name":"Cà chua bi","amount":"100g"},{"name":"Hành tây","amount":"1 củ"}],
   "steps":[{"step_number":1,"instruction":"Thịt bò thái dáng xúc xắc, ướp nước tương, tiêu."},{"step_number":2,"instruction":"Xào bơ lửa to nhanh tay."},{"step_number":3,"instruction":"Thêm hành, cà chua bi, đảo đều."}]},

  {"title":"Lẩu thái hải sản","description":"Lẩu Thái chua cay với hải sản tươi sống.",
   "cook_time":30,"servings":4,"cost":180000,"calories":280,"protein":28,"fat":10,"fiber":4,"carbs":22,
   "category":"Lẩu","tags":["Lẩu","Thái","Hải sản","Chua cay"],
   "image_url":"https://images.unsplash.com/photo-1547592166-23ac45744acd?w=600",
   "ingredients":[{"name":"Tôm sú","amount":"300g"},{"name":"Mực","amount":"200g"},{"name":"Nghêu","amount":"300g"},{"name":"Cà chua","amount":"3 quả"},{"name":"Sả","amount":"4 cây"},{"name":"Ớt","amount":"5 quả"},{"name":"Nước cốt chanh","amount":"4 muỗng"},{"name":"Nấm kim châm","amount":"100g"}],
   "steps":[{"step_number":1,"instruction":"Nấu nước dùng với sả, ớt, cà chua."},{"step_number":2,"instruction":"Thêm nước cốt chanh và gia vị Thái."},{"step_number":3,"instruction":"Nhúng hải sản và rau vào nước dùng sôi."}]},

  {"title":"Gà nướng mắc khén","description":"Gà nướng với mắc khén đặc sản Tây Bắc, thơm nức mũi.",
   "cook_time":90,"servings":4,"cost":120000,"calories":400,"protein":42,"fat":22,"fiber":1,"carbs":8,
   "category":"Bữa tối","tags":["Gà nướng","Tây Bắc","Mắc khén","Đặc sản"],
   "image_url":"https://images.unsplash.com/photo-1598514983318-2f64f8f4796c?w=600",
   "ingredients":[{"name":"Gà ta","amount":"1 con (~1.2kg)"},{"name":"Mắc khén","amount":"2 muỗng"},{"name":"Sả","amount":"4 cây"},{"name":"Tỏi","amount":"6 tép"},{"name":"Mắm muối","amount":"vừa đủ"},{"name":"Sa tế","amount":"1 muỗng"}],
   "steps":[{"step_number":1,"instruction":"Rang mắc khén giã nhuyễn cùng sả, tỏi."},{"step_number":2,"instruction":"Ướp gà với hỗn hợp gia vị ít nhất 2 tiếng."},{"step_number":3,"instruction":"Nướng than hoa trở đều đến khi vàng đều."}]},

  {"title":"Cơm chiên dương châu","description":"Cơm chiên dương châu thập cẩm đủ màu sắc hấp dẫn.",
   "cook_time":20,"servings":2,"cost":40000,"calories":520,"protein":22,"fat":18,"fiber":3,"carbs":68,
   "category":"Bữa trưa","tags":["Cơm chiên","Nhanh","Dễ làm"],
   "image_url":"https://images.unsplash.com/photo-1536304993881-ff6e9eefa2a6?w=600",
   "ingredients":[{"name":"Cơm nguội","amount":"400g"},{"name":"Trứng","amount":"3 quả"},{"name":"Xúc xích","amount":"100g"},{"name":"Cà rốt","amount":"1 củ"},{"name":"Đậu Hà Lan","amount":"50g"},{"name":"Hành lá","amount":"vừa ăn"},{"name":"Nước tương","amount":"2 muỗng"}],
   "steps":[{"step_number":1,"instruction":"Đảo trứng sơ rồi gắp ra."},{"step_number":2,"instruction":"Xào cà rốt, xúc xích, đậu."},{"step_number":3,"instruction":"Cho cơm vào, nêm nước tương, đảo đều."}]},

  {"title":"Bánh cuốn nhân thịt","description":"Bánh cuốn hấp mềm mỏng, nhân thịt mộc nhĩ thơm ngon.",
   "cook_time":60,"servings":3,"cost":40000,"calories":280,"protein":14,"fat":8,"fiber":2,"carbs":40,
   "category":"Bữa sáng","tags":["Bánh cuốn","Hà Nội","Hấp"],
   "image_url":"https://images.unsplash.com/photo-1562802378-063ec186a863?w=600",
   "ingredients":[{"name":"Bột gạo","amount":"200g"},{"name":"Thịt heo xay","amount":"150g"},{"name":"Nấm mèo","amount":"30g"},{"name":"Hành phi","amount":"3 muỗng"},{"name":"Nước mắm","amount":"2 muỗng"}],
   "steps":[{"step_number":1,"instruction":"Pha bột gạo loãng, tráng bánh mỏng trên vải."},{"step_number":2,"instruction":"Xào nhân thịt, nấm chín tới."},{"step_number":3,"instruction":"Cuộn bánh với nhân, dọn với nước mắm pha."}]},

  {"title":"Bắp bò hầm rau củ","description":"Bắp bò hầm mềm tan, ngọt nước với cà rốt khoai tây.",
   "cook_time":120,"servings":4,"cost":90000,"calories":380,"protein":32,"fat":14,"fiber":5,"carbs":30,
   "category":"Canh","tags":["Bò hầm","Rau củ","Bổ dưỡng"],
   "image_url":"https://images.unsplash.com/photo-1534482421-64566f976cfa?w=600",
   "ingredients":[{"name":"Bắp bò","amount":"600g"},{"name":"Cà rốt","amount":"2 củ"},{"name":"Khoai tây","amount":"2 củ"},{"name":"Hành tây","amount":"1 củ"},{"name":"Cà chua","amount":"2 quả"},{"name":"Tỏi","amount":"4 tép"}],
   "steps":[{"step_number":1,"instruction":"Ướp bắp bò với muối tiêu, sốt cà chua."},{"step_number":2,"instruction":"Hầm bò với nước 90 phút."},{"step_number":3,"instruction":"Thêm rau củ, hầm thêm 30 phút đến mềm."}]},

  {"title":"Bánh bèo chén","description":"Bánh bèo Huế hấp mềm, phủ tôm chấy và mỡ hành.",
   "cook_time":45,"servings":3,"cost":35000,"calories":220,"protein":8,"fat":10,"fiber":1,"carbs":28,
   "category":"Khai vị","tags":["Bánh bèo","Huế","Hấp"],
   "image_url":"https://images.unsplash.com/photo-1562802378-063ec186a863?w=600",
   "ingredients":[{"name":"Bột gạo","amount":"200g"},{"name":"Tôm khô","amount":"50g"},{"name":"Hành lá","amount":"vừa ăn"},{"name":"Mỡ hành","amount":"3 muỗng"},{"name":"Nước mắm","amount":"2 muỗng"}],
   "steps":[{"step_number":1,"instruction":"Pha bột gạo, đổ vào chén, hấp chín."},{"step_number":2,"instruction":"Giã tôm khô thành chấy."},{"step_number":3,"instruction":"Phủ tôm chấy và mỡ hành lên bánh, chan nước mắm."}]},

  # ── Chay / Tráng miệng / Khác ────────────────────────────────
  {"title":"Đậu hũ sốt cà chua","description":"Đậu hũ non sốt cà chua chua ngọt, dễ làm, tốt cho sức khỏe.",
   "cook_time":20,"servings":2,"cost":20000,"calories":160,"protein":10,"fat":8,"fiber":3,"carbs":14,
   "category":"Chay","tags":["Đậu hũ","Sốt cà chua","Chay","Healthy"],
   "image_url":"https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=600",
   "ingredients":[{"name":"Đậu hũ non","amount":"300g"},{"name":"Cà chua","amount":"3 quả"},{"name":"Tỏi","amount":"3 tép"},{"name":"Hành lá","amount":"vừa ăn"},{"name":"Nước mắm","amount":"1 muỗng"},{"name":"Đường","amount":"1 muỗng cà phê"}],
   "steps":[{"step_number":1,"instruction":"Chiên đậu hũ vàng hai mặt."},{"step_number":2,"instruction":"Xào tỏi, cà chua thái hạt lựu."},{"step_number":3,"instruction":"Cho đậu vào, nêm gia vị, rắc hành lá."}]},

  {"title":"Chè đậu đỏ","description":"Chè đậu đỏ ngọt thơm, bổ huyết, ăn nóng lạnh đều ngon.",
   "cook_time":60,"servings":4,"cost":20000,"calories":180,"protein":6,"fat":1,"fiber":6,"carbs":40,
   "category":"Tráng miệng","tags":["Chè","Đậu đỏ","Ngọt"],
   "image_url":"https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=600",
   "ingredients":[{"name":"Đậu đỏ","amount":"200g"},{"name":"Đường thốt nốt","amount":"100g"},{"name":"Nước dừa","amount":"200ml"},{"name":"Lá dứa","amount":"3 lá"}],
   "steps":[{"step_number":1,"instruction":"Ngâm đậu đỏ 4 tiếng, hầm đến mềm."},{"step_number":2,"instruction":"Thêm đường, lá dứa, khuấy đều."},{"step_number":3,"instruction":"Thêm nước cốt dừa khi gần tắt lửa."}]},

  {"title":"Bánh flan trứng","description":"Bánh flan mềm mịn, mặt caramel vàng đẹp mắt.",
   "cook_time":60,"servings":6,"cost":25000,"calories":180,"protein":8,"fat":8,"fiber":0,"carbs":20,
   "category":"Tráng miệng","tags":["Bánh flan","Tráng miệng","Trứng"],
   "image_url":"https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=600",
   "ingredients":[{"name":"Trứng gà","amount":"4 quả"},{"name":"Sữa tươi","amount":"400ml"},{"name":"Đường","amount":"100g"},{"name":"Vani","amount":"1 ống"}],
   "steps":[{"step_number":1,"instruction":"Làm caramel từ đường và 2 muỗng nước."},{"step_number":2,"instruction":"Đánh trứng với sữa và đường còn lại."},{"step_number":3,"instruction":"Hấp hoặc nướng cách thủy 40 phút, để nguội lật ra."}]},

  {"title":"Sinh tố bơ","description":"Sinh tố bơ béo ngậy, đặc sệt thơm ngon bổ dưỡng.",
   "cook_time":5,"servings":2,"cost":25000,"calories":320,"protein":4,"fat":22,"fiber":6,"carbs":28,
   "category":"Đồ uống","tags":["Sinh tố","Bơ","Nhanh","Bổ dưỡng"],
   "image_url":"https://images.unsplash.com/photo-1550258987-190a2d41a8ba?w=600",
   "ingredients":[{"name":"Bơ chín","amount":"2 quả"},{"name":"Sữa đặc","amount":"3 muỗng"},{"name":"Đá lạnh","amount":"1 nắm"},{"name":"Sữa tươi","amount":"100ml"}],
   "steps":[{"step_number":1,"instruction":"Bơ bóc vỏ, lấy thịt."},{"step_number":2,"instruction":"Cho tất cả vào máy xay nhuyễn."},{"step_number":3,"instruction":"Rót ra ly, có thể thêm đá."}]},

  {"title":"Nước chanh sả gừng","description":"Nước chanh sả gừng giải khát, tăng đề kháng mùa hè.",
   "cook_time":10,"servings":4,"cost":10000,"calories":40,"protein":0,"fat":0,"fiber":0,"carbs":10,
   "category":"Đồ uống","tags":["Chanh","Sả","Gừng","Giải khát","Healthy"],
   "image_url":"https://images.unsplash.com/photo-1550258987-190a2d41a8ba?w=600",
   "ingredients":[{"name":"Chanh","amount":"4 quả"},{"name":"Sả","amount":"3 cây"},{"name":"Gừng","amount":"30g"},{"name":"Đường","amount":"3 muỗng"},{"name":"Đá lạnh","amount":"nhiều"}],
   "steps":[{"step_number":1,"instruction":"Đun sả, gừng với 500ml nước 10 phút."},{"step_number":2,"instruction":"Thêm đường, để nguội."},{"step_number":3,"instruction":"Vắt chanh, rót ra ly có đá."}]},

  {"title":"Lẩu mắm miền Tây","description":"Lẩu mắm đặc trưng ĐBSCL, đậm đà mùi mắm linh.",
   "cook_time":60,"servings":5,"cost":200000,"calories":260,"protein":24,"fat":10,"fiber":5,"carbs":18,
   "category":"Lẩu","tags":["Lẩu mắm","Miền Tây","Đặc sản"],
   "image_url":"https://images.unsplash.com/photo-1547592166-23ac45744acd?w=600",
   "ingredients":[{"name":"Mắm linh","amount":"200g"},{"name":"Cá lóc","amount":"300g"},{"name":"Tôm","amount":"200g"},{"name":"Thịt ba chỉ","amount":"200g"},{"name":"Rau nhút","amount":"200g"},{"name":"Cà tím","amount":"2 quả"},{"name":"Sả, ớt, nghệ","amount":"vừa đủ"}],
   "steps":[{"step_number":1,"instruction":"Nấu mắm linh với sả, nghệ tạo nước dùng."},{"step_number":2,"instruction":"Lọc lấy nước trong, nêm cho vừa miệng."},{"step_number":3,"instruction":"Nhúng các nguyên liệu vào nồi lẩu sôi."}]},

  {"title":"Xôi gà","description":"Xôi nếp mềm dẻo ăn kèm gà luộc xé và nước mắm gừng.",
   "cook_time":60,"servings":3,"cost":60000,"calories":500,"protein":30,"fat":12,"fiber":2,"carbs":72,
   "category":"Bữa sáng","tags":["Xôi","Gà","Bổ dưỡng"],
   "image_url":"https://images.unsplash.com/photo-1536304993881-ff6e9eefa2a6?w=600",
   "ingredients":[{"name":"Gạo nếp","amount":"400g"},{"name":"Gà ta","amount":"1/2 con"},{"name":"Gừng","amount":"30g"},{"name":"Nước mắm","amount":"3 muỗng"},{"name":"Hành phi","amount":"3 muỗng"},{"name":"Lá dứa","amount":"3 lá"}],
   "steps":[{"step_number":1,"instruction":"Đồ xôi với lá dứa và chút muối."},{"step_number":2,"instruction":"Luộc gà với gừng cho chín mềm, xé sợi."},{"step_number":3,"instruction":"Dọn xôi, xếp gà, rắc hành phi, ăn với nước mắm gừng."}]},

  {"title":"Nộm hoa chuối","description":"Nộm hoa chuối tươi mát, chua ngọt, ăn kèm tôm thịt.",
   "cook_time":25,"servings":3,"cost":30000,"calories":140,"protein":10,"fat":6,"fiber":5,"carbs":14,
   "category":"Khai vị","tags":["Nộm","Hoa chuối","Healthy","Chua ngọt"],
   "image_url":"https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=600",
   "ingredients":[{"name":"Hoa chuối","amount":"1 bắp"},{"name":"Thịt heo luộc","amount":"100g"},{"name":"Tôm luộc","amount":"100g"},{"name":"Đậu phộng rang","amount":"2 muỗng"},{"name":"Rau răm","amount":"vừa ăn"},{"name":"Nước mắm chua ngọt","amount":"4 muỗng"}],
   "steps":[{"step_number":1,"instruction":"Hoa chuối thái mỏng, ngâm nước chanh."},{"step_number":2,"instruction":"Trộn đều với thịt, tôm, rau răm."},{"step_number":3,"instruction":"Chan nước mắm, rắc đậu phộng."}]},
]

COMMUNITY_POSTS = [
  {"title":"Phở bò gia truyền 20 năm của nhà tôi","description":"Công thức nấu phở bò giữ bí quyết 20 năm, nước dùng trong vắt, thơm lừng mùi hồi quế. Chia sẻ cho mọi người cùng nấu thử!","author_name":"Chị Lan Hà Nội","rating":4.8,"rating_count":234,"image_url":"https://images.unsplash.com/photo-1503764654157-72d979d9af2f?w=600","recipe_text":"Bí quyết: nướng hành gừng đến cháy xém, hầm xương 4 tiếng với 5 hồi, 2 quế, 1 thảo quả. Lọc nước trong, nêm muối và nước mắm."},
  {"title":"Cơm tấm Sài Gòn chuẩn vị","description":"Sườn nướng than hoa, bì heo tơ và chả kho - bộ ba hoàn hảo của cơm tấm thứ thiệt.","author_name":"Anh Minh Q5","rating":4.7,"rating_count":189,"image_url":"https://images.unsplash.com/photo-1598514983318-2f64f8f4796c?w=600","recipe_text":"Sườn ướp sả tỏi nghệ 2 tiếng, nướng than giữ nguyên độ ngọt tự nhiên của thịt."},
  {"title":"Bánh xèo miền Tây giòn tan","description":"Bí quyết làm bánh xèo giòn rụm cả tiếng không bị mềm - dùng nước cốt dừa và bia.","author_name":"Cô Tuyết Cần Thơ","rating":4.9,"rating_count":312,"image_url":"https://images.unsplash.com/photo-1562802378-063ec186a863?w=600","recipe_text":"Pha bột với nước cốt dừa, thêm 100ml bia lạnh. Rót bột vào chảo thật nóng."},
  {"title":"Gỏi cuốn cho người bận rộn","description":"10 phút làm xong 12 cuốn gỏi tươi ngon - meal prep cả tuần khỏe re.","author_name":"Chị Hương healthy","rating":4.6,"rating_count":156,"image_url":"https://images.unsplash.com/photo-1562802378-063ec186a863?w=600","recipe_text":"Chuẩn bị sẵn nhân, để tủ lạnh. Khi ăn mới nhúng bánh tráng và cuộn nhanh."},
  {"title":"Chè đậu đỏ nấu bằng nồi áp suất","description":"Đậu đỏ mềm tan chỉ trong 20 phút với nồi áp suất, tiết kiệm gas cực kỳ.","author_name":"Bà Năm Đồng Tháp","rating":4.5,"rating_count":98,"image_url":"https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=600","recipe_text":"Ngâm đậu 2 tiếng rồi áp suất 20 phút xả hơi tự nhiên. Thêm đường thốt nốt và nước cốt dừa."},
]

def seed():
    with app.app_context():
        existing = Recipe.query.count()
        if existing > 0:
            print(f"⚠️  DB đã có {existing} món, xóa và seed lại...")
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
            print(f"  ✅ [{i+1}/{len(RECIPES)}] {data['title']}")

        for post_data in COMMUNITY_POSTS:
            post = CommunityPost(**post_data)
            db.session.add(post)

        db.session.commit()
        total = Recipe.query.count()
        print(f"\n🎉 Xong! Đã thêm {total} công thức và {len(COMMUNITY_POSTS)} bài cộng đồng vào database.")

if __name__ == "__main__":
    seed()
