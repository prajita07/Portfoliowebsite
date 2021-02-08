from django.db import models

# Create your models here.
class ContactMe(models.Model):
    Job_title = models.CharField(max_length=50)
    Full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    received_at = models.DateTimeField(auto_now=True)
    message = models.TextField(null=False)

    class Meta:
        verbose_name = 'Contact Me'
        verbose_name_plural = 'Contact Me'

