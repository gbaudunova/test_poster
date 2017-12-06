# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib import auth
from .forms import PortalForm
from .list_portals import list_portals
from .tasks import auth_portal
from .models import Portal


def catch_portal_form(request):
    if request.method == 'POST':
        portal_form = PortalForm(request.POST or None)
        return portal_form
    else:
        return redirect('/main/')


def portal_verification(request):
    form = catch_portal_form(request)
    if form.is_valid():
        create_new_portal = form.save(commit=False)
        portal = find_selected_portal(request)
        return create_new_portal, portal

    else:
        messages.error(request, "Форма не валидна")
        return redirect('/main/')


def create_portal(request):
    data = portal_verification(request)
    create_new_portal = data[1]
    portal = data[0]
    if Portal.objects.filter(name=create_new_portal['name']):
        messages.error(request, "Портал %s уже существует в вашем списке!" % portal['name'])
    else:
        auth_portal_complate = auth_portal(portal, auth, request)
        if auth_portal_complate == True:
            user = auth.get_user(request).username
            create_new_portal.user = user
            create_new_portal.save()
            return redirect('/main/')
        else:
            messages.error(request, "Не получилось аутентифицироваться на портале %s" % portal['name'])


def find_selected_portal(request):
    for i in range(len(list_portals)):
        if list_portals[i].get('name') == request.POST.get('portals'):
            portal = list_portals[i]
            return portal


def delete_portal(request, id_portal):
    portal = Portal.objects.filter(pk=id_portal)
    portal.delete()
    return redirect('/main/')
