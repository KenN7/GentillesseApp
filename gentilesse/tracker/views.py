from django.shortcuts import render, redirect, get_object_or_404 
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages

from tracker.models import *
from tracker.forms import * 
import tracker.graph as flot

# Create your views here.

@login_required
def point_add(request, username_to, label_id, amount):
    user_by = User.objects.get(username=request.user)
    user_to = get_object_or_404(User, username=username_to)
    label = get_object_or_404(Label, name=label_id)
    point = EventPoint.objects.create(by=user_by,to=user_to,label=label,points=int(amount))

    return redirect('list-points')


@login_required
def point_list(request):
    points = EventPoint.objects.order_by('-date')[:5]
    users = User.objects.all()
    labels = Label.objects.all()
    gr = flot.Flot()
    #(date, points)
    for user in users:
        tuplist = []
        if user.total_points():
            for p in user.total_points_list():
                tuplist.append((p.date, user.from_begin_points(p.date)))
            gr.add_lines(tuplist)

    
    c = {
            'graph': gr,
            'users': users,
            'labels': labels,
            'points': points,
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
        if label:
            form.save()
            messages.success(request, 'Label modified successfully.')
        else:
            label = form.save(commit=False)
            label.save()
            messages.success(request, 'Label added successfully.')

        return redirect('list-label')
        
    c = {
            'form': form,
            'label': label,
            }
    return render(request, 'label_edit.html', c)


@login_required
@require_http_methods(["POST"])
def label_delete(request, name):
    label = get_object_or_404(Label, name=name)
    label.delete()

    messages.success(request, "Label deleted successfully.")
    return redirect('list-label')





