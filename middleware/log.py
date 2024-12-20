import requests,time
from django.utils.deprecation import MiddlewareMixin
from ps_webapp.models import RequestLog

class LogRequestMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip_address = request.META.get('REMOTE_ADDR')
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        path = request.get_full_path()
        method = request.method

        # Extract vendor and OS system from user-agent
        vendor, os_system = self.parse_user_agent(user_agent)

        # Fetch location and coordinates
        location_data = self.get_location(ip_address)
        if 'error' not in location_data:
            location = location_data.get('city', '')
            latitude = location_data.get('latitude')
            longitude = location_data.get('longitude')

            RequestLog.objects.create(
                ip_address=ip_address,
                user_agent=user_agent,
                path=path,
                method=method,
                vendor=vendor,
                os_system=os_system,
                location=location,
                latitude=latitude,
                longitude=longitude,
                additional_info=location_data
            )
        else:
            print("\n\n\n#################################################Skipping Request Log#########################################################\n\n\n")

    def parse_user_agent(self, user_agent):
        # Basic parsing of user-agent string (extend as needed)
        vendor = "Unknown Vendor"
        os_system = "Unknown OS"
        
        if "Windows" in user_agent:
            os_system = "Windows"
        elif "Macintosh" in user_agent:
            os_system = "MacOS"
        elif "Linux" in user_agent:
            os_system = "Linux"
        
        if "Chrome" in user_agent:
            vendor = "Google"
        elif "Firefox" in user_agent:
            vendor = "Mozilla"
        # Add more parsing logic as needed
        
        return vendor, os_system

    def get_location(self, ip_address):
        # additional_info | {"ip": "182.75.165.126", "loc": "28.5498,77.2651", "org": "AS9498 BHARTI Airtel Ltd.", "city": "New Delhi", "postal": "110020", "readme": "https://ipinfo.io/missingauth", "region": "Delhi", "country": "IN", "hostname": "nsg-static-126.165.75.182-airtel.com", "latitude": 28.5498, "timezone": "Asia/Kolkata", "longitude": 77.2651}
        generated = time.time()-(86400/4)
        resp = RequestLog.objects.filter(ip_address=ip_address,generated__gt=generated).first()
        # import pdb;pdb.set_trace()
        if resp:
            data = resp.additional_info
            print(f"\n\n\nresp additional_info :{data}\n\n\n")
        else:
            # Replace with your IP geolocation API URL
            api_url = f"https://ipinfo.io/{ip_address}/json"
            response = requests.get(api_url)
            data = response.json()
        print("data,",data)
        data.update({
            'latitude': None,
            'longitude': None
        })
        
        if 'loc' in data:
            location = data['loc'].split(',')
            data['latitude'] = float(location[0])
            data['longitude'] = float(location[1])
        
        return data
