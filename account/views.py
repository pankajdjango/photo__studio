from django.shortcuts import render, redirect
from . models import Photographer, Client, Location, EventType, Event, BookingRequest, Photo, Payment, Review, Notification
from django.http import HttpResponse
from ps_webapp.models.AccountProfile import AccountProfile
from authenticate import already_login
# View to handle user registration

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
            obj = AccountProfile.objects.filter(email=email,password=password).first()
            if obj:
                request.session["userid"] = obj.userid
                request.session["username"] = obj.full_name
                return redirect("/")
            else:
                context.update({"login_error":f"Invalid Email or Password !","login":True})
        else:
            try:
                AccountProfile(full_name=full_name,email=email, mobile=mobile, password= password, city_id=city_id).save()
                context["signup_succes"]=f"Signup successful. Please login."
                context["login"]=True
            except Exception as e:
                context["signup_error"]="Something went wrong! Please try again."
    print(f"################################## {'account/signup_login.html'}")
    return render(request,"account/signup_login.html",context)


# View to handle user logout
def logout(request):
    # Logic to log out user
    request.session.clear()
    # Redirect to home page or login page
    return redirect('/')



    # Create your views here.
    # def profile(request):
    #     return render(request,"account/profile.html")

def home(request):
    # Logic to display the home page
    return render(request, 'home.html')

def photographer_profile(request, photographer_id):
    photographer = Photographer.objects.get(pk=photographer_id)
    # Logic to display photographer's profile
    return render(request, 'photographer_profile.html', {'photographer': photographer})

def client_profile(request, client_id):
    client = Client.objects.get(pk=client_id)
    # Logic to display client's profile
    return render(request, 'client_profile.html', {'client': client})

def event_details(request, event_id):
    event = Event.objects.get(pk=event_id)
    # Logic to display event details
    return render(request, 'event_details.html', {'event': event})

def book_event(request, event_id):
    if request.method == 'POST':
        event = Event.objects.get(pk=event_id)
        client = request.user.client
        # Logic to book the event
        booking_date = request.POST.get('booking_date')
        message = request.POST.get('message')
        # Additional logic for booking
        booking_request = BookingRequest.objects.create(client=client, event=event, booking_date=booking_date, message=message)
        # Redirect to event details page after booking
        return redirect('event_details', event_id=event_id)
    else:
        # Render form to book event
        event = Event.objects.get(pk=event_id)
        return render(request, 'book_event.html', {'event': event})

def make_payment(request, booking_id):
    if request.method == 'POST':
        booking_request = BookingRequest.objects.get(pk=booking_id)
        amount = request.POST.get('amount')
        payment_method = request.POST.get('payment_method')
        transaction_id = request.POST.get('transaction_id')
        # Logic to make payment
        payment = Payment.objects.create(booking=booking_request, amount=amount, payment_method=payment_method, transaction_id=transaction_id)
        # Additional logic after payment
        return redirect('booking_confirmation', booking_id=booking_id)
    else:
        # Render payment form
        booking_request = BookingRequest.objects.get(pk=booking_id)
        return render(request, 'make_payment.html', {'booking_request': booking_request})

def booking_confirmation(request, booking_id):
    booking_request = BookingRequest.objects.get(pk=booking_id)
    # Logic to display booking confirmation
    return render(request, 'booking_confirmation.html', {'booking_request': booking_request})

# View to display user dashboard
def dashboard(request):
    if request.user.is_authenticated:
        # Logic to display user-specific dashboard
        # Retrieve user's bookings, events, notifications, etc.
        return render(request, 'dashboard.html')
    else:
        # Redirect to login page if user is not authenticated
        return redirect('login')

# View to handle booking cancellation
def cancel_booking(request, booking_id):
    if request.method == 'POST':
        # Logic to cancel booking
        # Update booking status or delete booking
        return redirect('dashboard')
    else:
        # Render confirmation page for booking cancellation
        booking = BookingRequest.objects.get(pk=booking_id)
        return render(request, 'cancel_booking.html', {'booking': booking})

# View to handle event search
def search_events(request):
    if request.method == 'POST':
        # Logic to search for events based on user input
        # Display search results
        return render(request, 'search_results.html', {'events': events})
    else:
        # Render search form
        return render(request, 'search_events.html')

# View to handle event filtering
def filter_events(request):
    if request.method == 'POST':
        # Logic to filter events based on user preferences
        # Display filtered events
        return render(request, 'filtered_events.html', {'events': events})
    else:
        # Render filtering options
        return render(request, 'filter_events.html')

# View to handle event booking history
def booking_history(request):
    if request.user.is_authenticated:
        # Logic to retrieve user's booking history
        # Display booking history
        return render(request, 'booking_history.html', {'bookings': bookings})
    else:
        # Redirect to login page if user is not authenticated
        return redirect('login')
