from django.contrib import admin
from .models import User,Donor, Recipient, Organ

# Register your models here.

admin.site.register(User)
admin.site.register(Donor)
admin.site.register(Recipient)
admin.site.register(Organ)