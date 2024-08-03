from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage

# Create your views here.

def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', )
            content = request.POST.get('content', )
            #enviamos el correo y redireccionamos
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\n{}".format(name,email,content),
                "no-contestar@inbox.mailtrap.io",
                ["nicolascornaglia0@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                # Todo ha ido bien
                return redirect(reverse('contact')+"?ok")
            except Exception:
                import traceback
                traceback.print_exc()
                # Algo no ha ido bien
                return redirect(reverse('contact')+"?fail")
            
    return render(request, "contact/contact.html", {'form':contact_form})
