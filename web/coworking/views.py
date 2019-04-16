import logging
from django.shortcuts import render

logger = logging.getLogger('rocdev')


def index(request):
    return render(
        request, 'coworking/index.html')
