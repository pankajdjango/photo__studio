from ps_webapp.models import CityMaster
from django import  template
from django.db import connection
from datetime import datetime
import pytz

register=template.Library()

@register.filter(name='city_name')
def city_name(city_id):
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT city,state FROM general.city_master WHERE city_id = {city_id}")
        rows , = cursor.fetchall()
    return f"{rows[0]} ({rows[1]})"


@register.filter(name='epoch_timestamp')
def epoch_timestamp(generated):
    if not generated:
        return ""
    timestamp = datetime.fromtimestamp(generated)
    return timestamp.strftime("%Y-%m-%d %H:%M:%S")



@register.filter(name='timestamp')
def timestamp(event_date):
    if not event_date:
        return ""
    ist_timezone = pytz.timezone('Asia/Kolkata')
    event_date_ist = event_date.astimezone(ist_timezone)
    formatted_date = event_date_ist.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_date
