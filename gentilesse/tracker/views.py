from django.shortcuts import render, redirect, get_object_or_404 
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

from datetime import date
from tracker.models import *

# Create your views here.

@login_required
def point_add(request, username_to, label_id, amount):
    if username_to and amount:
        user_by = User.objects.get(username=request.user)
        user_to = User.objects.get(username=username_to)
        label = Label.objects.get(name=label_id)
        point = EventPoint(by=user_by,to=user_to,label=label,date=date.today(),points=int(amount))
        point.save()
    else:
        messages.error(request, 'Error adding points')

    return redirect('list-points')


@login_required
def point_list(request):
    #points = EventPoint.objects.all()
    users = User.objects.all()
    labels = Label.objects.all()
    
    c = {
            'users': users,
            'labels': labels,
            }
    return render(request, 'point_list.html', c)


@login_required
def point_edit(request, id):
    if id:
        point = get_object_or_404(EventPoint, pk=id)
    else:
        point = None

    form = PointForm(request.POST or None, instance=point)
    
    if request.method == 'POST' and form.is_valid():
        if id:
            form.save()
            messages.success(request, 'Point modified.')
        return redirect('list-point')

    c = {
            'form': form,
            'point': point,
            }
    return render(request, 'point_edit.html')
    

@login_required
def label_list(request):
    labels = Label.objects.all()
    if not labels:
        messages.info(request, 'Create a label first')
        return redirect('add-label')

    c = {
            'labels': labels,
            }

    return render(request, 'label_list.html', c)


@login_required
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
    return render(request, 'label_edit.html', c)


@login_required
def label_delete(request, name):
    label = get_object_or_404(Label, id=id)
    author = User.objects.get(username=request.user.username)

    for point in label.points.all():
        point.label = None
    label.remove()

    messages.success(request, "Label deleted successfully.")
    return redirect('list-label')





