from django.db import models

DAYS_OF_WEEK = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
)

# Create your models here.
class Employee(models.Model):
    """Model representing a book genre."""
    id = models.IntegerField(primary_key=True,
                          help_text='Unique ID for this employee')
    surnname = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    day_off1 = models.IntegerField(choices=DAYS_OF_WEEK)
    day_off2 = models.IntegerField(choices=DAYS_OF_WEEK)
    regular_login = models.TimeField(max_length=50)
    regular_logout = models.TimeField(max_length=50)


    def __int__(self):
        """String for representing the Model object."""
        return self.id


class TimeRecord(models.Model):
    owner = models.ForeignKey(Employee, on_delete=models.RESTRICT)
    time_in = models.TimeField()
    time_out = models.TimeField()

    def __str__(self):
        """String for representing the Model object."""
        return self.owner

