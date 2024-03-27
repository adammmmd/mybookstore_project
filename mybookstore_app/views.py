from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def landing(request):
    context = {}
    context['Bukus'] = TabelBuku.objects.all()
    print(context['Bukus'])
    return render(request, 'landing.html', context)