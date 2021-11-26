from django.contrib import admin

from main_app.models import Feeding, Finch, Toy

admin.site.register(Finch)
admin.site.register(Feeding)
admin.site.register(Toy)
