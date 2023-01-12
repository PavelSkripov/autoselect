from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

User = get_user_model()

class Sensor(models.Model):
    marking = models.CharField(max_length=120)
    case_size = models.CharField(max_length=60)
    mounting = models.CharField(max_length=60)
    sensing_distance = models.CharField(max_length=60)
    connection_type = models.CharField(max_length=60)
    housing = models.CharField(max_length=60)
    diameter = models.CharField(max_length=60)
    length = models.CharField(max_length=60)
    type_shell = models.CharField(max_length=60)
    size_frame = models.CharField(max_length=60)
    current = models.CharField(max_length=60)
    voltage = models.CharField(max_length=60)
    contact_structure = models.CharField(max_length=60)
    frequency = models.CharField(max_length=60)
    indication = models.CharField(max_length=60)
    electr_protection = models.CharField(max_length=60)
    degree_of_protect = models.CharField(max_length=60)
    num_wires = models.IntegerField()
    temp_range = models.CharField(max_length=60)
    work_dist = models.CharField(max_length=60)
    special = models.CharField(max_length=60)
    wiring = models.CharField(max_length=60)
    manufacture = models.CharField(max_length=60)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.marking


    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('sensor-detail', args=[str(self.id)])


class Analog(models.Model):
    marking = models.CharField(max_length=120)
    marking_analog = models.ManyToManyField(Sensor)
    difference = models.TextField()
    manufacture_original = models.CharField(max_length=60)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.marking


    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('analog-detail', args=[str(self.id)])