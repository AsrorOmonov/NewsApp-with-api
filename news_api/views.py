from django.shortcuts import render


def index(request):
    import requests
    import json

    news_api_requests = requests.get(
        'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=57cf72c8ac934ecc8eb15e31135e4bb3')
    api = json.loads(news_api_requests.content)

    context = {
        'api': api
    }

    return render(request, 'index.html', context)
