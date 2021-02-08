from django.db import models


class Banner(models.Model):
    image_file = models.ImageField(upload_to='uploads/', null= True)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
         return self.title

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banner'

    
class Subscription(models.Model):
    email= models.EmailField(max_length=50)
    received_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscription'

    
    

    
