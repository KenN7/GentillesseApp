from django.db import models
from colorful import fields
import datetime
from django.contrib import auth

# Create your models here.
class User(auth.models.User):
    
    class Meta:
        proxy = True

    def total_points(self):
        return sum(self.points.points.all())

    def daily_points(self, date):
        return sum(self.points.filter(date=date).points.all())

    def from_begin_points(self, date):
        return sum(self.points.filter(date__lt=date).points.all())

    def total_points_list(self):
        return self.points.all()

    def daily_points_list(self):
        return self.points.filter(date=date).points.all()

    def from_begin_points_list(self, date):
        return self.points.filter(date__lt=date).points.all()


class Label(models.Model):
    name = models.CharField(max_length=20)
    color = fields.RGBColorField(default="#000000",verbose_name="Background color")

    def total_label_points(self):
        return sum(self.points.all())

    def label_points_list(self):
        return self.points.all()

    def __str__(self):
        return self.name


class EventPoint(models.Model):
    by = models.ForeignKey(User, related_name='from')
    to = models.ForeignKey(User, related_name='points')
    label = models.ForeignKey(Label, blank=True, null=True, related_name='points')
    date = models.DateField()
    points = models.IntegerField()

    def __str__(self):
        return self.by

