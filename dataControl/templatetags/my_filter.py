from django import template
register = template.Library()
@register.filter
def ValueToStr(value):
    if value == "" or value is None:
        return "暂无信息"
    else:
        return value