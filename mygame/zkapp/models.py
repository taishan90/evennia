from __future__ import unicode_literals


from django.db import models

# Create your models here.
class MyDataStore(models.Model):
    "A simple model for storing some data" 
    db_key = models.CharField(max_length=80, db_index=True)
    db_category = models.CharField(max_length=80, null=True, blank=True)
    db_text = models.TextField(null=True, blank=True)
    # we need this one if we want to be 
    # able to store this in an Evennia Attribute!
    db_date_created = models.DateTimeField('date created', editable=False,
                                            auto_now_add=True, db_index=True)
"""
from evennia.utils.idmapper.models import SharedMemoryModel

class MyDataStore(SharedMemoryModel):
    # the rest is the same as before, but db_* is important; these will
    # later be settable as .key, .category, .text ...
    db_key = models.CharField(max_length=80, db_index=True)
    db_category = models.CharField(max_length=80, null=True, blank=True)
    db_text = models.TextField(null=True, blank=True)
    db_date_created = models.DateTimeField('date created', editable=False,
                                            auto_now_add=True, db_index=True)       
"""