from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from ecommerce.models import Item


def home(request):
    context = {
        "items": Item.objects.all()
    }
    return render(request, 'home.html', context)


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def loginfunc(request):
    return render(request, 'registration/login.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact-page.html')


def accountvalidation(request):
    if request.user.is_authenticated:
        if request.user.is_business:
            return redirect('businesses:business-dashboard')
        else:
            return redirect('customers:customer-dashboard')
    return render(request, 'home.html')
