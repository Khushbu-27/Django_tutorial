
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'blog-home'),
    path('about/',views.about, name = 'blog-about'),
    path('userblogs/',views.userblogs, name = 'blog-userblogs'),
    path('create/', views.create_blog, name='blog-create'),
    path('update/<int:pk>/', views.update_blog, name='update-blog'),
    path('delete/<int:pk>/', views.delete_blog, name='delete-blog'),
]