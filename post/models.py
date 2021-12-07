from django.db import models

# Create your models here.
class Post(models.Model):  
    
    title = models.CharField(max_length=100)
    content = models.TextField()  
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    class Meta:
    
        # renames the instances of the model
        # with their title name  
        def __str__(self):
            return self.title