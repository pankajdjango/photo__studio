from django.shortcuts import redirect, render
from account.authenticate import login_required
from django.http import HttpResponse
from ps_webapp.models import EventStatus, EventType, EventBookingMaster, AccountProfile
from datetime import datetime
from django.utils import timezone
from django.contrib import messages

# Create your views here.
@login_required
def index(request):
    context = dict()
    messages_list = messages.get_messages(request)
    context["message"] = messages_list
    return render(request, 'home/home.html',context)


@login_required
def booknow(request):
    context = dict()
    if request.method=='POST':
        print(request.POST)
        city_id = request.POST.get("city_id",None)
        area_address = request.POST.get("area_address",None)
        mobile = request.POST.get("mobile",None)
        message = request.POST.get("message",None)
        event_id = request.POST.get("event_id",None)
        event_date = request.POST.get("event_date",None)
        userid=request.session['userid']
        event_date_ist = datetime.strptime(event_date, '%Y-%m-%dT%H:%M').astimezone(timezone.get_current_timezone())
        try:
            EventBookingMaster(city_id=city_id,message=message,event_date=event_date_ist,mobile=mobile,area_address=area_address,event_id=event_id,user_id=userid).save()
            messages.success(request, "Your Booking Request Sent Successfully.")
        except Exception as e:
            messages.error(request, "Something went wrong. Please try again.")
        return redirect('/', **context)
    context["event_type"] = EventType.objects.values()
    return render(request, 'home/booknow.html',context)


@login_required
def about(request):
    context = dict()
    return render(request, 'home/about.html',context)

@login_required
def photoshoot(request):
    context = dict()
    return render(request, 'home/photoshoot.html',context)

@login_required
def gallery(request):
    context = dict()
    return render(request, 'home/gallery.html',context)

@login_required
def booking_stats(request):
    context = dict()
    userid = request.session['userid']
    context["booking_stats"] = EventBookingMaster.objects.filter(user_id=userid)

    return render(request, 'home/booking_stats.html',context)
