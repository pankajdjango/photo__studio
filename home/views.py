from django.shortcuts import redirect, render
from authenticate import login_required
from django.http import HttpResponse

# Create your views here.
@login_required
def index(request):
    context = dict()
    return render(request, 'home.html',context)

def custom_404(request, exception):
    return HttpResponse("404 Page Not Found ...", status=404)

