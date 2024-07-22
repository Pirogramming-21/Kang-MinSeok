from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser): # 유저
    name = models.CharField("이름", max_length=20, null=True)


class Post(models.Model): #게시글
    writer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="writer"
    )
    liked = models.IntegerField('좋아요 개수', default = 0)
    likedUser = models.ManyToManyField(User, related_name="liked_posts", blank=True)
    content = models.TextField('내용')
    photo = photo = models.ImageField('이미지', blank=True, upload_to='pirosta/%Y%m%d')


class Comment(models.Model): #댓글
    content = models.TextField('내용')
    writer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commentWriter"
    )
    postInfo = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="commentPostInfo"
    )
