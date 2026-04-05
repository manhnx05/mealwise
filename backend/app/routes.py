from flask import Blueprint, request, jsonify
from . import db
from .models import Recipe, MealPlan, CommunityPost, SavedRecipe

bp = Blueprint('api', __name__, url_prefix='/api')


# ──────────────────────── HEALTH CHECK ────────────────────────
@bp.route('/ping', methods=['GET'])
def ping():
    return jsonify({'status': 'ok', 'message': 'MealWise Backend đang hoạt động!'})


# ──────────────────────── RECIPES ───────────────────────────
@bp.route('/recipes', methods=['GET'])
def get_recipes():
    category = request.args.get('category')
    search = request.args.get('search', '')
    query = Recipe.query
    if category:
        query = query.filter_by(category=category)
    if search:
        query = query.filter(Recipe.title.ilike(f'%{search}%'))
    recipes = query.order_by(Recipe.created_at.desc()).all()
    return jsonify([r.to_dict() for r in recipes])


@bp.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return jsonify(recipe.to_dict())


@bp.route('/recipes', methods=['POST'])
def create_recipe():
    data = request.json
    recipe = Recipe(
        title=data.get('title'),
        description=data.get('description'),
        image_url=data.get('image_url'),
        video_url=data.get('video_url'),
        cook_time=data.get('cook_time'),
        servings=data.get('servings'),
        cost=data.get('cost'),
        calories=data.get('calories'),
        protein=data.get('protein'),
        fat=data.get('fat'),
        fiber=data.get('fiber'),
        carbs=data.get('carbs'),
        category=data.get('category'),
        ingredients=data.get('ingredients', []),
        steps=data.get('steps', []),
        tags=data.get('tags', []),
    )
    db.session.add(recipe)
    db.session.commit()
    return jsonify(recipe.to_dict()), 201


@bp.route('/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    data = request.json
    for field in ['title', 'description', 'image_url', 'video_url', 'cook_time',
                  'servings', 'cost', 'calories', 'protein', 'fat', 'fiber',
                  'carbs', 'category', 'ingredients', 'steps', 'tags']:
        if field in data:
            setattr(recipe, field, data[field])
    db.session.commit()
    return jsonify(recipe.to_dict())


@bp.route('/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    return jsonify({'message': 'Đã xoá công thức'}), 200


# ──────────────────────── MEAL PLANS ────────────────────────
@bp.route('/meal-plans', methods=['GET'])
def get_meal_plans():
    plans = MealPlan.query.order_by(MealPlan.created_at.desc()).all()
    return jsonify([p.to_dict() for p in plans])


@bp.route('/meal-plans/latest', methods=['GET'])
def get_latest_plan():
    plan = MealPlan.query.order_by(MealPlan.created_at.desc()).first()
    if not plan:
        return jsonify(None)
    return jsonify(plan.to_dict())


@bp.route('/meal-plans', methods=['POST'])
def create_meal_plan():
    data = request.json
    plan = MealPlan(
        week_start=data.get('week_start'),
        meals=data.get('meals', []),
        shopping_list=data.get('shopping_list', []),
        total_cost=data.get('total_cost', 0),
    )
    db.session.add(plan)
    db.session.commit()
    return jsonify(plan.to_dict()), 201


@bp.route('/meal-plans/<int:plan_id>', methods=['PUT'])
def update_meal_plan(plan_id):
    plan = MealPlan.query.get_or_404(plan_id)
    data = request.json
    for field in ['week_start', 'meals', 'shopping_list', 'total_cost']:
        if field in data:
            setattr(plan, field, data[field])
    db.session.commit()
    return jsonify(plan.to_dict())


@bp.route('/meal-plans/<int:plan_id>', methods=['DELETE'])
def delete_meal_plan(plan_id):
    plan = MealPlan.query.get_or_404(plan_id)
    db.session.delete(plan)
    db.session.commit()
    return jsonify({'message': 'Đã xoá thực đơn'}), 200


# ──────────────────────── COMMUNITY POSTS ────────────────────
@bp.route('/community', methods=['GET'])
def get_posts():
    posts = CommunityPost.query.order_by(CommunityPost.created_at.desc()).all()
    return jsonify([p.to_dict() for p in posts])


@bp.route('/community', methods=['POST'])
def create_post():
    data = request.json
    post = CommunityPost(
        title=data.get('title'),
        description=data.get('description'),
        image_url=data.get('image_url'),
        recipe_text=data.get('recipe_text'),
        author_name=data.get('author_name'),
        rating=data.get('rating', 0),
        rating_count=data.get('rating_count', 0),
        comments=data.get('comments', []),
    )
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_dict()), 201


@bp.route('/community/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = CommunityPost.query.get_or_404(post_id)
    data = request.json
    for field in ['title', 'description', 'image_url', 'recipe_text',
                  'author_name', 'rating', 'rating_count', 'comments']:
        if field in data:
            setattr(post, field, data[field])
    db.session.commit()
    return jsonify(post.to_dict())


@bp.route('/community/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = CommunityPost.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({'message': 'Đã xoá bài đăng'}), 200


# ──────────────────────── SAVED RECIPES ─────────────────────
@bp.route('/saved-recipes', methods=['GET'])
def get_saved():
    saves = SavedRecipe.query.order_by(SavedRecipe.created_at.desc()).all()
    return jsonify([s.to_dict() for s in saves])


@bp.route('/saved-recipes', methods=['POST'])
def save_recipe():
    data = request.json
    recipe_id = data.get('recipe_id')
    # Tránh lưu trùng
    existing = SavedRecipe.query.filter_by(recipe_id=recipe_id).first()
    if existing:
        return jsonify({'message': 'Đã lưu rồi', 'data': existing.to_dict()}), 200
    saved = SavedRecipe(recipe_id=recipe_id)
    db.session.add(saved)
    db.session.commit()
    return jsonify(saved.to_dict()), 201


@bp.route('/saved-recipes/<int:recipe_id>', methods=['DELETE'])
def unsave_recipe(recipe_id):
    saved = SavedRecipe.query.filter_by(recipe_id=recipe_id).first_or_404()
    db.session.delete(saved)
    db.session.commit()
    return jsonify({'message': 'Đã bỏ lưu'}), 200
