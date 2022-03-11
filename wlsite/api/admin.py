from asyncio import tasks
from django.contrib import admin
from .models import ContactForm, Activity, Customer, Logs, Team, Role, ResourceLink, Task, Worker, Project

admin.site.register(ContactForm)
admin.site.register(Activity)
admin.site.register(Customer)
admin.site.register(Team)
admin.site.register(Role)
admin.site.register(ResourceLink)
admin.site.register(Task)
admin.site.register(Worker)
admin.site.register(Project)
admin.site.register(Logs)