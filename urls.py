from django.urls import path
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os

def verify_webhook(request):
    if request.method == 'GET':
        token = request.GET.get('hub.verify_token')
        challenge = request.GET.get('hub.challenge')
        if token == os.environ.get('VERIFY_TOKEN'):
            return HttpResponse(challenge)
        return HttpResponse('Invalid token', status=403)
    return HttpResponse('OK')

urlpatterns = [
    path('webhook/', csrf_exempt(verify_webhook)),
]
