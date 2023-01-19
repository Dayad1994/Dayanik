
from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.dayanik, name='dayanik'),
    path('blog/', views.index, name='index'),
    path('new/', views.PostCreateView.as_view(), name='new_post')
]
