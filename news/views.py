from django.shortcuts import render
import requests
import API_KEY
def get_articles(category="all", lang="ru", pageSize=100):
    response = requests.get(
        f"https://newsapi.org/v2/everything?q={category}&language={lang}&pageSize={pageSize}&apiKey={API_KEY}"
    )
    data = response.json()
    if data["status"] != "ok":
        print("[!] Ошибка в получении новостей")
        return
    return data["articles"]


def homepage_view(request):
    news = get_articles(category="Minecraft", pageSize=12)
    return render(request, "index.html", {"news": news})


# TO-DO: создать страницу about.html
def favourite(request): ...
