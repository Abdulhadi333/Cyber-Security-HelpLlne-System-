from django.contrib import admin

from .models import Scan_Vul, Certification, Comment, Profile, reatingProfile


class Scan_VulAdmin(admin.ModelAdmin):
    list_display = ('ScannerName', 'VulnerabilityName','created_at')


class CertificationAdmin(admin.ModelAdmin):
    list_display = ('titleCer', 'CompanyName')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'service', 'email')



admin.site.register(Scan_Vul,Scan_VulAdmin)
admin.site.register(Certification, CertificationAdmin)
admin.site.register(Comment)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(reatingProfile)


