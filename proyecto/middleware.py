from ipware import get_client_ip
from django.http import HttpResponse
from .models import Visitantes

BLACK_LIST = [
    ''
]

class IPIsValid():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip, is_routable = get_client_ip(request)
        Visitantes.objects.create(ip=ip)

        if ip in BLACK_LIST:
            return HttpResponse('Bad request', status=404)
        else:
            return self.get_response(request)