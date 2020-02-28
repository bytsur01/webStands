from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import SoldierForm


# Create your views here.


def index(request):
    context = {}

    # create object of form
    form = SoldierForm(request.POST or None, request.FILES or None)

    # check if the 1st form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        # refresh the page without data upon submit
        return HttpResponseRedirect(reverse('index'))

    context['form'] = form
    return render(request, "base.html", context)

