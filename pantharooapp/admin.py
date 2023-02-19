from django.contrib import admin
from pantharooapp.models import History, AllowDevice, NotAllow, AvailableFiles, FileHistory, FileHistoryNotAllowSPAM, EmailSeenDB
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(History)
admin.site.register(AllowDevice)
admin.site.register(NotAllow)
admin.site.register(FileHistory)
admin.site.register(AvailableFiles)
admin.site.register(FileHistoryNotAllowSPAM)
class EmailSeenDBV(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('email','numberOfSeen','Title','lastSeen','lastseenTime')
admin.site.register(EmailSeenDB, EmailSeenDBV)