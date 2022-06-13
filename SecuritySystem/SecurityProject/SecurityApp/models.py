from django.db import models
from django.contrib.auth.models import User


class Scan_Vul(models.Model):
    CHOICES1 = (
        ('Microsoft OS', 'Microsoft OS'),
        ('MAC OS', 'MAC OS'),
        ('Linux OS', 'Linux OS'),
        ('Unix OS', 'Unix OS'),
        ('Other', 'Other')

    )
    CHOICES2 = (
        ('active', 'active'),
        ('Non Active', 'Non Active')
    )

    ScannerName = models.CharField(max_length=150)
    VulnerabilityName = models.CharField(max_length=256)
    type_OS = models.CharField(max_length=250, choices=CHOICES1)
    stateOFvul = models.CharField(max_length=250, choices=CHOICES2)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class Certification(models.Model):
    image = models.URLField()
    titleCer = models.CharField(max_length=256)
    CompanyName = models.CharField(max_length=256)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.titleCer


class Comment(models.Model):
    title = models.CharField(max_length=100)
    comment = models.TextField(max_length=500)
    certification = models.ForeignKey(Certification, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class Profile(models.Model):
    image = models.URLField()
    name = models.CharField(max_length=256)
    education = models.CharField(max_length=256)
    abstract = models.TextField(max_length=500)
    experience = models.TextField(max_length=500)
    service = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
