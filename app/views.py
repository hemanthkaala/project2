from django.shortcuts import render

# Create your views here.
def awm(request):
    return render(request,"staticfile.html")