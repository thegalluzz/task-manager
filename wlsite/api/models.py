from datetime import date
from pyexpat import model
from django.db import models

# Create your models here.

class ContactForm(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=25, null=True, blank=True)
    country = models.CharField(max_length=250, null=True, blank=True)
    details = models.CharField(max_length=2000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'contact-form ' + self.first_name + ' ' + self.last_name + ' ' + str(self.date)

    class Meta:
        verbose_name_plural = "Contact Forms"


class Task(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=2500)
    creation_date = models.DateField(auto_now_add=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    completion_percentage = models.FloatField(default=0)
    archived = models.BooleanField(default=False)
    dependencies = models.ManyToManyField('self', related_name='dependencies_task', symmetrical=False, blank=True)

    def __str__(self):
        return 'Task: ' + self.title

class Worker(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)

    def __str__(self):
        return 'Worker: ' + self.first_name + self.last_name


class TaskItem(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=2500)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='task_item')

    def __str__(self):
        return 'Task item: ' + self.title


class Activity(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=2000, null=True, blank=True)
    
    def __str__(self):
        return 'Activity: ' + self.title
    
    class Meta:
        verbose_name_plural = "Activities"


class Customer(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    vat = models.CharField(max_length=250)
    creation_date = models.DateField(auto_now_add=True)
    company_name = models.CharField(max_length=250, blank=True, null=True)
    contact_name = models.CharField(max_length=250, blank=True, null=True)
    contact_email = models.EmailField(max_length=250, blank=True, null=True)
    contact_phone = models.CharField(max_length=250, blank=True, null=True)
    note = models.TextField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return 'Customer: ' + self.first_name + ' ' + self.last_name 


class Team(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=2000, null=True, blank=True)
    workers = models.ManyToManyField(Worker)
    
    def __str__(self):
        return 'Team: ' + self.title


class Role(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=2000, null=True, blank=True)
    workers = models.ManyToManyField(Worker)
    
    def __str__(self):
        return 'Role: ' + self.title


class ResourceLink(models.Model):
    url = models.URLField(max_length=2000, null=True, blank=True)
    title = models.CharField(max_length=250)

    def __str__(self):
        return 'Resource Link: ' + self.title


class Priority(models.Model):
    title = models.CharField(max_length=250)
    
    def __str__(self):
        return 'Priority: ' + self.title


class Project(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=2000, null=True, blank=True)
    customer = models.ManyToManyField(Customer)
        
    def __str__(self):
        return 'Priority: ' + self.title


class Logs(models.Model):
    description = models.TextField(max_length=2000, null=True, blank=True)
    activity = models.ManyToManyField(Activity)
    date = models.DateField(auto_now_add=True)