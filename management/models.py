from distutils.command.upload import upload
from email.policy import default
from operator import mod
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
#compress image
from io import BytesIO
from PIL import Image
from django.core.files import File
# Create your models here.

#image compression method
def compress(image):
    im=Image.open(image)
    im_io=BytesIO()
    try:
        
       im.save(im_io,'JPEG',quality=60)
    except:
        im.save(im_io,'png',quality=60)
    new_image=File(im_io,name=image.name)
    return new_image
    



User=get_user_model()

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=True)
    id_user=models.IntegerField()
    bio=models.TextField(blank=True)
    profileimage=models.ImageField(upload_to='profile_images',default='blank-profile-picture.png',null=True)
    location=models.CharField(max_length=100,blank=True)
    def getImange(self):
        if self.profileimage != "defaults.jpg":
           def save(self,*args,**kwargs):
               new_image=compress(self.profileimage)
               self.profileimage=new_image
               super().save(*args,**kwargs)

    
    def __str__(self):
        return self.user.username