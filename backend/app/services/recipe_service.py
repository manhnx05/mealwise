from .. import db
from ..models import Recipe


RECIPE_FIELDS = ['title', 'description', 'image_url', 'video_url', 'cook_time',
                 'servings', 'cost', 'calories', 'protein', 'fat', 'fiber',
                 'carbs', 'category', 'ingredients', 'steps', 'tags']


def get_all(category=None, search=None):
    query = Recipe.query
    if category:
        query = query.filter_by(category=category)
    if search:
        query = query.filter(Recipe.title.ilike(f'%{search}%'))
    return query.order_by(Recipe.created_at.desc()).all()


def get_by_id(recipe_id):
    return Recipe.query.get_or_404(recipe_id)


def create(data: dict):
    recipe = Recipe(**{k: data.get(k) for k in RECIPE_FIELDS})
    recipe.ingredients = data.get('ingredients', [])
    recipe.steps = data.get('steps', [])
    recipe.tags = data.get('tags', [])
    db.session.add(recipe)
    db.session.commit()
    return recipe


def update(recipe_id, data: dict):
    recipe = get_by_id(recipe_id)
    for field in RECIPE_FIELDS:
        if field in data:
            setattr(recipe, field, data[field])
    db.session.commit()
    return recipe


def delete(recipe_id):
    recipe = get_by_id(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
