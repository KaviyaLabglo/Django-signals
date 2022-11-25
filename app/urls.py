from django.urls import path
from app import views

urlpatterns = [
    path('',views.register, name='register'),
    path('pro/', views.profile, name='pro'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    
   
    
]

