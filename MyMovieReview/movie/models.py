from django.db import models

# Create your models here.
class Review(models.Model):
    movie_genre = [
            ('액션', '액션 영화'), #db저장되는 내용, 화면에 나오는 내용
            ('범죄', '범죄 영화'),
            ('SF', 'SF 영화'),
            ('코미디', '코미디 영화'),
            ('로맨스', '로맨스 영화'),
            ('스릴러', '스릴러 영화'),
            ('공포', '공포 영화'),
            ('판타지', '판타지 영화'),
            ('멜로', '멜로 영화'),
            ('스포츠', '스포츠 영화'),
            ('뮤지컬', '뮤지컬 영화'),
            ('음악', '음악 영화')
    ]

    title=models.CharField(max_length=30) #제목
    director=models.CharField(max_length=20) #감독
    actor=models.CharField(max_length=20) #주연
    year=models.IntegerField() #개봉년도
    genre=models.CharField(max_length=10, choices=movie_genre) #장르
    rate=models.DecimalField(max_digits=3, decimal_places=1) #별점
    running_time=models.IntegerField() #러닝타임
    content=models.TextField() #리뷰내용

