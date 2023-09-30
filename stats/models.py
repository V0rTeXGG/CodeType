from django.db import models


class Stats(models.Model):
    id = models.BigIntegerField(primary_key=True)
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
    user_id_stats = models.BigIntegerField()

    def __int__(self):
        return self.user_id_stats
