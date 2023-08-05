from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def index(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        send_mail(
           subject,
           message,
           settings.EMAIL_HOST_USER,
          [email],
   
)
        
    return render(request , 'index.html', {})



