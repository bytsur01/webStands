from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from .forms import SoldierForm
from django.views.generic.list import ListView
from .models import Soldierdata


# Create your views here.


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SoldierForm(request.POST or None)

        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required

            # redirect to a new URL:
            return redirect('index')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SoldierForm()

    return render(request, 'index.html', {'form': form})


class SoldierList(ListView):
    model = Soldierdata
