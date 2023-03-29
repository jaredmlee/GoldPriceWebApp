from django.shortcuts import render


def index(request):
    return render(request, 'gold/gold.html')


def plan(request):
    return render(request, 'gold/plan.html')