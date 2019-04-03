from django.urls import path,include
from .views import home, about
from users import views as user_views



urlpatterns = [
    path('', home, name='blog-home'),
    path('about/', about, name='blog-about'),
    path('register/', user_views.register, name='register'),

]