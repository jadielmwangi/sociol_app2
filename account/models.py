from django.db import models

# Create your models here.
from django.conf import settings
class Profile(models.Model):    
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                            blank=True)

    school = models.CharField(max_length=100)
                  
    def __str__(self):
        return f'Profile for user {self.user.username}'                            