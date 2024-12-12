from django.db import models


class Appointment(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    service = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.customer_name} - {self.service} on {self.date} at {self.time}"
