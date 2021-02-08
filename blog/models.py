from django.db import models


# Create your models here.

class BlogCategory(models.Model):
    category_name= models.CharField(null=False ,max_length=30)
    created_at = models.DateTimeField(null=False)
    
    def __str__(self):
        return self.category_name
        
    class Meta:
        verbose_name = 'Blog Category'
        verbose_name_plural = 'Blog Categories'


class Blog(models.Model):
    title = models.CharField(null=False ,max_length=100)
    category = models.ForeignKey(BlogCategory, on_delete= models.CASCADE)
    author = models.CharField(null=False ,max_length=50)
    image_file = models.ImageField(upload_to='images', null= True)
    description = models.TextField(null=False, max_length=200)
    is_popular = models.BooleanField(null=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'





