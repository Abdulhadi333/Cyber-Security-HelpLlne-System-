from django.urls import path
from . import views

urlpatterns = [
    # urls for vulnerabilities...
    path("add-vulnerability", views.add_Scan_Vul, name="Add vulnerability"),
    path("list-vulnerabilities",views.list_Scan_Vul,name='list vulnerabilities'),
    path("update-vulnerability/<vulner_id>", views.update_Scan_Vul, name='update vulnerabilities'),
    path("delete-vulnerability/<vulner_id>", views.delete_vulnerability, name='delete vulnerabilities'),
    path("search/<vul_id>", views.search_vulnerabilityOS, name="searchOS"),
    # urls for Certifications...
    path("add-Certification", views.add_Certification, name="Add Certification"),
    path("list-certification", views.list_Certification, name='list Certification'),
    path("update-certification/<cer_id>", views.update_Certification, name='update Certification'),
    path("delete-certification/<cer_id>", views.delete_Certification, name='delete Certification'),
    # urls for Profile...
    path("add-profile", views.add_Profile, name="Add Profile"),
    path("list-profile", views.list_profile, name='list profile'),
    path("update-profile/<profile_id>", views.update_profile, name='update profile'),
    path("delete-profile/<profile_id>", views.delete_profile, name='delete profile'),
    # urls for comments...
    path("add-comment", views.create_comment, name="Add Comment"),
    path("list-comments", views.list_comments, name='list comments'),
    path("comment-search/<certification_id>", views.search_comment, name="search comment"),

]


