from django.shortcuts import render, redirect
from ps_webapp.models.AccountProfile import AccountProfile
from account.authenticate import already_login


@already_login
def signup_login(request):
    context = dict()
    if request.method == 'POST':
        full_name = request.POST.get("full_name",None)
        email = request.POST.get("email",None)
        mobile = request.POST.get("mobile",None)
        password = request.POST.get("password",None)
        city_id = request.POST.get("city_id",None)
        login = request.POST.get("login",None)
        if login:
            user = AccountProfile.objects.filter(email=email,password=password).first()
            if user:
                request.session.update({"userid":user.userid,"username":user.full_name})
                return redirect("/")
            else:
                context.update({"login_error":f"Invalid Email or Password !","login":True})
        else:
            try:
                AccountProfile(full_name=full_name,email=email, mobile=mobile, password= password, city_id=city_id).save()
                context.update({"signup_succes":f"Signup successful. Please login.","login":True})
            except Exception as e:
                context["signup_error"]="Something went wrong! Please try again."
    return render(request,"account/signup_login.html",context)


def logout(request):
    request.session.clear()
    return redirect('/')
