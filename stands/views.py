from django.shortcuts import render, HttpResponseRedirect
from .forms import SoldierForm
from django_tables2 import SingleTableView, RequestConfig
from .tables import Soldiertable
from .models import *


# Create your views here.


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SoldierForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('base.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SoldierForm()

    return render(request, 'base.html', {'form': form})


def soldierinfo(request):
    table = Soldiertable(Soldierdata.objects.all())
    model = Soldierdata
    table_class = Soldiertable
    RequestConfig(request).configure(table)
    return render(request, 'base.html', {'table1': table})
