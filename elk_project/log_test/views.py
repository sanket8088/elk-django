from django.shortcuts import render
from django.http import HttpResponse
import logging
logger = logging.getLogger(__name__)


def student_show(request):
    logger.info('Something went wrong!')
    x = []
    for i in range(10):
        x.append(i)
    return HttpResponse("<h1>DataFlair Django Tutorials</h1>The Digits are {0}".format(x))