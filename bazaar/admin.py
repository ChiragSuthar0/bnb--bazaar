from django.contrib import admin
from .models import Firm
from .models import Trader
from .models import Update

# Register your models here.

admin.site.register(Firm)
admin.site.register(Trader)
admin.site.register(Update)
