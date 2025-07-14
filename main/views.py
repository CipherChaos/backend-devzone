from django.shortcuts import render

def home(request):
    age = 19
    context = {"age": age}
    return render(request, "home.html",context)
