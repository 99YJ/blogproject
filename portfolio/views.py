from django.shortcuts import render
from .models import Portfolio

def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio/portfolio.html', {'portfolios': portfolios})

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs':blogs})