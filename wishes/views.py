from django.shortcuts import render
from django.http import HttpResponse
from .tasks import my_first_task, add, send_birthday_mail
from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
def index(request):   
    # send_birthday_mail.delay()    
    my_first_task.delay(10)
    return HttpResponse('response done')

@csrf_exempt
def addition(request): 
    s = add.delay(10, 15).get()
    print("sum",s)
    return HttpResponse('sum complete', s)