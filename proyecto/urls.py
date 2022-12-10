from django.urls import path
from django.contrib.auth.views import LoginView, logout_then_login
from . import views

urlpatterns=[
    path('portfolio/', views.index.as_view(), name="index"),
    path('portfolio/accounts/login/', LoginView.as_view(), name="login"),
    path('portfolio/accounts/register/', views.RegisterView.as_view(), name='register'),
    path('portfolio/project/register', views.RegisterProjectView.as_view(), name='registerProject'),
    path('portfolio/logout/', logout_then_login, name='logout'),
    path('portfolio/contact/', views.email.as_view(), name='email'),
    path('portfolio/project/<int:id>/details/', views.detailsOneProject, name='detailsOne'),
]