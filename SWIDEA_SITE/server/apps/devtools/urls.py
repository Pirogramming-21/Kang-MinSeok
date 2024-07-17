from django.urls import path
from .views import *

app_name = 'devtools'

urlpatterns = [
    path('manage/', dev_list, name='manage'),
    path('create/', dev_create, name='create'),
    path('detail/<int:pk>', detail, name='detail'),
    path('edit/<int:pk>', edit, name='edit'),
    path('delete/<int:pk>', delete, name='delete'),
]