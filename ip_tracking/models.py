from django.db import models

# Create your models here.
class RequestLog(models.Model):
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    path = models.CharField(max_length=2048)

    def __str__(self):
        return f"{self.ip_address} - {self.timestamp} at {self.path}"


class BlockedIP(models.Model):
    pass