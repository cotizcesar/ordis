"""ordis-app URL Configuration

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
from .views import Market, ItemDetail, OrderCreateView

urlpatterns = [
    path('market/', Market.as_view(), name='market'),
    path('market/order/create', OrderCreateView.as_view(), name='order_create'),
    url(r'market/items/(?P<slug>[-\w]+)$', ItemDetail.as_view(), name='item_detail'),
]