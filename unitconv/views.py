from django.shortcuts import render
from django.http import JsonResponse


def convert(request):
    response = {"test": "test"}
    return JsonResponse(response)
