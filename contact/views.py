from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
from .models import ClientData


def contact(request):
    contact_form = ContactForm()
    #procesamos el formulario cuando el request es post
    if request.method == "POST":
        #declaramos el formulario contact con los datos rellenados
        #podemos así comprobar si son validos los datos
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            #si son correctos recuperamos los datos
            #Por defecto se asigna una cadena vacía
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #tenemos toda las informaciones para guardar el cliente y enviar la mail
            #Guardo los datos
            client_data = ClientData(name=name, email=email)
            client_data.save()
            # Creamos el correo
            email = EmailMessage(
                "El templo del vino! Bienvenido!",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                # Ponemos mas correos a los cuales queremos enviar el correo
                ["alessiocioffi.es@gmail.com"],
                # El usuario responde a ['']
                reply_to=[email]
            )

            # Lo enviamos y redireccionamos
            try:
                email.send()
                # Todo ha ido bien, redireccionamos a OK
                #reverse es para utiliza el path y no con el url tags
                return redirect(reverse('contact')+"?ok")
            except:
                # Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact')+"?fail")
    
    return render(request, "contact/contact.html",{'form':contact_form})