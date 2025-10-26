import requests
from django.http import HttpRequest, HttpResponse


def my_cool_view(request: HttpRequest) -> HttpResponse:
    response = requests.get("http://api.github.com")
    return HttpResponse(response.text)
