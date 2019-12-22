from django.db import models

# Create your models here.

class Post(models.Model):
    categoryList =(('drama','Drama'),('action','Action'))


    title = models.CharField(max_length=255)
    category = models.CharField(max_length=6,choices=categoryList,default='drama')
    content = models.TextField()
    is_featured = models.BooleanField(default=False)

    

    def __str__(self):
        return self.title