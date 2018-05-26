# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home_page(request):
	return render(request, 'accueil.html')

def search_tweets(request):
	return render(request, 'recherche.html')