from . import views
from django.urls import path, include

urlpatterns = [
    path("", views.dash, name='dash'),
    path("category", views.category, name='category'),
    path("cart", views.cart, name='cart'),
    path("viewprod/<int:pk>/<cat>", views.prodview, name='viewproduct'),
    path("bookorder", views.book, name='bookorder'),
    path("createuser", views.signup, name='signup'),
    path("loginuser", views.handlelogin, name='login'),
    path("logoutuser", views.handlelogout, name='logout'),
    path("additem", views.additem, name='additem'),
    path("managecookie/<pk>", views.managecookie, name='managecookie'),
    path("category/<pk>", views.category, name='category'),
    path("category/<page>", views.category, name='category'),
     path("searchprod", views.search, name='search'),
]
