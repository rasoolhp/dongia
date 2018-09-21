from django.db import models
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver

class User(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Dong(models.Model):
    name = models.CharField(max_length = 50)
    amount = models.FloatField()
    dongia = models.ManyToManyField(User)
    donger = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="donger",
    )

    @property
    def dong_per_person(self):
        tedad = self.dongia.count()
        return self.amount/tedad if tedad else None
    def __str__(self):
        return self.name
    def dongia_list(self):
        return " - ".join([ p.name for p in self.dongia.all() ])

class DongRecord(models.Model):
    for_dong = models.ForeignKey(
        Dong,
        on_delete = models.CASCADE,
        related_name = "for_dong",
        null = True,
    )
    from_user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = "from_user",
        null = True,
    )
    to_user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = "to_user",
        null = True,
    )
    amount = models.FloatField(null = True, blank = True)
    paid = models.BooleanField(default = False, null = True, blank = True)

@receiver(m2m_changed, sender = Dong.dongia.through)
def m2m_func(sender, instance, action, **kwargs):
    print ("action:",action)
    child_records = DongRecord.objects.filter(for_dong__id=instance.id)
    print ("olds:",child_records)
    for records in child_records:
        child_records.delete()
        print("deleted an old dong record")
    print ("news:",instance.dongia.all())
    for member in instance.dongia.all():
        #this is for find me to me dong!
        dong_record = DongRecord.objects.get_or_create(
            for_dong = instance,
            from_user = member,
            to_user = instance.donger,
            amount = instance.dong_per_person,
        )
        print("added a dong record")

@receiver(post_save, sender = Dong)
def post_save_func(sender, instance, created, **kwargs):
    if not created:
        child_records = DongRecord.objects.filter(for_dong__id=instance.id)
        print("updates:",child_records)
        for dong_rec in child_records:
            print("record-check")
            if dong_rec.to_user != instance.donger:
                child_records.update(to_user = instance.donger)
                print("updated touser")
            if dong_rec.amount != instance.dong_per_person:
                child_records.update(amount = instance.dong_per_person)
                print("updated amount")
        print("post_updated")
    else:
        print("new_post")
