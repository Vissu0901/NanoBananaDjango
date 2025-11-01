from django.urls import path
from .views import signup, login, api_root

urlpatterns = [
    path('', api_root),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
]
