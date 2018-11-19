from django.db import models

# Create your models here.


class kwdata(models.Model):
	kw_number  = models.CharField(max_length=15, default='', help_text='pełny numer kw')
	date_of_save = models.DateField(null=True, blank=True)
	date_of_close = models.DateField(null=True, blank=True)

	KW_NIER_GR = 'NG'
	KW_LOK_MIESZ = 'LM'
	KW_TYPE_CHOICES = (
		(KW_NIER_GR, 'Nieruchomość gruntowa'),
		(KW_LOK_MIESZ, 'Lokal stanowiący odrębną nieruchomość'),
	)
	kw_type = models.CharField(max_length=2, choices=KW_TYPE_CHOICES)


	def __str__(self):
		return self.kw_number

	@property
	def get_date_of_save(self):
		if self.date_of_save is None:
			return ''
		else:
			return self.date_of_save


	@property
	def get_kw_type(self):
		if self.kw_type==self.KW_NIER_GR:
			return 'Nieruchomość gruntowa'
		else:
			return 'Lokal stanowiący odrębną nieruchomość'
	

		