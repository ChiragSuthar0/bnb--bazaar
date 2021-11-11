from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.
class Firm(models.Model):
    firm_id=models.AutoField
    firm_name=models.CharField(max_length=25)
    firm_price=models.IntegerField()

    def __str__(self):
        return self.firm_name

class Trader(models.Model):
    trader_id = models.AutoField
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=25)

    f1 = models.IntegerField(default=0)
    f2 = models.IntegerField(default=0)
    f3 = models.IntegerField(default=0)
    f4 = models.IntegerField(default=0)
    f5 = models.IntegerField(default=0)
    f6 = models.IntegerField(default=0)
    f7 = models.IntegerField(default=0)
    f8 = models.IntegerField(default=0)
    """
    f9 = models.IntegerField(default=0)
    f10 = models.IntegerField(default=0)
    f11 = models.IntegerField(default=0)
    f12 = models.IntegerField(default=0)
    f13 = models.IntegerField(default=0)
    f14 = models.IntegerField(default=0)
    f15 = models.IntegerField(default=0)
    """
    mb = models.IntegerField(default=15000)
    mi = models.IntegerField(default=0)
    mt = models.IntegerField(default=15000)

    def __str__(self):
        return self.username + " : " + str(self.mt)


class Update(models.Model):
    news=models.TextField()
    update_time=models.TimeField(default=timezone.now())
    def __str__(self):
        return "News update @ " + str(self.update_time)[:6]

