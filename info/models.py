from django.db import models
import os
def get_image_path(instance, filename):
    return os.path.join('images', str(instance.id), filename)

class Team(models.Model):
	"""docstring for Team"""
	post_choices = (("Ex Mem", "Executive Member"),("Joint", "Joint Secretary"),("Additional", "Additional Secretary"),("General","General Secretary"),)
	name=models.CharField(max_length=100,unique=False)
	post=models.CharField(max_length=50,choices=post_choices,default="Ex Mem")
	image=models.ImageField(upload_to='photos', verbose_name='My Photo')

	def __str__(self):
		return self.name
		
# Create your models here.
