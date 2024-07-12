from django.urls import path
from .views import *

app_name = 'movie'

urlpatterns = [
    path('', movie_list), #리뷰 리스트
    path('/<int:pk>', review_detail), #리뷰 디테일 페이지
    path('/create_review', review_create), # 리뷰 작성 페이지
    path('/<int:pk>/edit', review_edit), # 리뷰 수정 페이지
    path('/<int:pk>/delete', review_delete) # 리뷰 수정 페이지
]