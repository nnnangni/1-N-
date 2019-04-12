from django.db import models

# Create your models here.
class Diary(models.Model):
    title = models.CharField(max_length=100)
    
# 다이어리에 누군가가 댓글을 단다?!
# 관계설정을 위해 Foreign Key 가 필요! -> post정보
class Comment(models.Model):
    content = models.TextField()
    # post에는 몇 번 게시물에 속해있는지에 대한 정보 필요
    # post = modles.ForeignKey(어떤 게시물?, 삭제할때 참조 같이 삭제)
    post = models.ForeignKey(Diary, on_delete=models.CASCADE)
