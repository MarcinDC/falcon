from django.db import models

# Create your models here.


class one_product(models.Model):
	name = models.CharField(max_length=100)
	code = models.CharField(max_length=20)
	score = models.FloatField()
	image_name = models.CharField(max_length=100)

	CORE_PRODUCT_LINK = 'https://www.ceneo.pl/'
	CORE_PHOTO_LINK = 'https://image.ceneostatic.pl/data/products/'


	@property
	def GetProductLink(self):
		return self.CORE_PRODUCT_LINK + self.code
	
	@property
	def GetPhotoLink(self):
		return self.CORE_PHOTO_LINK + self.code + '/' + self.image_name
	