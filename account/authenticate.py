from django.shortcuts import redirect


def login_required(get_response):
    def middleware(request):
        if not request.session.get('userid'):
            return redirect('/account/login.html')
        response = get_response(request)
        return response
    return middleware


def already_login(get_response):
    def middleware(request):
        if request.session.get('userid'):
            return redirect('/')
        response = get_response(request)
        return response
    return middleware
