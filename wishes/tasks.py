from celery import shared_task
# from celery import task
from celery.schedules import crontab
import datetime
from celery.utils.log import get_task_logger
from time import sleep
from wishes.models import BirthdayWishes
from django.core.mail import send_mail
from birthday_wishes.settings import EMAIL_HOST_USER

logger = get_task_logger(__name__)


@shared_task(name='my_first_task')
def my_first_task(duration):
    sleep(duration)
    return('first_task_done')


@shared_task(name='add')
def add(a, b):
    return a + b

# @periodic_task(run_every=crontab(minute=0, hour='12'))
# @task(bind=True, name='send_birthday_mail')
@shared_task(bind=True, name='send_birthday_mail')
def send_birthday_mail():
    today = datetime.date.today()
    user_details = BirthdayWishes.objects.all()
    mail_subject = "Birthday whises"
    for user in user_details:
        if user.birthdate.month == today.month and user.birthdate.day == today.day:
            print('User Name: ', user.username)
            message = f"May your birthday be the start of a year filled with good luck, good health and much happiness. !! \n\n Happy Birthday {user.username}"
            to_email = user.email
            print(to_email)
                    
            send_mail(
                subject = mail_subject,
                message=message,
                from_email=EMAIL_HOST_USER,
                recipient_list=[to_email],
                fail_silently=True,
            )

          
