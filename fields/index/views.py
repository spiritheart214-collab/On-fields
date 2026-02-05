from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import FAQ
from tutorials.models import Tutorial
from news.models import News_preview
from .forms import MailSendForm


def index(request: HttpRequest):
    context = {
        "faqs" : FAQ.objects.all(),
        "tutorials": Tutorial.objects.all(),
        "news" :  News_preview.objects.all(),
    }
    return render(request, 'index/index.html', context)

def send_email(request):
    if request.method == 'POST':
        form = MailSendForm(request.POST)
        if form.is_valid():   
            name = form.cleaned_data['name']
            message = form.cleaned_data['textarea']
            letter = 'Имя: {} \nСообщение: {}'.format(name, message)
            subject = 'Сообщение с сайта "На полях"'
            from_email = 'onFileds@yandex.ru'
            recipient_list = ['onFileds@yandex.ru']
            send_mail(subject, letter, from_email, recipient_list, fail_silently=False)
            messages.success(request, 'Ваше сообщение отправлено!')
            return redirect('index:index')
    else:
        form = MailSendForm()
    return render(request, 'index/index.html', {'form': form})
