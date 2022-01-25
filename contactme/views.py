from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

def thanks(request):
    return render(request, "contactme/thanks.html")
def shipping(request):
    return render(request, 'contactme/shipping.html', {})
def refund(request):
    return render(request, 'contactme/refund.html', {})
def privacy(request):
    return render(request, 'contactme/privacy.html', {})

def contactme(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Пробное сообщение"
            body = {
                'your_name': form.cleaned_data['your_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message,
                          'tokynaba@mail.ru',
                          ['tokynaba@mail.ru'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            return render(request, "contactme/thanks.html", {})

    form = ContactForm()
    return render(request, "contactme/contactme.html", {'form': form})
