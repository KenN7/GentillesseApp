from django.db import models
from django.contrib import auth
from django.db.models import Sum
from django.core.validators import RegexValidator

from colorful import fields

# Create your models here.
class User(auth.models.User):
    
    class Meta:
        proxy = True

    def total_points(self):
        return self.points.aggregate(Sum('points'))['points__sum']

    def daily_points(self, date):
        return self.points.filter(date=date).aggregate(Sum('points'))['points__sum']

    def from_begin_points(self, date):
        return self.points.filter(date__lte=date).aggregate(Sum('points'))['points__sum']

    def total_points_list(self):
        return self.points.all()

    def daily_points_list(self):
        return self.points.filter(date=date).points.all()

    def from_begin_points_list(self, date):
        return self.points.filter(date__lte=date).points.all()


class Label(models.Model):
    name_validator = RegexValidator(regex='^[A-Za-z0-9_-]+$',
            message="Please enter only characters, number, underscores or hyphens.")
    name = models.CharField(max_length=20, unique=True, validators=[name_validator])
    color = fields.RGBColorField(default="#000000",verbose_name="Background color")
    inverted = models.BooleanField(default=True)

    def total_label_points(self):
        return self.points.aggregate(Sum('points'))['points__sum']

    def label_points_list(self):
        return self.points.all()

    def __str__(self):
        return self.name


class EventPoint(models.Model):
    by = models.ForeignKey(User, related_name='from')
    to = models.ForeignKey(User, related_name='points')
    label = models.ForeignKey(Label, related_name='points')
    date = models.DateTimeField(auto_now_add=True)
    points = models.IntegerField()

    def __str__(self):
        return '%s->%s:%s' % (self.by.username,self.to.username,self.points)

