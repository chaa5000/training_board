from django.urls import path, include # أضف include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
        # أضف هذا السطر وتأكد أن الاسم هو 'register' ليطابق ما كتبته في القالب
    path('signup/', views.signup, name='register'), 
    path('accounts/', include('django.contrib.auth.urls')), # روابط تسجيل الدخول الجاهزة
    path('logout/', views.user_logout, name='logout'),
]