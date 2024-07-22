from django.urls import path
from .views import *

app_name = 'pirosta'

urlpatterns = [
    path("", login, name="login"), # 시작 화면
    path("signup/", signup, name="signup"), # 회원가입
    path("logout/", logout, name="logout"), # 로그아웃
    path("posts/", posts, name="posts"), # 게시물 화면
    path("create_post/", create_post, name="create_post"), # 게시물 화면
    path('like_ajax/', like_ajax, name='like_ajax'),
    path('comment_ajax/', comment_ajax, name='comment_ajax'),
    path('delete_comment_ajax/', delete_comment_ajax, name='delete_comment_ajax'),
]