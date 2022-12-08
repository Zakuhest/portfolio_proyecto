from django.urls import path
from django.contrib.auth.views import LoginView, logout_then_login
from . import views

urlpatterns=[
    path('', views.index.as_view(), name="index"),
    path('accounts/login/', LoginView.as_view(), name="login"),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('registerProject/', views.RegisterProjectView.as_view(), name='registerProject'),
    path('logout/', logout_then_login, name='logout'),
    path('contact/', views.email.as_view(), name='email')
]