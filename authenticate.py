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


from django.shortcuts import render

class Custom404Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Check if response status code is 404
        if response.status_code == 404:
            # Render custom 404 page
            return render(request, '404.html', status=404)

        return response

