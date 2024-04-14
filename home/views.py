from django.shortcuts import redirect, render
from account.authenticate import login_required
from django.http import HttpResponse
from ps_webapp.models import EventStatus, EventType, EventBookingMaster, AccountProfile
from datetime import datetime
from django.utils import timezone
# Create your views here.
@login_required
def index(request):
    context = dict()
    return render(request, 'home/home.html',context)

# "status" : EventStatus.objects.values_list('status',flat=True),

@login_required
def booknow(request):
    context = dict()
    if request.method=='POST':
        print(request.POST)
        city_id = request.POST.get("city_id",None)  #['214784']
        area_address = request.POST.get("area_address",None)    #['rews sdf']
        mobile = request.POST.get("mobile",None)    #['7983456820']
        message = request.POST.get("message",None)  #['test']
        event_id = request.POST.get("event_id",None)    #['2']
        event_date = request.POST.get("event_date",None)    #['2024-12-31T23:59']
        userid=request.session.get('userid')
        event_date_ist = datetime.strptime(event_date, '%Y-%m-%dT%H:%M').astimezone(timezone.get_current_timezone())
        obj = EventBookingMaster(
                city_id = city_id,
                message = message,
                event_date = event_date_ist,
                mobile = mobile,
                area_address = area_address,
                event_id = event_id,
                user_id = userid
            )
        obj.save()
        print(obj.__dict__)
    context["event_type"] = EventType.objects.values()
    return render(request, 'home/booknow.html',context)


def about(request):
    context = dict()
    return render(request, 'home/about.html',context)

def photoshoot(request):
    context = dict()
    return render(request, 'home/photoshoot.html',context)

def gallery(request):
    context = dict()
    return render(request, 'home/gallery.html',context)
