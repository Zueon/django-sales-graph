import pandas as pd
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib import messages
from .forms import SalesSearchForm
from .models import *


# Create your views here.
from .utils import get_chart


def sales(request):
    search_form = SalesSearchForm(request.POST or None)
    context = {'search_form' : search_form}
    return render(request, 'sales.html', context)