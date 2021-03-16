from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    return render(request, "ajax/index.html")


def compute(request):
    a, b = request.POST.get("a"), request.POST.get("b")
    return JsonResponse({"operation_result": int(a) + int(b)})
