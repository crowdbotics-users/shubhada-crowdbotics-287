from django.shortcuts import render

# Create your views here.

from home.models import CustomText, HomePage


def home(request):
    packages = [
	{'name':'django-rest-framework', 'url': 'http://pypi.python.org/pypi/django-rest-framework/0.1.0'},
	{'name':'graphene-django', 'url': 'http://pypi.python.org/pypi/graphene-django/2.0.0'},
	{'name':'django-social-auth', 'url': 'http://pypi.python.org/pypi/django-social-auth/0.7.28'},
	{'name':'django-social-auth', 'url': 'http://pypi.python.org/pypi/django-social-auth/0.7.28'},
	{'name':'django-guardian', 'url': 'http://pypi.python.org/pypi/django-guardian/1.4.9'},
	{'name':'django-allauth', 'url': 'http://pypi.python.org/pypi/django-allauth/0.34.0'},
    ]
    context = {
        'customtext': CustomText.objects.first(),
        'homepage': HomePage.objects.first(),
        'packages': packages
    }
    return render(request, 'home/index.html', context)
