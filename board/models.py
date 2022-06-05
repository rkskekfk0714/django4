from django.db import models
from acc.models import User
# Create your models here.
class Board(models.Model):
    subject = models.CharField(max_length=100)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="writer")
    content = models.TextField()
    pubdate = models.DateTimeField()
    likey = models.ManyToManyField(User, blank=True, related_name="likey")

    def __str__(self):
        return self.subject

    
    def summary(self):
        # 80 글자 이상일 경우 80 글자 까지만 출력 뒤에 ...
        # 80 미만인 경우 그냥 출력
        if len(self.content) >= 80:
            return f"{self.content[:80]} ..." 
        return self.content


    def hot(self):
        if self.likey.count() >= 2:
            return True
        return False
    

class Reply(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    replyer = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"{self.board}_{self.replyer}"