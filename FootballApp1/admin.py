from django.contrib import admin

# Register your models here.
from django.contrib import admin

from FootballApp1.models import Player, Team
admin.site.register(Player)
admin.site.register(Team)

