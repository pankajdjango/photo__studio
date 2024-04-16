from django.shortcuts import redirect
from ps_webapp.models import UserRoles

def login_required(get_response):
    def wrapper(request):
        if not request.session.get('userid'):
            return redirect('/account/login.html')
        response = get_response(request)
        return response
    return wrapper


def already_login(get_response):
    def wrapper(request):
        if request.session.get('userid'):
            return redirect('/')
        response = get_response(request)
        return response
    return wrapper



def admin_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not UserRoles.objects.filter(userid=request.session.get('userid'),role__role_name='Admin').exists():
            return redirect('/')
        return view_func(request, *args, **kwargs)
    return wrapper
