from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'household/index.html', context)