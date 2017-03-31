from django.shortcuts import render
# from django.http import Http404

# Create your views here.


def Index(request):
    return render(request, 'twitter_search/index.html')

