from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Fixture)
admin.site.register(FixtureGainType)
admin.site.register(CustomTaxRate)