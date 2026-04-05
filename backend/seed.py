"""
Script seeding dữ liệu mẫu món Việt Nam vào database Neon.
Chạy: cd backend && .\venv\Scripts\python seed.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app import create_app
from app import db
from app.models import Recipe, CommunityPost

app = create_app()

RECIPES = [
  {
    "title": "Phở bò",
    "description": "Phở bò truyền thống Hà Nội.",
    "cook_time": 180,
    "servings": 4,
    "cost": 80000,
    "calories": 450,
    "protein": 28,
    "fat": 12,
    "fiber": 2,
    "carbs": 55,
    "category": "Bữa sáng",
    "tags": [
      "Phở",
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
    "description": "Bún bò cay nồng đặc trưng Huế.",
    "cook_time": 150,
    "servings": 4,
    "cost": 75000,
    "calories": 480,
    "protein": 30,
    "fat": 14,
    "fiber": 3,
    "carbs": 58,
    "category": "Bữa sáng",
    "tags": [
      "Bún",
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
    "description": "Bánh mì Sài Gòn giòn rụm với nhân thịt nguội.",
    "cook_time": 15,
    "servings": 1,
    "cost": 25000,
    "calories": 380,
    "protein": 18,
    "fat": 16,
    "fiber": 2,
    "carbs": 42,
    "category": "Bữa sáng",
    "tags": [
      "Bánh mì"
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
    "title": "Cơm tấm",
    "description": "Cơm tấm Sài Gòn với sườn nướng mỡ hành.",
    "cook_time": 60,
    "servings": 2,
    "cost": 55000,
    "calories": 650,
    "protein": 35,
    "fat": 22,
    "fiber": 2,
    "carbs": 80,
    "category": "Bữa trưa",
    "tags": [
      "Cơm tấm"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/C%C6%A1m_T%E1%BA%A5m%2C_Da_Nang%2C_Vietnam.jpg/330px-C%C6%A1m_T%E1%BA%A5m%2C_Da_Nang%2C_Vietnam.jpg",
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
    "title": "Bún chả",
    "description": "Chả viên nướng than hoa chan mắm chua ngọt.",
    "cook_time": 45,
    "servings": 3,
    "cost": 65000,
    "calories": 520,
    "protein": 32,
    "fat": 18,
    "fiber": 3,
    "carbs": 55,
    "category": "Bữa trưa",
    "tags": [
      "Bún chả"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/B%C3%BAn_ch%E1%BA%A3_Th%E1%BB%A5y_Khu%C3%AA.jpg/330px-B%C3%BAn_ch%E1%BA%A3_Th%E1%BB%A5y_Khu%C3%AA.jpg",
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
    "description": "Bánh tráng cuộn tôm thịt tươi mát.",
    "cook_time": 30,
    "servings": 4,
    "cost": 50000,
    "calories": 180,
    "protein": 14,
    "fat": 4,
    "fiber": 3,
    "carbs": 25,
    "category": "Khai vị",
    "tags": [
      "Gỏi cuốn"
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
    "title": "Thịt kho tàu",
    "description": "Thịt ba chỉ kho trứng với nước dừa.",
    "cook_time": 90,
    "servings": 4,
    "cost": 70000,
    "calories": 580,
    "protein": 30,
    "fat": 35,
    "fiber": 0,
    "carbs": 22,
    "category": "Bữa chính",
    "tags": [
      "Thịt kho"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Caramelized_Pork_and_Eggs.jpg/330px-Caramelized_Pork_and_Eggs.jpg",
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
    "title": "Cá kho tộ",
    "description": "Cá lóc kho tộ kẹo nước màu.",
    "cook_time": 40,
    "servings": 3,
    "cost": 50000,
    "calories": 340,
    "protein": 28,
    "fat": 14,
    "fiber": 0,
    "carbs": 18,
    "category": "Bữa chính",
    "tags": [
      "Cá kho"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/vi/c/c0/Nguy%E1%BB%85n_Tr%C6%B0%E1%BB%9Dng_T%E1%BB%99.jpg",
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
    "title": "Canh chua",
    "description": "Canh chua cá lóc mát rượi.",
    "cook_time": 30,
    "servings": 4,
    "cost": 60000,
    "calories": 220,
    "protein": 22,
    "fat": 6,
    "fiber": 4,
    "carbs": 20,
    "category": "Canh",
    "tags": [
      "Canh chua"
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
    "title": "Cháo lòng",
    "description": "Cháo lòng heo béo ngậy.",
    "cook_time": 90,
    "servings": 4,
    "cost": 60000,
    "calories": 320,
    "protein": 20,
    "fat": 10,
    "fiber": 1,
    "carbs": 40,
    "category": "Bữa sáng",
    "tags": [
      "Cháo"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Ch%C3%A1o_l%C3%B2ng.jpg/330px-Ch%C3%A1o_l%C3%B2ng.jpg",
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
    "title": "Xôi xéo",
    "description": "Xôi nếp dẻo phủ đậu xanh hành phi.",
    "cook_time": 60,
    "servings": 2,
    "cost": 20000,
    "calories": 420,
    "protein": 10,
    "fat": 8,
    "fiber": 3,
    "carbs": 78,
    "category": "Bữa sáng",
    "tags": [
      "Xôi"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/X%C3%B4i_%C4%91%E1%BB%97_xanh.jpg/330px-X%C3%B4i_%C4%91%E1%BB%97_xanh.jpg",
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
    "title": "Mì Quảng",
    "description": "Mì Quảng tôm thịt đậm vị xương.",
    "cook_time": 60,
    "servings": 3,
    "cost": 55000,
    "calories": 520,
    "protein": 26,
    "fat": 18,
    "fiber": 3,
    "carbs": 65,
    "category": "Bữa trưa",
    "tags": [
      "Mì Quảng"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Mi_Quang_1A_Danang.jpg/330px-Mi_Quang_1A_Danang.jpg",
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
    "title": "Hủ tiếu",
    "description": "Hủ tiếu Nam Vang nước trong.",
    "cook_time": 120,
    "servings": 4,
    "cost": 65000,
    "calories": 420,
    "protein": 24,
    "fat": 10,
    "fiber": 2,
    "carbs": 60,
    "category": "Bữa sáng",
    "tags": [
      "Hủ tiếu"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/H%E1%BB%A7_t%C3%ADu_Nam_Vang_%28h%E1%BB%A7_t%C3%ADu_t%C3%B4m%29%2C_qu%C3%A1n_C%E1%BA%A7u_Tr%E1%BA%AFng%2C_K%C3%AAnh_n%C6%B0%E1%BB%9Bc_%C4%91en_%281%29.jpg/330px-H%E1%BB%A7_t%C3%ADu_Nam_Vang_%28h%E1%BB%A7_t%C3%ADu_t%C3%B4m%29%2C_qu%C3%A1n_C%E1%BA%A7u_Tr%E1%BA%AFng%2C_K%C3%AAnh_n%C6%B0%E1%BB%9Bc_%C4%91en_%281%29.jpg",
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
    "title": "Chả cá Lã Vọng",
    "description": "Chả cá lăng nướng ăn bún.",
    "cook_time": 45,
    "servings": 3,
    "cost": 120000,
    "calories": 380,
    "protein": 32,
    "fat": 20,
    "fiber": 2,
    "carbs": 20,
    "category": "Bữa tối",
    "tags": [
      "Chả cá"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Ch%E1%BA%A3_c%C3%A1_L%C3%A3_V%E1%BB%8Dng_H%C3%A0_N%E1%BB%99i_th%C3%A1ng_2_n%C4%83m_2018_%281%29.jpg/330px-Ch%E1%BA%A3_c%C3%A1_L%C3%A3_V%E1%BB%8Dng_H%C3%A0_N%E1%BB%99i_th%C3%A1ng_2_n%C4%83m_2018_%281%29.jpg",
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
    "title": "Chè",
    "description": "Chè đậu ninh nhừ thanh mát.",
    "cook_time": 60,
    "servings": 4,
    "cost": 20000,
    "calories": 180,
    "protein": 6,
    "fat": 1,
    "fiber": 6,
    "carbs": 40,
    "category": "Tráng miệng",
    "tags": [
      "Chè"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/S%E1%BB%91ng_l%C6%B0ng_kh%E1%BB%A7ng_long_T%C3%A0_X%C3%B9a.jpg/330px-S%E1%BB%91ng_l%C6%B0ng_kh%E1%BB%A7ng_long_T%C3%A0_X%C3%B9a.jpg",
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
    "title": "Bò lúc lắc",
    "description": "Thịt thăn bò xào bơ tỏi.",
    "cook_time": 20,
    "servings": 2,
    "cost": 100000,
    "calories": 420,
    "protein": 38,
    "fat": 22,
    "fiber": 2,
    "carbs": 14,
    "category": "Bữa chính",
    "tags": [
      "Bò"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Product_Shots_of_Food-Bo_Luc_Lac.jpg/330px-Product_Shots_of_Food-Bo_Luc_Lac.jpg",
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
    "title": "Bánh bèo",
    "description": "Bánh bèo chén Huế tôm chấy.",
    "cook_time": 45,
    "servings": 3,
    "cost": 35000,
    "calories": 220,
    "protein": 8,
    "fat": 10,
    "fiber": 1,
    "carbs": 28,
    "category": "Khai vị",
    "tags": [
      "Bánh"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/B%C3%A1nh_b%C3%A8o.jpg/330px-B%C3%A1nh_b%C3%A8o.jpg",
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
    "title": "Cơm chiên",
    "description": "Cơm chiên dương châu thập cẩm.",
    "cook_time": 20,
    "servings": 2,
    "cost": 40000,
    "calories": 520,
    "protein": 22,
    "fat": 18,
    "fiber": 3,
    "carbs": 68,
    "category": "Bữa trưa",
    "tags": [
      "Cơm"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Fried_rice_with_chicken_%2817234644521%29.jpg/330px-Fried_rice_with_chicken_%2817234644521%29.jpg",
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
    "title": "Sinh tố",
    "description": "Sinh tố bơ xay nhuyễn.",
    "cook_time": 5,
    "servings": 2,
    "cost": 25000,
    "calories": 320,
    "protein": 4,
    "fat": 22,
    "fiber": 6,
    "carbs": 28,
    "category": "Đồ uống",
    "tags": [
      "Sinh tố"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Crystals_of_vitamin_C.jpg/330px-Crystals_of_vitamin_C.jpg",
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
    "title": "Bún riêu cua",
    "description": "Bún riêu cua đồng đậu hũ.",
    "cook_time": 60,
    "servings": 4,
    "cost": 70000,
    "calories": 360,
    "protein": 22,
    "fat": 12,
    "fiber": 3,
    "carbs": 45,
    "category": "Bữa sáng",
    "tags": [
      "Bún"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/B%C3%BAn_ri%C3%AAu_cua_n%C6%B0%E1%BB%9Bc.jpg/330px-B%C3%BAn_ri%C3%AAu_cua_n%C6%B0%E1%BB%9Bc.jpg",
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
    "description": "Rau muống xanh giòn phi tỏi thơm.",
    "cook_time": 10,
    "servings": 2,
    "cost": 15000,
    "calories": 80,
    "protein": 4,
    "fat": 6,
    "fiber": 3,
    "carbs": 8,
    "category": "Rau củ",
    "tags": [
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
  },
  {
    "title": "Bánh cuốn",
    "description": "Bánh cuốn nhân thịt nấm mèo.",
    "cook_time": 30,
    "servings": 2,
    "cost": 35000,
    "calories": 300,
    "protein": 14,
    "fat": 8,
    "fiber": 3,
    "carbs": 46,
    "category": "Bữa sáng",
    "tags": [
      "Bánh"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Banh_cuon.jpg/330px-Banh_cuon.jpg",
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
    "title": "Nem rán",
    "description": "Nem rán Hà Nội vàng rụm.",
    "cook_time": 45,
    "servings": 4,
    "cost": 60000,
    "calories": 500,
    "protein": 22,
    "fat": 30,
    "fiber": 3,
    "carbs": 35,
    "category": "Bữa chính",
    "tags": [
      "Nem"
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
    "title": "Bánh xèo",
    "description": "Bánh xèo miền Tây vỏ giòn nhân tôm.",
    "cook_time": 25,
    "servings": 3,
    "cost": 40000,
    "calories": 450,
    "protein": 18,
    "fat": 20,
    "fiber": 4,
    "carbs": 50,
    "category": "Bữa chính",
    "tags": [
      "Bánh xèo"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/B%C3%A1nh_x%C3%A8o_with_n%C6%B0%E1%BB%9Bc_m%E1%BA%AFm.jpg/330px-B%C3%A1nh_x%C3%A8o_with_n%C6%B0%E1%BB%9Bc_m%E1%BA%AFm.jpg",
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
    "title": "Bò kho",
    "description": "Bò kho sả ớt hầm mềm.",
    "cook_time": 120,
    "servings": 4,
    "cost": 85000,
    "calories": 550,
    "protein": 40,
    "fat": 25,
    "fiber": 5,
    "carbs": 10,
    "category": "Bữa chính",
    "tags": [
      "Bò"
    ],
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Bo_kho_mien_Bac.jpg/330px-Bo_kho_mien_Bac.jpg",
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
  {"title":"Menu theo tiêu chuẩn dinh dưỡng","description":"Thực đơn tiết kiệm thời gian","author_name":"Bảo Lam","rating":5.0,"rating_count":299,"image_url":"https://images.unsplash.com/photo-1598514983318-2f64f8f4796c?w=600","recipe_text":"Kiểm tra ngay tab công thức nhé"}
]

def seed():
    with app.app_context():
        Recipe.query.delete()
        CommunityPost.query.delete()
        db.session.commit()

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
            db.session.add(recipe)

        for post_data in COMMUNITY_POSTS:
            post = CommunityPost(**post_data)
            db.session.add(post)

        db.session.commit()

if __name__ == "__main__":
    seed()
