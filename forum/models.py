from django.db import models
from django.conf import settings


        
class Thread(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=250)
    vote = models.BigIntegerField()    
    created_at = models.DateTimeField(auto_now_add=True)
    # tag = models.ForeignKey(Tag,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Threads'

class Tag(models.Model):
    keyword = models.CharField(max_length=100)
    thread = models.ForeignKey(Thread,on_delete=models.CASCADE)    
    def __str__(self):
        return self.keyword
    

class Answer(models.Model):
    description = models.TextField()
    vote = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    thread = models.ForeignKey(Thread,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Comment(models.Model):
    body= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Response(models.Model):
    body= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 
    thread = models.ForeignKey(Thread,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class UserVoteThread(models.Model):
    status =  models.BooleanField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread,on_delete=models.CASCADE)
    

class UserVoteAnswer(models.Model):
    status =  models.BooleanField()    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE)
    

    
