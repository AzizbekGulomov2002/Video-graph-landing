from django import template

register = template.Library()

@register.filter
def distinct_by_type(portfolios):
    """Returns distinct portfolio type names."""
    seen = set()
    unique_types = []
    for portfolio in portfolios:
        type_name = portfolio.type.name
        if type_name not in seen:
            seen.add(type_name)
            unique_types.append(type_name)
    return unique_types
