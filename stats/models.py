from django.db import models


class Stats(models.Model):
    profile_photo = models.ImageField(upload_to='movies/')
    complete_tasks = models.BigIntegerField(default=0)
    time_tasks = models.BigIntegerField(default=0)
    level = models.BigIntegerField(default=0)
    js_tasks = models.BigIntegerField(default=0)
    js_aim = models.BigIntegerField(default=0)
    js_speed = models.BigIntegerField(default=0)
    js_avg = models.BigIntegerField(default=0)

    def __str__(self):
        return self.complete_tasks
