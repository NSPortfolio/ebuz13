from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone

class Post(models.Model):
    bakeries = "Bakeries"
    organization = (
        (bakeries, "Bakeries"),
    )
    environment = "Environment"
    stem = "STEM"
    readwrite = "Reading/Writing"
    musicart = "Music/Art"
    other = "Other"
    interest = (
        (environment, "Environment"),
        (stem, "STEM"),
        (readwrite, "Reading/Writing"),
        (musicart, "Music/Art"),
        (other, "Other"),
    )
    inperson = "In-Person"
    online = "Shipping and Pickup"
    communication = (
        (inperson, "In-Person"),
        (online, "Shipping and Pickup"),
    )

    inperson = "Yes"
    online = "No"
    yes = (
        (inperson, "Yes"),
        (online, "No"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=255, blank=True)
    name_of_organization = models.CharField(max_length=255, unique=True)
    organization = models.CharField(max_length=255, choices=organization, default=bakeries)
    interest = models.CharField(max_length=255, choices=interest, default=environment)
    website = models.URLField(max_length=255, blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    communication = models.CharField(max_length=255, choices=communication, default=online)
    yes = models.CharField(max_length=255, choices=yes, default=inperson)
    description = models.TextField(null=True, blank=False)
    looking = models.TextField(null=True, blank=False)
    update = models.TextField(null=True, blank=False)
    recentevent = models.CharField(max_length=255, null=True, blank=False)
    saved = models.ManyToManyField(User, related_name='saved', blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name_of_organization

