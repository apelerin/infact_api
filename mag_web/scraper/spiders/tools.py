import api.models
from api.models import Category


def match_category(category):
    try:
        db_category = Category.objects.get(match__contains=[category])
    except api.models.Category.DoesNotExist:
        return
    return db_category
