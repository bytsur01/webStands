from django.shortcuts import render,  redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SoldierForm, CrgTableOneForm
from django.views.generic import ListView, FormView
from django.views.generic.edit import CreateView
from .models import Soldierdata, CrgTableOne
from django.views.decorators.clickjacking import xframe_options_exempt


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



class Amgt1Create(FormView):
    form_class = CrgTableOneForm
    template_name = 'stands/amgt1view.html'
    fields = '__all__'


    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(Amgt1Create, self).form_valid(form)


class SoldierList(ListView):
    model = Soldierdata
