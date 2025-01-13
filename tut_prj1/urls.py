"""
URL configuration for tut_prj1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path , include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_views.register, name='register'),
    path('reset_password/', 
         auth_views.PasswordResetView.as_view(template_name = "users/reset_pass.html"), 
         name ='reset_password'
         ),
    path('reset_password_sent/', 
         auth_views.PasswordResetDoneView.as_view(template_name = "users/pass_reset_sent.html"),
         name ='password_reset_done'
         ),
    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name = "users/pass_reset_form.html"), 
         name ='password_reset_confirm'
         ),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name = "users/pass_reset_done.html"), 
         name ='password_reset_complete'
         ),
    path('profile/', user_views.profile_update, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/mylogout.html'), name='mylogout'),
    # path('logout/', user_views.blog_logout, name='logout'),
    path('', include('blogapp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    