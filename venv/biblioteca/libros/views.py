from django.shortcuts import render

# Create your views here.
def home1(request):
    context = locals()
    template = 'home.html'
    return render(request,template, context)
