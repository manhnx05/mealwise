from .. import db
from ..models import CommunityPost, SavedRecipe

POST_FIELDS = ['title', 'description', 'image_url', 'recipe_text',
               'author_name', 'rating', 'rating_count', 'comments']


# ── Community Posts ──────────────────────────────────────────

def get_all_posts():
    return CommunityPost.query.order_by(CommunityPost.created_at.desc()).all()


def create_post(data: dict):
    post = CommunityPost(
        title=data.get('title'),
        description=data.get('description'),
        image_url=data.get('image_url'),
        recipe_text=data.get('recipe_text'),
        author_name=data.get('author_name', 'Ẩn danh'),
        rating=data.get('rating', 0),
        rating_count=data.get('rating_count', 0),
        comments=data.get('comments', []),
    )
    db.session.add(post)
    db.session.commit()
    return post


def update_post(post_id, data: dict):
    post = CommunityPost.query.get_or_404(post_id)
    for field in POST_FIELDS:
        if field in data:
            setattr(post, field, data[field])
    db.session.commit()
    return post


def delete_post(post_id):
    post = CommunityPost.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()


# ── Saved Recipes ─────────────────────────────────────────────

def get_saved():
    return SavedRecipe.query.order_by(SavedRecipe.created_at.desc()).all()


def save_recipe(recipe_id: int):
    existing = SavedRecipe.query.filter_by(recipe_id=recipe_id).first()
    if existing:
        return existing, False  # (record, created)
    saved = SavedRecipe(recipe_id=recipe_id)
    db.session.add(saved)
    db.session.commit()
    return saved, True


def unsave_recipe(recipe_id: int):
    saved = SavedRecipe.query.filter_by(recipe_id=recipe_id).first_or_404()
    db.session.delete(saved)
    db.session.commit()
