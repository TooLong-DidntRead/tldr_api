from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class User(models.Model):
	name = models.CharField(max_length=200)

	def clean(self):
		if not self.name:
			raise ValidationError(_('All fields must be filled in.'))

class Query(models.Model):
	areas_of_focus = ArrayField(models.CharField(max_length=200), blank=True, default=list)    
	tos = models.TextField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def clean(self):
		if not self.areas_of_focus or not self.tos or not self.user:
			raise ValidationError(_('All fields must be filled in.'))
    
class Result(models.Model):
		response = models.JSONField(default=dict)
		query = models.ForeignKey(Query, on_delete=models.CASCADE)
		
		def clean(self):
			if not self.response or not self.query:
				raise ValidationError(_('All fields must be filled in.'))
			
class Tos(models.Model):
		tos = models.TextField()
		
		def clean(self):
			if not self.tos:
				raise ValidationError(_('All fields must be filled in.'))
			
class Comparison(models.Model):
		response = models.JSONField(default=dict)
		user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
		
		def clean(self):
			if not self.response or not self.user:
				raise ValidationError(_('All fields must be filled in.'))
			
class TosComparisons(models.Model):
		tos = models.ForeignKey(Tos, on_delete=models.CASCADE)
		comparison = models.ForeignKey(Comparison, on_delete=models.CASCADE)

		def clean(self):
			if not self.tos or not self.comparison:
				raise ValidationError(_('All fields must be filled in.'))
			
