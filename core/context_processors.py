def external_data(request):
    # Django: Importing User Model
    from django.contrib.auth.models import User
    # Market: Importing Item Model
    from market.models import Item, Order
    return {
        'omnisearch': Item.objects.all().values('name', 'slug'),
        'user_count': Item.objects.all().count(),
        'selling_count': Order.objects.filter(want='S').exclude(is_active=False).count(),
        'buying_count': Order.objects.filter(want='S').exclude(is_active=False).count()
    }