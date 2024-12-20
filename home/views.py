from django.shortcuts import redirect, render
from account.authenticate import login_required,admin_login_required
from django.http import HttpResponse
from ps_webapp.models import EventStatus, EventType, EventBookingMaster, AccountProfile
from datetime import datetime,timedelta
from django.utils import timezone
from django.contrib import messages
from ps_webapp.models import UserRoles

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
    context,filter_clause = dict(),dict()
    userid = request.GET.get("userid","")
    status = request.GET.get("status","")
    from_date_str = request.GET.get("from_date","")
    to_date_str = request.GET.get("to_date","")
    loggedin_userid = request.session['userid']

    is_admin = UserRoles.objects.filter(userid=loggedin_userid,role__role_name='Admin').exists()
    if is_admin and userid:
        filter_clause["user_id"] = request.GET.get('userid')

    if not is_admin:
        filter_clause = {'user_id':loggedin_userid }

    if from_date_str and to_date_str:
        from_date = datetime.strptime(from_date_str,'%Y-%m-%d')
        to_date = datetime.strptime(to_date_str,'%Y-%m-%d')+timedelta(days=1)-timedelta(seconds=1)
        filter_clause.update({"event_date__range":(from_date, to_date)})

    if status:
        filter_clause["status__status"]=status

    booking_stats = EventBookingMaster.objects.filter(**filter_clause)
    users = AccountProfile.objects.all()
    status_data = EventStatus.objects.values_list('status', flat=True)

    context.update({
        "booking_stats":booking_stats,
        "users":users,
        "status_data":status_data,
        "is_admin":is_admin,
        "from_date":from_date_str,
        "to_date":to_date_str,
        "userid":int(userid) if userid else '',
        "status":status,
    })
    return render(request, 'home/booking_stats.html',context)


@admin_login_required
def update_booking_request(request, id):
    if request.method == "POST":
        booking_status = request.POST.get("booking_status","")
        id = request.POST.get("id","")
        obj = EventBookingMaster.objects.get(id=id)
        obj.status_id=booking_status
        obj.updated_by_id=request.session["userid"]
        obj.save()
        return redirect('/booking_stats')

    context = {
        "status_data":EventStatus.objects.values_list('status',flat=True),
        "booking_data":EventBookingMaster.objects.get(id=id),
    }
    return render(request, 'home/update_booking_request.html', context)
from django.views.decorators.csrf import csrf_exempt
import json
@csrf_exempt
def eventScheduler(request):
    #print(f"\n\n\nrequest --------------------------- \n {json.loads(json.dumps(request.POST).get('request_data[data]'))}\n\n\n")
    data =  json.loads(request.POST["request_data[data]"])
    for d in data:
        print(d)
    return HttpResponse(request)


def biodata(request):
    return render(request, 'home/biodata.html')
def amt(request):
    return render(request, 'home/amt.html')
