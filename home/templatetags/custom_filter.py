from ps_webapp.models import CityMaster
from django import  template
from django.db import connection

register=template.Library()

@register.filter(name='city_name')
def city_name(city_id):
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT city,state FROM general.city_master WHERE city_id = {city_id}")
        rows , = cursor.fetchall()
    return f"{rows[0]} ({rows[1]})"


@register.filter(name='epoch_timestamp')
def epoch_timestamp(generated):
    if not generated:return ""
    with connection.cursor() as cursor:
        cursor.execute(f"select to_timestamp({generated})::timestamp")
        rows , = cursor.fetchall()
    return f"{rows[0]}"


@register.filter(name='timestamp')
def timestamp(event_date):
    if not event_date:return ""
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT (TIMESTAMP WITH TIME ZONE '{event_date}')::timestamp")
        rows , = cursor.fetchall()
    return f"{rows[0]}"
