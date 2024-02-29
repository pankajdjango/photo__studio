from django.shortcuts import redirect, render
from authenticate import login_required


# Create your views here.
@login_required
def index(request):
    context = dict()
    return render(request, 'home.html',context)
