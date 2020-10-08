from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from allauth.account.forms import LoginForm, SignupForm
from authentication.forms import CustomUserCreationForm
from allauth.account.forms import SignupForm


class AlbanianView(TemplateView):
    template_name = 'al/home_al.html'

class AlbanianServicesView(TemplateView):
    template_name = 'al/services_al.html'

class AlbanianProductsView(TemplateView):
    template_name = 'al/products_al.html'

class AlbanianPricingView(TemplateView):
    template_name = 'al/pricing_al.html'

class AlbanianSupportView(TemplateView):
    template_name = 'al/support_al.html'

class AlbanianExamplesView(TemplateView):
    template_name = 'al/examples_al.html'

def homepage(request):
    return render(request, 'home2.html', {'signup_form': SignupForm })

def services(request):
    return render(request, 'services.html', {'signup_form': SignupForm })

def products(request):
    return render(request, 'products.html', {'signup_form': SignupForm })

def pricing(request):
    return render(request, 'pricing.html', {'signup_form': SignupForm })

def support(request):
    return render(request, 'support.html', {'signup_form': SignupForm })

def examples(request):
    return render(request, 'examples.html', {'signup_form': SignupForm })

class HomePageView(TemplateView):
    template_name = 'home.html'

class ServicesView(TemplateView):
    template_name = 'services.html'

class ProductsView(TemplateView):
    template_name = 'products.html'

class PricingView(TemplateView):
    template_name = 'pricing.html'

class SupportView(TemplateView):
    template_name = 'support.html'

class ExamplesView(TemplateView):
    template_name = 'examples.html'