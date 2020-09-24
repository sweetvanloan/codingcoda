from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('javascript/', views.javascript, name='javascript'),
    path('python/', views.python, name='python'),
    path('ruby/', views.ruby, name='ruby'),
    path('css/', views.css, name='css'),
]