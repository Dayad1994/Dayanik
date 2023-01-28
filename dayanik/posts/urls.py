
from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('blog/', views.BlogView.as_view(), name='index'),
    path('<str:username>/', views.ProfileView.as_view(), name='profile'),
    path('', views.dayanik, name='dayanik')
]
