from django.contrib import admin
from . import models

class TimeAdmin(admin.ModelAdmin):
	pass
	# list_display=['schedule','movie','theater']
	# list_filter=['movie','theater']

admin.site.register(models.Movie)
admin.site.register(models.Theather)
admin.site.register(models.Time, TimeAdmin)
