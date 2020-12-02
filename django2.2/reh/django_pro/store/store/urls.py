"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from accounts.views import BlogView,IndexPageView,about,contact
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import *
# from products.views import product,vegetables,all_product
# from cart.views import add_to_cart,remove_from_cart,view_cart
# from order.views import checkout,orders
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexPageView, name='index'),
    path('aboutus/', about, name='about'),
    path('contact-us/', contact, name='contact'),
    path('our-blog/', BlogView, name='blog'),
   


    path('i18n/', include('django.conf.urls.i18n')),

    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('carts.urls')),
   
    # # path('p/',products.views.home, name='home'),
    # url(r'products/(?P<slug>[^\/]+)\/add', add_to_cart, name='add_to_cart'),
    # url(r'products/(?P<id>\d+)\/remove', remove_from_cart,name='remove_from_cart'),
    # path('products/(?P<slug>[^\/]+)\/?', detail, name='detail'),
    # path('products/', product.views.all, name='all'),
    # path('cart/', view_cart, name='view_cart'),
    # path('checkout/', checkout, name='checkout'),
    # path('orders/', orders, name='orders'),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)