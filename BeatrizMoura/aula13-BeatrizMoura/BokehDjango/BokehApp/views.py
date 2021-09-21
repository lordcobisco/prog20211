from django.shortcuts import render
from django.http import HttpResponse
from bokeh.plotting import figure
from bokeh.embed import components


# Create your views here.

def home(request):
    plot = figure(plot_width = 400, plot_height = 400)
    plot = circle([1,2,3,4,5], [6,7,8,9,1], plot_width = 400, plot_height = 400)

    
    return HttpResponse('Isso aparece quando vc digita http://127.0.0.1:8000')
