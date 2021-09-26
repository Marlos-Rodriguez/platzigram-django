"""platzigram Views"""
# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime

from json import dumps


def sort(request):
    numbers = [int(i) for i in request.GET.get('numbers').split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Success'
    }
    return HttpResponse(dumps(data), content_type='application/json')


def age(request, name, age):
    """Return a greeting"""
    if age < 12:
        message = F'Sorry {name} you are not allowed here'
    else:
        message = F'Hello {name}, Welcome to Platzigram'

    return HttpResponse(message)
