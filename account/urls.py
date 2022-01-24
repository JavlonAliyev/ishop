from rest_framework.authtoken import views
from django.urls import path
from .views import MeView

app_name = 'account'
urlpatterns = [
    path('auth/', views.obtain_auth_token, name="auth"),
    path('me/', MeView.as_view(), name="me")
]