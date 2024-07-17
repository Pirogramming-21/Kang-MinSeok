from django.db import models
from apps.devtools.models import DevTool
# Create your models here.
class Idea(models.Model):
    title = models.CharField('제목', max_length=30)
    image = models.ImageField('이미지', blank=True, upload_to='ideas/%Y%m%d')
    content = models.TextField('설명')
    interest = models.IntegerField('관심도')
    devtool = models.ForeignKey(DevTool, on_delete=models.CASCADE, related_name="idea", verbose_name='개발도구' ,null=True)

    def __str__(self):
        return self.devtool
