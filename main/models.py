from __future__ import unicode_literals

from django.db import models

class Theather(models.Model):
	name = models.CharField(max_length=140)
	# movie = models.ForeignKey(Movie,related_name='theathers')
	def __str__(self):
		return self.name

class Movie(models.Model):
	title = models.CharField(max_length=140)
	poster = models.ImageField(upload_to="posters",blank=True,null=True)
	trailer = models.CharField(max_length=140, blank=True,null=True)
	dec = models.TextField(blank=True,null=True)
	theater = models.ManyToManyField(Theather,related_name='movies')

	def __str__(self):
		return self.title

class Time(models.Model):
	schedule = models.CharField(max_length=140)
	movie = models.ManyToManyField(Movie, related_name='shows')
	theater = models.ManyToManyField(Theather, related_name='shows')
	def __str__(self):
		return self.schedule