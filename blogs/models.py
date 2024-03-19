from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class BlogText(models.Model):
    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.text