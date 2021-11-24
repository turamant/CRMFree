from django.contrib import admin

from apps.leads.models import Lead, User, Agent, UserProfile

admin.site.register(Lead)
admin.site.register(User)
admin.site.register(Agent)
admin.site.register(UserProfile)