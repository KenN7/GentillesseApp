from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

from tracker.models import *

# Create your views here.


def login(request):

    c = {
            }
    return render(request, 'template/login.html', c)

def point_list(request):
    points = EventPoint.objects.all()
    if not points:
        messages.info(request, 'Add points first')
    
    c = {

            }
    return render(request, 'template/point_list.html', c)

def point_edit(request, id):
    if id:
        point = get_object_or_404(EventPoint, pk=id)
    else:
        point = None

    form = PointForm(request.POST or None, instance=point)
    
    if request.method == 'POST' and form.is_valid():
        if label:
            form.save()
            messages.success(request, 'Point modified.')
        else:
            point = form.save()
            point.by = user
            point.save()
            messages.success(request, 'Success !')

        return redirect('list-point')

    c = {
            'form': form,
            'point': point,
            }
    return render(request, 'template/point_edit.html')
    


def label_list(request):
    labels = Label.objects.all()
    if not labels:
        messages.info(request, 'Create a label first')
        return redirect('add-label')

    c = {
            'labels': labels,
            }

    return render(request, 'template/label_list.html', c)


def label_edit(request, name=None):
    if name:
        label = get_object_or_404(Label, name=name)
    else:
        label = None

    form = LabelForm(request.POST or None, instance=label)

    if request.method == 'POST' and form.is_valid():
        similar = Label.objects.filter(name=form.cleaned_data['name'])
        
        if label:
            similar = similar.exclude(pk=label.pk)
        if similar.exists():
            form._errors['name'] = ['There is already a label with this name.']
        else:
            if label:
                form.save()
                messages.success(request, 'Label modified successfully.')
            else:
                label = form.save(commit=False)
                label.project = project
                label.save()
                messages.success(request, 'Label added successfully.')

        point = request.GET.get('point')
        if point:
            return redirect('add-label-to-point', point, label.name)

        return redirect('list-label')
        
    c = {
            'form': form,
            'label': label,
            }
    return render(request, 'template/label_edit.html', c)


    def label_delete(request, name):
        label = get_object_or_404(Label, id=id)
        author = User.objects.get(username=request.user.username)
        
        for point in label.points.all():
            point.label = None
        label.remove()

        messages.success(request, "Label deleted successfully.")

        return redirect('list-label')





