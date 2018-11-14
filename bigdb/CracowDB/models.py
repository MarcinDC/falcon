from django.db import models

# Create your models here.


class kwdata(models.Model):
	prefix  = models.CharField(max_length=4)
	number  = models.CharField(max_length=4)
	correct = models.CharField(max_length=1)

	KW_NIER_GR = 'NG'
	KW_LOK_MIESZ = 'LM'
	KW_TYPE_CHOICES = (
		(KW_NIER_GR, 'Nieruchomość gruntowa'),
		(KW_LOK_MIESZ, 'Lokal mieszkalny'),
	)
	kw_type = models.CharField(max_length=2, choices=KW_TYPE_CHOICES)

	def __str__(self):
		return self.title
		