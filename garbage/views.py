from django.http import HttpResponse, Http404
from .models import Garbage
from django.shortcuts import render


def index(request):
    latest_garbage_list = Garbage.objects.order_by("type_of_garbage")
    context = {"latest_garbage_list": latest_garbage_list}
    return render(request, "garbage/index.html", context)


def detail(request, garbage_id):
    try:
        garbage = Garbage.objects.get(pk=garbage_id)
    except Garbage.DoesNotExist:
        raise Http404("Garbage has been cleared, fear not soldier")
    return render(request, "garbage/detail.html", {"garbage": garbage})