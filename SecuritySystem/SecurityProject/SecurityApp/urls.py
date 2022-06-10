from django.urls import path
from . import views


urlpatterns = [
    path("add-vulnerability", views.add_Scan_Vul, name="Add vulnerability"),
    path("list-vulnerabilities",views.list_Scan_Vul,name='list vulnerabilities'),
    path("update-vulnerability/<vulner_id>", views.update_Scan_Vul, name='update vulnerabilities'),

]


