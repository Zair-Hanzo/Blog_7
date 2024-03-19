from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.home, name='home'),
    path('blogposts/', views.blogposts, name='blogposts'),
    path('blogposts/<int:blogpost_id>/', views.blogpost, name='blogpost'),
    path('new_blogpost/', views.new_blogpost, name='new_blogpost'),
    path('new_blogtext/<int:blogpost_id>/', views.new_blogtext, name='new_blogtext'),
    path('edit_blogtext/<int:blogtext_id>/', views.edit_blogtext, name='edit_blogtext')
]