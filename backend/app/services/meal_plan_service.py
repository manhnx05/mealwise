from .. import db
from ..models import MealPlan

PLAN_FIELDS = ['week_start', 'meals', 'shopping_list', 'total_cost']


def get_all():
    return MealPlan.query.order_by(MealPlan.created_at.desc()).all()


def get_latest():
    return MealPlan.query.order_by(MealPlan.created_at.desc()).first()


def create(data: dict):
    plan = MealPlan(
        week_start=data.get('week_start'),
        meals=data.get('meals', []),
        shopping_list=data.get('shopping_list', []),
        total_cost=data.get('total_cost', 0),
    )
    db.session.add(plan)
    db.session.commit()
    return plan


def update(plan_id, data: dict):
    plan = MealPlan.query.get_or_404(plan_id)
    for field in PLAN_FIELDS:
        if field in data:
            setattr(plan, field, data[field])
    db.session.commit()
    return plan


def delete(plan_id):
    plan = MealPlan.query.get_or_404(plan_id)
    db.session.delete(plan)
    db.session.commit()
