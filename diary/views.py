from django.shortcuts import render
from .models import Diary, Comment

# Create your views here.
def list(request):
    diary = Diary.objects.get(id=1)
    # 1:N 관계
    comments = diary.comment_set.all()
    for comment in comments:
        print(comment.content)