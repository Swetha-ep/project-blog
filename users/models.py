from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from cloudinary.models import CloudinaryField
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # image = models.ImageField(
    #     default='https://res.cloudinary.com/doqvx7gyg/image/upload/v1732348965/default_tkihgy.jpg',
    #     upload_to='profile_pics'
    # )
    image = CloudinaryField('image',default='default_tkihgy')

    def __str__(self):
        return f'{self.user.username} Profile'
    