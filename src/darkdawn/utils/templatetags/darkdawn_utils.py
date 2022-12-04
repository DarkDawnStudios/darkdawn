from datetime import datetime
from django import template

from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def copyright_text(from_year):
    from_year = int(from_year)
    year = datetime.now().year
    if from_year == year:
        return f"© {year} Dark Dawn Studios"
    if from_year < year:
        return f"© {from_year}-{year} Dark Dawn Studios"
    if from_year > year:
        return f"© {from_year} Dark Dawn Studios"
