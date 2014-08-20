from django.conf.urls import url

urlpatterns = [
        url(r'^$', 'tracker.views.point_list', name='list-points'),
        url(r'^label/list$', 'tracker.views.label_list', name='list-label'),
        url(r'^label/(?P<name>[A-Za-z0-9_.-]+)/edit$', 'tracker.views.label_edit', name='edit-label'),
        url(r'^label/(?P<name>[A-Za-z0-9_.-]+)/delete$', 'tracker.views.label_delete', name='delete-label'),
        url(r'^points/add/(?P<username_to>[A-Za-z0-9_.-]+)/(?P<amount>[0-9]+)/(?P<label_id>[A-Za-z0-9_.-]+)$', 'tracker.views.point_add', name='add-points'),
        url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
        url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),

]
