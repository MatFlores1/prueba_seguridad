from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(template_name = 'index.html'), name = 'logout'),
    path('', views.index, name = 'index'),
    

]