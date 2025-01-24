import os
from django.conf import settings
from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render
from django.core.management import execute_from_command_line

# Configure Django settings
settings.configure(
    DEBUG=True,
    SECRET_KEY='your-secret-key',
    ROOT_URLCONF=__name__,
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(os.path.dirname(__file__), 'templates')],
        },
    ],
    STATIC_URL='/static/',
    STATICFILES_DIRS=[os.path.join(os.path.dirname(__file__), 'static')],
)

# Views
def login_view(request):
    return render(request, 'login.html')

def index_view(request):
    return render(request, 'index.html')

# URL Configuration
urlpatterns = [
    url(r'^login/$', login_view),
    url(r'^index/$', index_view),
]

# Run the app
if __name__ == "__main__":
    execute_from_command_line()
