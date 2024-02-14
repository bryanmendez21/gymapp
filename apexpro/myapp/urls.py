from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

#--PATHS TO PAGES--
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name ='home'),
    path('register/', views.register, name='register'),
    path('', views.Custom_login, name ='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('account/', views.account_view, name='account'),
    path('activity/', views.activity_view, name='activity'),
    path('diet/', views.diet_view, name='diet'),
    path('composition/', views.composition_view, name='composition'),
    path('routine/', views.routine_view, name='routine'),
    ]
