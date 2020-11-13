from django.urls import path


from .import views
urlpatterns = [
    path('', views.index , name='index'),
    path('singup/', views.singup , name='singup'),
    path('login', views.login , name='login'),
    path('logout', views.logout , name='logout'),
    path('cart', views.cart , name='cart'),
    path('checkout', views.checkout , name='checkout'),
    path('order', views.order , name='order'),
]