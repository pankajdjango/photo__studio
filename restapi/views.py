from django.http import JsonResponse
from ps_webapp.models import CityMaster
import json

# Create your views here.
def country_state_city_list(request):
    city_term = request.GET.get('city[term]',None)
    try:
        if city_term:
            results = CityMaster.objects.filter(city__icontains=city_term,country_code='IN').values('city_id','city', 'state__state', 'state__country_code__name')
            return JsonResponse(data=list(results), status=200, safe=False)
    except Exception as e:
        return JsonResponse(data=json.dumps({"error": "Something went wrong!"}), status=500, safe=False)
