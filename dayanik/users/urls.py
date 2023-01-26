from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', views.InlogView.as_view(), name='login'),
    path('password_change/', views.PwdChangeView.as_view(),
          name='password_change'),
    path('password_reset/', views.PwdResetView.as_view(),
          name='password_reset'),
    path(
        'reset/<uidb64>/<token>/',
        views.PwdResetConfirmView.as_view(),
        name='password_reset_confirm',
    ),
]
