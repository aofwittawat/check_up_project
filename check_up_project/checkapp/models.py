from django.db import models


class UserDetail(models.Model):
    CHOICES = (('m', 'male'), ('f', 'female'))
    username = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    gender = models.CharField(max_length=40, choices=CHOICES, blank=True)
    age = models.IntegerField()
    weight = models.IntegerField()
    height = models.IntegerField()
    tel = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, blank=True)
    userimage = models.ImageField(upload_to='image', null=True, blank=True)
    address = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    smoking = models.BooleanField(default=False)
    alcohol = models.BooleanField(default=False)
    HT = models.BooleanField(default=False)
    DM = models.BooleanField(default=False)
    DLP = models.BooleanField(default=False)
    hepatitis = models.BooleanField(default=False)
    chronic_hepatitis = models.BooleanField(default=False)
    osteoporosis = models.BooleanField(default=False)
    allergy = models.BooleanField(default=False)
    ACS = models.BooleanField(default=False)
    renal_stone = models.BooleanField(default=False)
    cancer = models.BooleanField(default=False)
    CA_breast = models.BooleanField(default=False)
    CA_ovary = models.BooleanField(default=False)
    CA_cervix = models.BooleanField(default=False)
    CA_GI = models.BooleanField(default=False)
    CA_liver = models.BooleanField(default=False)
    CA_pancreas = models.BooleanField(default=False)
    CA_others = models.BooleanField(default=False)
    CA_prostate = models.BooleanField(default=False)

    def __str__(self):
        return self.username
