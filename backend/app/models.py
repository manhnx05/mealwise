from . import db
from datetime import datetime


class Recipe(db.Model):
    """Bảng lưu các công thức nấu ăn"""
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    image_url = db.Column(db.Text)
    video_url = db.Column(db.Text)
    cook_time = db.Column(db.Integer)        # phút
    servings = db.Column(db.Integer)
    cost = db.Column(db.Numeric(12, 0))      # VNĐ
    calories = db.Column(db.Integer)
    protein = db.Column(db.Numeric(6, 1))
    fat = db.Column(db.Numeric(6, 1))
    fiber = db.Column(db.Numeric(6, 1))
    carbs = db.Column(db.Numeric(6, 1))
    category = db.Column(db.String(50))      # quick_meal, low_fat, ...
    ingredients = db.Column(db.JSON, default=list)  # [{name, amount, calories, cost}]
    steps = db.Column(db.JSON, default=list)        # [{step_number, instruction, image_url}]
    tags = db.Column(db.JSON, default=list)         # ["Bữa sáng", "Chay", ...]
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'image_url': self.image_url,
            'video_url': self.video_url,
            'cook_time': self.cook_time,
            'servings': self.servings,
            'cost': float(self.cost) if self.cost else None,
            'calories': self.calories,
            'protein': float(self.protein) if self.protein else None,
            'fat': float(self.fat) if self.fat else None,
            'fiber': float(self.fiber) if self.fiber else None,
            'carbs': float(self.carbs) if self.carbs else None,
            'category': self.category,
            'ingredients': self.ingredients or [],
            'steps': self.steps or [],
            'tags': self.tags or [],
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }


class MealPlan(db.Model):
    """Bảng lưu thực đơn tuần"""
    __tablename__ = 'meal_plans'

    id = db.Column(db.Integer, primary_key=True)
    week_start = db.Column(db.Date, nullable=False)
    meals = db.Column(db.JSON, default=list)        # [{day, breakfast, lunch, dinner}]
    shopping_list = db.Column(db.JSON, default=list) # [{name, amount, checked}]
    total_cost = db.Column(db.Numeric(12, 0))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'week_start': self.week_start.isoformat() if self.week_start else None,
            'meals': self.meals or [],
            'shopping_list': self.shopping_list or [],
            'total_cost': float(self.total_cost) if self.total_cost else 0,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }


class CommunityPost(db.Model):
    """Bảng lưu bài đăng cộng đồng"""
    __tablename__ = 'community_posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    image_url = db.Column(db.Text)
    recipe_text = db.Column(db.Text)
    rating = db.Column(db.Numeric(3, 2), default=0)
    rating_count = db.Column(db.Integer, default=0)
    author_name = db.Column(db.String(100))
    comments = db.Column(db.JSON, default=list)  # [{author, text, date}]
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'image_url': self.image_url,
            'recipe_text': self.recipe_text,
            'rating': float(self.rating) if self.rating else 0,
            'rating_count': self.rating_count or 0,
            'author_name': self.author_name,
            'comments': self.comments or [],
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }


class SavedRecipe(db.Model):
    """Bảng lưu công thức yêu thích của người dùng"""
    __tablename__ = 'saved_recipes'

    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    recipe = db.relationship('Recipe', backref='saves', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'recipe_id': self.recipe_id,
            'recipe': self.recipe.to_dict() if self.recipe else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }
