from django.db import models
from django.contrib.auth.models import User


class Scan_Vul(models.Model):
    name = models.CharField(max_length=150)
    titleVul = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class Certification(models.Model):
    image = models.ImageField(upload_to='images')
    titleCer = models.CharField(max_length=256)
    CompanyName = models.CharField(max_length=256)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    scanVul = models.ForeignKey(Scan_Vul, on_delete=models.CASCADE)
    certification = models.ForeignKey(Certification, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Profile(models.Model):
    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=256)
    education = models.CharField(max_length=256)
    abstract = models.TextField(max_length=500)
    experience = models.TextField(max_length=500)
    service = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
