from django import forms
from django.forms.models import modelform_factory

from tracker.models import *

LabelForm = modelform_factory(Label, fields=['name', 'color', 'inverted'])
