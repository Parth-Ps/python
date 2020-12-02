from django.conf.urls import url

from .views import ProductListView,CategoryListView,CategoryDetail,ProductDetailView,VariationListView
app_name='products'
urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='product_list'),
    url(r'^categories/$', CategoryListView.as_view(), name='category_list'),
    url(r'^categories/(?P<slug>[\w-]+)/$', CategoryDetail.as_view(), name='category_detail'),
    url(r'^(?P<id>[\w-]+)/$', ProductDetailView.as_view(), name='product_detail'),
    url(r'^(?P<id>[\w-]+)/variation/?', VariationListView.as_view(), name='variation_list'),
]
