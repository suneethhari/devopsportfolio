from django.shortcuts import render

# Create your views here.
def demo(request):
    return render(request,"index.html")
def single(request):
    return render(request,"single.html")

