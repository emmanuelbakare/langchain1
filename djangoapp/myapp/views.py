from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from myapp.models import Contact
from myapp.forms import ContactForm

def test(request):
    return HttpResponse("<h1>Hello django </h1>")

def contacts(request):
    contacts = Contact.objects.all()
    return render(request, "myapp/contacts.html",context={"contacts":contacts} )
    # return HttpResponse("<H1> Contact List </H1>")

def add_contact(request):
    if request.method =="POST":
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
        
        return redirect('contact-list')
    else:
        form = ContactForm()

    return render(request,'myapp/add_contact.html', context={"form":form})
            