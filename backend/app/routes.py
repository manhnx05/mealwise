import base64
from flask import Blueprint, request, jsonify
from .services import recipe_service, meal_plan_service, community_service
from .services.ai_service import invoke_gemini

bp = Blueprint('api', __name__, url_prefix='/api')


# ── HEALTH CHECK ──────────────────────────────────────────────
@bp.route('/ping', methods=['GET'])
def ping():
    return jsonify({'status': 'ok', 'message': 'MealWise Backend đang hoạt động!'})


# ── RECIPES ───────────────────────────────────────────────────
@bp.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = recipe_service.get_all(
        category=request.args.get('category'),
        search=request.args.get('search', '')
    )
    return jsonify([r.to_dict() for r in recipes])


@bp.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    return jsonify(recipe_service.get_by_id(recipe_id).to_dict())


@bp.route('/recipes', methods=['POST'])
def create_recipe():
    recipe = recipe_service.create(request.json)
    return jsonify(recipe.to_dict()), 201


@bp.route('/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    recipe = recipe_service.update(recipe_id, request.json)
    return jsonify(recipe.to_dict())


@bp.route('/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    recipe_service.delete(recipe_id)
    return jsonify({'message': 'Đã xoá công thức'}), 200


# ── MEAL PLANS ────────────────────────────────────────────────
@bp.route('/meal-plans', methods=['GET'])
def get_meal_plans():
    return jsonify([p.to_dict() for p in meal_plan_service.get_all()])


@bp.route('/meal-plans/latest', methods=['GET'])
def get_latest_plan():
    plan = meal_plan_service.get_latest()
    return jsonify(plan.to_dict() if plan else None)


@bp.route('/meal-plans', methods=['POST'])
def create_meal_plan():
    plan = meal_plan_service.create(request.json)
    return jsonify(plan.to_dict()), 201


@bp.route('/meal-plans/<int:plan_id>', methods=['PUT'])
def update_meal_plan(plan_id):
    plan = meal_plan_service.update(plan_id, request.json)
    return jsonify(plan.to_dict())


@bp.route('/meal-plans/<int:plan_id>', methods=['DELETE'])
def delete_meal_plan(plan_id):
    meal_plan_service.delete(plan_id)
    return jsonify({'message': 'Đã xoá thực đơn'}), 200


# ── COMMUNITY POSTS ───────────────────────────────────────────
@bp.route('/community', methods=['GET'])
def get_posts():
    return jsonify([p.to_dict() for p in community_service.get_all_posts()])


@bp.route('/community', methods=['POST'])
def create_post():
    post = community_service.create_post(request.json)
    return jsonify(post.to_dict()), 201


@bp.route('/community/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = community_service.update_post(post_id, request.json)
    return jsonify(post.to_dict())


@bp.route('/community/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    community_service.delete_post(post_id)
    return jsonify({'message': 'Đã xoá bài đăng'}), 200


# ── SAVED RECIPES ─────────────────────────────────────────────
@bp.route('/saved-recipes', methods=['GET'])
def get_saved():
    return jsonify([s.to_dict() for s in community_service.get_saved()])


@bp.route('/saved-recipes', methods=['POST'])
def save_recipe():
    recipe_id = request.json.get('recipe_id')
    saved, created = community_service.save_recipe(recipe_id)
    msg = 'Đã lưu' if created else 'Đã lưu rồi'
    return jsonify({'message': msg, 'data': saved.to_dict()}), 201 if created else 200


@bp.route('/saved-recipes/<int:recipe_id>', methods=['DELETE'])
def unsave_recipe(recipe_id):
    community_service.unsave_recipe(recipe_id)
    return jsonify({'message': 'Đã bỏ lưu'}), 200


# ── AI & UPLOAD ───────────────────────────────────────────────
@bp.route('/generate-meal-plan', methods=['POST'])
def generate_ai_meal_plan():
    data = request.json or {}
    try:
        result = invoke_gemini(
            prompt=data.get('prompt', ''),
            json_schema=data.get('response_json_schema')
        )
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    file_content = file.read()
    b64_str = base64.b64encode(file_content).decode('utf-8')
    data_url = f"data:{file.mimetype};base64,{b64_str}"
    return jsonify({'file_url': data_url}), 200
