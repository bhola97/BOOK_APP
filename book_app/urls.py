from django.urls import path
from book_app.views import sign_up, sell
from book_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sign_up/', sign_up.as_view(), name='sign_up'),
    path('loginpage/', views.loginpage, name='loginpage'),
    path('logoutpage/', views.logoutpage, name='logoutpage'),
    path('sell/',views.sell, name="sell"),
    path('sellformcreated/',views.sellformcreated, name="sellformcreated"),
    path('borrow/', views.borrow, name='borrow'),
    path('book_detail/<uuid>', views.book_detail, name='book_detail'),
    path('carty/', views.cartss, name="cartss"),
    path('cart/<uuid>', views.add_to_cart, name="add_to_cart"),
    path("searched/", views.search, name="search"),
    path('cart/<pk>/delete', views.delete_from_cart.as_view(), name="delete_from_cart"),
    path('ads/', views.ads, name='ads'),

]
