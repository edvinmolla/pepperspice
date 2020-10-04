from django.urls import path
from allauth.account.views import LoginView, SignupView
from .views import *
from allauth.account import views as vw

urlpatterns = [
    path('', homepage, name='home'),
    path('services/', ServicesView.as_view(), name='services'),
    path('products/', ProductsView.as_view(), name='products'),
    path('pricing/', PricingView.as_view(), name='pricing'),
    path('support/', SupportView.as_view(), name='support'),
    path('examples/', ExamplesView.as_view(), name='examples'),
    path('al/', AlbanianView.as_view(), name="albanian"),
    path('al/services/', AlbanianServicesView.as_view(), name='services_al'),
    path('al/products/', AlbanianProductsView.as_view(), name='products_al'),
    path('al/pricing/', AlbanianPricingView.as_view(), name='pricing_al'),
    path('al/support/', AlbanianSupportView.as_view(), name='support_al'),
    path('al/examples/', AlbanianExamplesView.as_view(), name='examples_al'),
    path('al/accounts/login/', LoginView.as_view(), name='login_al'),
    path('al/accounts/signup/', SignupView.as_view(), name='signup_al'),
]