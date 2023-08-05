import code
from email.policy import default
from django.db import models
from sqlalchemy import null

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
    


class flutter_data(models.Model):
    App_Name=models.CharField(max_length=30)
    description=models.TextField(max_length=1000,null=True,default="null")
    codes=models.TextField(max_length=10000)
    img=models.ImageField(upload_to='alexander',null=True,default='defaults.jpg')
    def getImange(self):
        if self.img != "defaults.jpg":
           def save(self,*args,**kwargs):
               new_image=compress(self.img)
               self.img=new_image
               super().save(*args,**kwargs)

    def __str__(self):
        return f'{self.App_Name}-{self.img}'

#C LANGEUAG

class C_data(models.Model):
    App_Name=models.CharField(max_length=30)
    description=models.TextField(max_length=1000,null=True,default="null")
    codes=models.TextField(max_length=10000)
    img=models.ImageField(upload_to='Calexander',null=True,default='defaults.jpg')
    def getImange(self):
        if self.img != "defaults.jpg":
           def save(self,*args,**kwargs):
               new_image=compress(self.img)
               self.img=new_image
               super().save(*args,**kwargs)

    def __str__(self):
        return f'{self.App_Name}-{self.img}'

# django
class django_data(models.Model):
    App_Name=models.CharField(max_length=30)
    description=models.TextField(max_length=1000,null=True,default="null")
    codes=models.TextField(max_length=10000)
    img=models.ImageField(upload_to='django',null=True,default="defaults.jpg")
    def getImange(self):
        if self.img != "defaults.jpg":
           def save(self,*args,**kwargs):
               new_image=compress(self.img)
               self.img=new_image
               super().save(*args,**kwargs)

    def __str__(self):
        return f'{self.App_Name}-{self.img}'

#web3
class web3(models.Model):
    App_Name=models.CharField(max_length=30)
    description=models.TextField(max_length=1000,null=True,default="null")
    codes=models.TextField(max_length=10000)
    img=models.ImageField(upload_to='web3',null=True,default="defaults.jpg")
    def getImange(self):
        if self.img != "defaults.jpg":
           def save(self,*args,**kwargs):
               new_image=compress(self.img)
               self.img=new_image
               super().save(*args,**kwargs)

    def __str__(self):
        return f'{self.App_Name}-{self.img}'


#solidity
class solidity(models.Model):
    App_Name=models.CharField(max_length=30)
    description=models.TextField(max_length=1000,null=True,default="null")
    codes=models.TextField(max_length=10000)
    img=models.ImageField(upload_to='solidity',null=True,default="defaults.jpg")
    def getImange(self):
        if self.img != "defaults.jpg":
           def save(self,*args,**kwargs):
               new_image=compress(self.img)
               self.img=new_image
               super().save(*args,**kwargs)

    def __str__(self):
        return f'{self.App_Name}-{self.img}'