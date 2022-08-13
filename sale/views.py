import pandas as pd
from django.shortcuts import render
from django.views.generic import ListView
from .forms import SalesSearchForm


# Create your views here.
def sales(request):
    search_form = SalesSearchForm(request.POST or None)
    context = {'search_form' : search_form}
    return render(request, 'sales.html', context)