from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

User = get_user_model()

class Sensor(models.Model):
    # Общие и индуктивные
    marking = models.CharField(max_length=120)
    sens_type = models.CharField(max_length=30)
    case_size = models.CharField(max_length=30, null=True, blank=True)
    mounting = models.CharField(max_length=30, null=True, blank=True)
    sensing_distance = models.CharField(max_length=30, null=True, blank=True)
    connection_type = models.CharField(max_length=30, null=True, blank=True)
    connector = models.CharField(max_length=30, null=True, blank=True)
    cable_length = models.CharField(max_length=30, null=True, blank=True)
    housing = models.CharField(max_length=30, null=True, blank=True)
    standard_size = models.CharField(max_length=30, null=True, blank=True)
    length = models.CharField(max_length=30, null=True, blank=True)
    type_shell = models.CharField(max_length=30, null=True, blank=True)
    size_frame = models.CharField(max_length=30, null=True, blank=True)
    type_current = models.CharField(max_length=30, null=True, blank=True)
    current = models.CharField(max_length=30, null=True, blank=True)
    voltage = models.CharField(max_length=30, null=True, blank=True)
    contact_structure = models.CharField(max_length=30, null=True, blank=True)
    frequency = models.CharField(max_length=30, null=True, blank=True)
    indication = models.CharField(max_length=30, null=True, blank=True)
    electr_protection = models.CharField(max_length=30, null=True, blank=True)
    degree_of_protect = models.CharField(max_length=30, null=True, blank=True)
    num_wires = models.CharField(max_length=30, null=True, blank=True)
    temp_range = models.CharField(max_length=30, null=True, blank=True)
    class_temp = models.CharField(max_length=30, null=True, blank=True)
    work_dist = models.CharField(max_length=30, null=True, blank=True)
    special_assign = models.CharField(max_length=30, null=True, blank=True)
    wiring = models.CharField(max_length=30, null=True, blank=True)
    manufacture = models.CharField(max_length=30, null=True, blank=True)
    delay_range = models.CharField(max_length=30, null=True, blank=True)
    adjustment_speed_range = models.CharField(max_length=30, null=True, blank=True)
    trip_delay = models.CharField(max_length=30, null=True, blank=True)
    umax = models.CharField(max_length=30, null=True, blank=True)
    irab = models.CharField(max_length=30, null=True, blank=True)
    ground = models.CharField(max_length=30, null=True, blank=True)
    max_pressure = models.CharField(max_length=30, null=True, blank=True)
    special_electrical_param = models.CharField(max_length=30, null=True, blank=True)
    vibro_resist = models.CharField(max_length=30, null=True, blank=True)
    out_analog_signal = models.CharField(max_length=30, null=True, blank=True)
    linear_area = models.CharField(max_length=30, null=True, blank=True)
    hole_diameter = models.CharField(max_length=30, null=True, blank=True)
    slot_width = models.CharField(max_length=30, null=True, blank=True)
    ex_marking = models.CharField(max_length=30, null=True, blank=True)
    special_version = models.CharField(max_length=30, null=True, blank=True)
    # Оптические
    breaker_type = models.CharField(max_length=30, null=True, blank=True)
    range_dist = models.CharField(max_length=30, null=True, blank=True)
    spectr = models.CharField(max_length=30, null=True, blank=True)
    sensitiv_adjustment = models.CharField(max_length=30, null=True, blank=True)
    operating_principle = models.CharField(max_length=30, null=True, blank=True)
    light_spot_size = models.CharField(max_length=30, null=True, blank=True)
    resolution = models.CharField(max_length=30, null=True, blank=True)
    display = models.CharField(max_length=30, null=True, blank=True)
    repetition_accuracy = models.CharField(max_length=30, null=True, blank=True)
    response_time = models.CharField(max_length=30, null=True, blank=True)
    protected_height = models.CharField(max_length=30, null=True, blank=True)
    num_beams = models.CharField(max_length=30, null=True, blank=True)
    max_range = models.CharField(max_length=30, null=True, blank=True)
    detection = models.CharField(max_length=30, null=True, blank=True)
    safety_output = models.CharField(max_length=30, null=True, blank=True)
    safety_level = models.CharField(max_length=30, null=True, blank=True)
    # Емкостные
    sensing_surface = models.CharField(max_length=30, null=True, blank=True)
    turn_on_delay = models.CharField(max_length=30, null=True, blank=True)
    turn_off_delay = models.CharField(max_length=30, null=True, blank=True)
    dielectric_constant = models.CharField(max_length=30, null=True, blank=True)
    # Магниточувствительные
    output_function = models.CharField(max_length=30, null=True, blank=True)
    switched_power = models.CharField(max_length=30, null=True, blank=True)
    controlled_level = models.CharField(max_length=30, null=True, blank=True)
    measuring_principle = models.CharField(max_length=30, null=True, blank=True)
    # Блоки сопряжения
    load_current_electronic = models.CharField(max_length=30, null=True, blank=True)
    load_current_relay = models.CharField(max_length=30, null=True, blank=True)
    num_of_connected = models.CharField(max_length=30, null=True, blank=True)
    num_of_relay_outputs = models.CharField(max_length=30, null=True, blank=True)
    num_of_electronic_outputs = models.CharField(max_length=30, null=True, blank=True)
    # Соединители
    nut_material = models.CharField(max_length=30, null=True, blank=True)
    plug_type = models.CharField(max_length=30, null=True, blank=True)
    num_contacts = models.CharField(max_length=30, null=True, blank=True)
    view = models.CharField(max_length=30, null=True, blank=True)
    connect = models.CharField(max_length=30, null=True, blank=True)
    # Влажности и температуры
    relative_output = models.CharField(max_length=30, null=True, blank=True)
    temperature_output = models.CharField(max_length=30, null=True, blank=True)
    relative_range = models.CharField(max_length=30, null=True, blank=True)
    temperature_range = models.CharField(max_length=30, null=True, blank=True)
    relative_accuracy = models.CharField(max_length=30, null=True, blank=True)
    temperature_accuracy = models.CharField(max_length=30, null=True, blank=True)
    temp_measurement_range = models.CharField(max_length=30, null=True, blank=True)
    rel_measurement_range = models.CharField(max_length=30, null=True, blank=True)
    operating_temperature = models.CharField(max_length=30, null=True, blank=True)






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
    difference1 = models.TextField()
    difference2 = models.TextField()
    manufacture_original = models.CharField(max_length=30)

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