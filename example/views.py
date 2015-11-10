from django.http import HttpResponse

from example.conf import settings

def homepage(request):
    return HttpResponse("<body><h2>Hello, the setting is: {0}</h2></body>".format(
        settings.EXAMPLE_MY_EXTRA_SETTING
    ))
