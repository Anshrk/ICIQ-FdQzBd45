from django.http import HttpResponse, Http404
from .models import Garbage
from .forms import GarbageForm
from django.shortcuts import render, redirect
from accounts.forms import CustomUserCreationForm


def index(request):
    if request.method == "POST":
        f = GarbageForm(request.POST)
        f.save()

        
    form = GarbageForm()
    latest_garbage_list = Garbage.objects.order_by("type_of_garbage")
    context = {"latest_garbage_list": latest_garbage_list, "form": form}


    return render(request, "garbage/index.html", context)


def detail(request, garbage_id):
    try:
        garbage = Garbage.objects.get(pk=garbage_id)
    except Garbage.DoesNotExist:
        raise Http404("Garbage has been cleared, fear not soldier")
    print('+'.join(garbage.location.split(" ")))
    return render(request, "garbage/detail.html", {"garbage": garbage, "location": '+'.join(garbage.location.split(" "))})

def signup(request): 
    # print(request.method)
    # if request.method == 'POST':  
    #     form = CustomUserCreationForm()  
    #     print("retext")
    #     if form.is_valid(): 
    #         print("Hello world") 
    #         form.save()
    #     else:
    #         print(form.error_messages)
    #         print("Hello world")
    #     return redirect("garbage:index")
    # else:
    #     form = CustomUserCreationForm()  
    #     context = {  
    #         'form':form,
    #     }  
    #     return render(request, 'garbage/register.html', context) 
    return redirect('admin/')