from django.conf.urls import url

from .views import CartCreateView,CartDetailView,CheckoutView
from orders.views import AddressFormView, UserAddressCreateView, ConfirmOrderView, OrdersList
app_name='cart'
urlpatterns = [
    url(r'^$', CartCreateView.as_view(), name='create_cart'),
    url(r'^view/$', CartDetailView.as_view(), name='cart_detail'),
    url(r'^checkout/$', CheckoutView.as_view(), name='cart_checkout'),
    url(r'^address/$', AddressFormView.as_view(), name='address'),   
    url(r'^address/add/$', UserAddressCreateView.as_view(), name='add_address'),
    url(r'^address/confirm/$', ConfirmOrderView.as_view(), name='confirm_order'),
    url(r'^orders/$', OrdersList.as_view(), name='order_list'),
]
