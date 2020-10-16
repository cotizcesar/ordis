from django import template

register = template.Library()


@register.simple_tag
def url_replace(request, field, value):
    #! Source: https://medium.com/@sumitlni/paginate-properly-please-93e7ca776432
    query_string = request.GET.copy()
    query_string[field] = value

    return query_string.urlencode()