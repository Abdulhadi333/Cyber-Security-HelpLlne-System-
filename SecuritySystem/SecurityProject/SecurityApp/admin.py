from django.contrib import admin

from .models import Scan_Vul, Certification, Comment, Profile, reatingProfile

admin.site.register(Scan_Vul)
admin.site.register(Certification)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(reatingProfile)


