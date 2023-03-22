from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_function, name='login'),
    path('register/', views.register, name='register'),
    path('user/', views.pagina_inicial, name='pagina_inicial')
]
