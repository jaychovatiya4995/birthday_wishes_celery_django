from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE','birthday_wishes.settings')
app = Celery('birthday_wishes')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Celery Beat Settings
# app.conf.beat_schedule = {
#     'send-mail-every-day-at-12': {
#         'task': 'wishes.tasks.send_birthday_mail',
#         'schedule': crontab(minute="*/1")
#     }
# }

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

