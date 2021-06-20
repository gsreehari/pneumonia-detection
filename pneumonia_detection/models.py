from django.db import models


class UserData(models.Model):
    def nameFile(instance,filename):
        filename = str(instance.name)+"-"+filename
        return '/'.join(['user_xray_images',filename])

    name = models.CharField(max_length=100, null=False, blank=False)
    age = models.IntegerField(default=0, null=False, blank=False)
    image = models.ImageField(upload_to= nameFile, null=False, blank=False)
    result = models.CharField(max_length=100, null=False, blank=False)