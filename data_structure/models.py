from django.db import models

# Create your models here.
class data_structure(models.Model):
    ranking=models.IntegerField(default=100)
    type=models.CharField(max_length=20,blank=True)
    name=models.CharField(max_length=50,blank=True)
    data=models.TextField(max_length=2000,blank=True)
    img=models.ImageField(upload_to='sample_image',blank=True)
    def __str__(self):
        return self.name