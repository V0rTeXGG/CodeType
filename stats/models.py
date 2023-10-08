from django.db import models
from django.contrib.auth.models import User


class Stats(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,
                                related_name='stats_user')
    complete_tasks = models.BigIntegerField(default=0)
    time_tasks = models.BigIntegerField(default=0)
    level = models.BigIntegerField(default=0)
    js_tasks = models.BigIntegerField(default=0)
    js_aim = models.BigIntegerField(default=0)
    js_speed = models.BigIntegerField(default=0)
    js_avg = models.BigIntegerField(default=0)
    c_tasks = models.BigIntegerField(default=0)
    c_aim = models.BigIntegerField(default=0)
    c_speed = models.BigIntegerField(default=0)
    c_avg = models.BigIntegerField(default=0)
    py_tasks = models.BigIntegerField(default=0)
    py_aim = models.BigIntegerField(default=0)
    py_speed = models.BigIntegerField(default=0)
    py_avg = models.BigIntegerField(default=0)

    def __int__(self):
        return self.user
