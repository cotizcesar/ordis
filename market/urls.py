"""ordis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

# userprofile: Importing Views
from .views import Market, MarketWarframe, MarketWeapon, MarketSentinel, MarketBeast, OrderCreateView, OrderBeastCreateView #ItemDetail,

urlpatterns = [
    path('market/', Market.as_view(), name='market'),
    path('market/warframe', MarketWarframe.as_view(), name='market_warframe'),
    path('market/weapon', MarketWeapon.as_view(), name='market_weapon'),
    path('market/sentinel', MarketSentinel.as_view(), name='market_sentinel'),
    path('market/beast', MarketBeast.as_view(), name='market_beast'),
    path('market/order/create', OrderCreateView.as_view(), name='order_create'),
    path('market/order/beast/create', OrderBeastCreateView.as_view(), name='order_beast_create'),
    #url(r'market/items/(?P<slug>[-\w]+)$', ItemDetail.as_view(), name='item_detail'),
]