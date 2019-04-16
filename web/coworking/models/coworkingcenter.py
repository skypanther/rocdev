from django.db import models


class CoworkingCenter(models.Model):
    # Name    Location    Drop-in rate    Plans   Trial offerings Size    Ammenities  Notes
    center_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    address = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    plans_url = models.CharField(max_length=255, blank=True, null=True)
    trial = models.CharField(max_length=255, blank=True, null=True)
    amenities = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
