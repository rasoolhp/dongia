from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

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
    def dong_per_person(self):
        tedad = self.dongia.count()
        return self.amount/tedad if tedad else None
    def __str__(self):
            return self.name

class DongRecord(models.Model):
    for_dong = models.ForeignKey(Dong, on_delete=models.CASCADE,related_name="for_dong",null=True)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="from_user",null=True)
    to_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="to_user",null=True)
    amount = models.FloatField(null=True,blank=True)
    paid = models.BooleanField(default=False,null=True,blank=True)


@receiver(m2m_changed,sender=Dong.dongia.through)
def calculate_dong(sender,instance,action,**kwargs):
    for member in instance.dongia.all():
        #this is for find me to me dong!
        if member != instance.donger:
            dong_record = DongRecord.objects.get_or_create(for_dong=instance,from_user=member,to_user=instance.donger,amount=instance.dong_per_person)
