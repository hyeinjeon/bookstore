from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.contrib.auth import get_user_model

# Create your models here.
class Blog(models.Model):
    title = models.CharField('제목', max_length=200)
    writer = models.CharField('작가', max_length=100)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    pub_date = models.DateTimeField('date published')
    body = models.TextField('내용')
    images = models.ImageField('표지', blank=True, upload_to="images", null=True)
    image_thumbnail = ImageSpecField(source = 'images', processors=[ResizeToFill(120,60)], format='JPEG')
    hits = models.PositiveBigIntegerField(default=0, verbose_name='조회수')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]