from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):

    return render(request,"index.html")

def calculate(request):
    x= int(request.GET['num1'])
    y= int(request.GET['num2'])
    res1=x+y
    res2=x-y
    res3=x*y
    res4=x/y
    return render(request, "result.html", {'res1': res1, 'res2':res2,'res3':res3,'res4':res4})
