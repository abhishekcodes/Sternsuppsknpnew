from django.conf.urls import url

from .views import (
    ProductListView,
    #product_list_view,
    #ProductDetailView,
    #product_detail_view,
    #ProductFeaturedListView,
    #ProductFeaturedDetailListView,
    ProductDetailSlugView
    )
app_name = 'products'

urlpatterns = [
    url(r'',ProductListView.as_view(), name='list'),
    url(r'<slug:slug>/',ProductDetailSlugView.as_view(), name='detail'),
]

