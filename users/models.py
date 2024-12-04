from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from cloudinary.models import CloudinaryField
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image',default='default_tkihgy')
    bio = models.TextField(blank=True,null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    