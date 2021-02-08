from django.db import models

# Create your models here.

class AboutMe(models.Model):
    Job_title = models.CharField(max_length=100)
    name = models.CharField(null=False ,max_length=50)
    image_file = models.ImageField(upload_to='uploads/', null= True)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=False)
    description = models.TextField(null=False, max_length=200)

    class Meta:
        verbose_name = 'About Me'
        verbose_name_plural = 'About Me'


    def __str__(self):
        return self.name

class Skills(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False ,max_length=50)
    image_file = models.ImageField(upload_to='images', null= True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
  

    def __str__(self):
        return self.name

    
    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

        

class Timeline(models.Model):
    date = models.DateField()
    title = models.CharField(null = False, max_length = 100)
    description =  models.CharField(null = False, max_length = 200)

    def __str__(self):
        return self.title
    
