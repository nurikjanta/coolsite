from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import  render
from women.models import Women


#
# def index(reguest):
#     return render(reguest, "index.html")
#
#
# def about(reguest):
#     return render(reguest, "about.html")
#
# def categories(reguest, cats_id):
#     return  HttpResponse(f"<h1>Статия по категориям<h1/> {cats_id}")

#
# def index(request):
#     data = {"header": "hello Django", "message": "Welcome to Python"}
#     return render(request, "index.html", context=data)

#
# def index(request):
#     header = "Данные пользователя"  # обычная переменная
#     langs = ["Python", "Java", "C#"]  # список
#     user = {"name": "Tom", "age": 23}  # словарь
#     address = ("Абрикосовая", 23, 45)  # кортеж
#
#     data = {"header": header, "langs": langs, "user": user, "address": address}
#     return render(request, "index.html", context=data)


# def about(request):
#     header = 'Рассказываю о себе'
#     langs = ['English', 'Russia', 'Spanish', 'French', "China"]
#     user = ['Shulamita', 'Sakura', 'Naruto', 'Hurem', 'Hinata', 'Erzhan'
#             , 'Aicholpon', 'Killua']
#     address = ("Ottava", "Ankara", "Madrid", "Kanoha", "Rome", "Paris", "Amsterdam")
#
#     data = {"header": header, "langs": langs, "user": user, "address": address}
#     return render(request, "about.html", context=data)

menu = ["О сайте", "Добавить статью", "Обратная связь", " Войти"]


def index(reguest):
    posts = Women.objects.all()
    data = {"menu": menu, 'title': 'главная строница', 'posts': posts}
    return render(reguest, "index.html", data)



# def about(reguest):
#     # posts = Women.objects.all()
#     data = {"menu": menu, 'title': 'О сайте'}
#     return render(reguest, "index.html", data)