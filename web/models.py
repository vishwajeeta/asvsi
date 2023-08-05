from django.db import models

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
    
class web_app(models.Model):
    App_Name=models.CharField(max_length=30)
    URL=models.CharField(max_length=100)
    img=models.ImageField(upload_to='apps')
    def save(self,*args,**kwargs):
        new_image=compress(self.img)
        self.img=new_image
        super().save(*args,**kwargs)

    def __str__(self):
        return f'{self.App_Name}-{self.img}'