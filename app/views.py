from django.shortcuts import render

# Create your views here.
def userdefinefilter(request):
    d={'data':'My NaMe Is bALaJi'}
    return render(request,'userdefinefilter.html',d)