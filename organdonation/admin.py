from django.contrib import admin
from .models import User,Donor, Recipient

# Register your models here.

admin.site.register(User)
admin.site.register(Donor)
admin.site.register(Recipient)