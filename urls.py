from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('register_new_admin', views.register_new_admin),
    path('login_current_admin', views.login_current_admin),
    path('shop', views.shop),
    path('shop/product_info', views.product_info),
    path('checkout', views.checkout),
    path('aboutmeandcontact', views.about_me_and_contact),
    path('events', views.events),
    path('admin', views.admin_login),
    path('admin_portal', views.admin_portal)
]