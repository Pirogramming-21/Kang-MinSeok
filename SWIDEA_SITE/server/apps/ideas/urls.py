from django.urls import path
from .views import *

app_name = 'ideas'

urlpatterns = [
  path('', main, name='main'),
  path('create/', create, name='create'),
  path('detail/<int:pk>', detail, name='detail'),
  path('edit/<int:pk>', edit, name='edit'),
  path('delete/<int:pk>', delete, name='delete'),
]