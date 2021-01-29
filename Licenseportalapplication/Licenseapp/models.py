from django.db import models
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta



class Client(models.Model):
    client_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=256)
    phone = models.CharField(max_length=10)
    user_name = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    admin_point_of_contact = models.EmailField(max_length=256)

    def __str__(self):
        return self.user_name

    def get_licenses(self):
        all_licenses = []
        for licence in self.license_set.all():
            all_licenses.append({
                'package': licence.package,
                'license_type': licence.license_type,
                'created_time': licence.created_time,
                'expiration_time': licence.expiration_time
            })

        return all_licenses


class License(models.Model):
    LICENSE_TYPE_CHOICES = [
        ('Production', 'Production'),
        ('Evaluation', 'Evaluation')
    ]
    package = models.CharField(max_length=200)
    license_type = models.CharField(max_length=125, choices=LICENSE_TYPE_CHOICES)
    created_time = models.DateTimeField(auto_now_add=True)
    expiration_time = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.package
