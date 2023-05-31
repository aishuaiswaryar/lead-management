from django.contrib import admin
from.models import batch,details
# Register your models here.
class batchAdmin(admin.ModelAdmin):
    list_display=('batchname',)
admin.site.register(batch,batchAdmin)

class detailsAdmin(admin.ModelAdmin):
    list_display= ('course', 'trainer', 'Start_date', 'End_date')
admin.site.register(details,detailsAdmin)