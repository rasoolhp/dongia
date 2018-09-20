from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Dong(models.Model):
    name = models.CharField(max_length=50)
    amount = models.FloatField()
    dongia = models.ManyToManyField(User)
    donger = models.ForeignKey(User,on_delete=models.CASCADE,related_name="donger")
    def dongia_list(self):
        return " - ".join( [p.name for p in self.dongia.all()] )
    @property
    def dong(self):
        tedad = self.dongia.count()
        return self.amount/tedad if tedad else None
    def __str__(self):
            return self.name
