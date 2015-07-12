from django.db import models

# Create your models here.
class SignUp(models.Model):
	"""docstring for Newsletter"""
	
	email = models.EmailField()
	full_name = models.CharField(max_length=100, blank=True, null=True)
	age = models.CharField(max_length=2,default='00')

	def __unicode__(self): #__str__
		return self.full_name

