from django.db import models
from members.models import *

# Create your models here.
class Board(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField(default="")
    date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    # related_name을 설정해야 외래키에서 불러올 수 있다.
    post = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.TextField(default = "")
    created_at = models.DateTimeField(auto_now_add=True)