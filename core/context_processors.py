def omnisearch(request):
    from market.models import Item
    return {'omnisearch': Item.objects.all().values('name', 'slug').order_by('name')}