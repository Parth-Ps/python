from django.shortcuts import render, redirect
from django.contrib import messages
from .form import ContactForm
# from .models import Contact

# Create your views here.


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST["name"]
            form.save()
            messages.success(request, "send sucessfully!!")
            return redirect('/')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
