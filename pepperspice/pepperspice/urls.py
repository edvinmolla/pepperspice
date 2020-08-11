# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('pages.urls')), # Welcome page
    path('dashboard/', include('dashboard.urls')),
    path('services/', include('pages.urls')),
    path('products/', include('pages.urls')),
    path('pricing/', include('pages.urls')),
    path('support/', include('pages.urls')),
    path('examples/', include('pages.urls')),
    path('al/', include('pages.urls')),
    # path('', TemplateView.as_view(template_name='logout.html'), name='logout') Kept as an example
]