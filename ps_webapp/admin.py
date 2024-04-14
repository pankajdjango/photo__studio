from django.contrib import admin
from ps_webapp import models


admin.site.register(models.AreaMaster)
admin.site.register(models.CityMaster)
admin.site.register(models.CountryMaster)
admin.site.register(models.CountryStates)
admin.site.register(models.PincodeMaster)
admin.site.register(models.ServiceProviderProfile)
# admin.site.register(models.UserProfile)
admin.site.register(models.UrlHistory)
admin.site.register(models.EventBookingMaster)
