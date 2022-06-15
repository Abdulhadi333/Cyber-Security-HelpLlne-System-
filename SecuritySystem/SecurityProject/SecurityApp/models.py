from django.db import models
from django.contrib.auth.models import User

"""
table for Scanner vulnerabilities enter new vulnerabilities...

"""


class Scan_Vul(models.Model):
    CHOICES1 = (
        ('Windows OS', 'Windows OS'),
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
    VulnerabilityName = models.CharField(max_length=300)
    type_OS = models.CharField(max_length=250, choices=CHOICES1)
    stateOFvul = models.CharField(max_length=250, choices=CHOICES2)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.VulnerabilityName



"""
table for Specialist CyberSecurity write new posts 
"""


class Certification(models.Model):
    image = models.URLField()
    titleCer = models.CharField(max_length=256)
    CompanyName = models.CharField(max_length=256)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.titleCer


"""
table wite new comments for posts Certifications 
"""


class Comment(models.Model):
    title = models.CharField(max_length=100)
    comment = models.TextField(max_length=500)
    certification = models.ForeignKey(Certification, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


"""
Table profile Specialist CyberSecurity
"""


class Profile(models.Model):
    image = models.URLField()
    name = models.CharField(max_length=256)
    education = models.CharField(max_length=256)
    abstract = models.TextField(max_length=500)
    experience = models.TextField(max_length=500)
    service = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    l = models.EmailField(max_length=100)


"""
rating for Specialist CyberSecurity
"""


class reatingProfile(models.Model):
    RATE_CHOICES = (
        ("4", "excellent"),
        ("3 good", "very good"),
        ("2", "good"),
        ("1", "bad"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.CharField(max_length=250, choices=RATE_CHOICES)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
