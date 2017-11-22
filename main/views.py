from django.shortcuts import render, redirect
from django.contrib import auth
from .tasks import register_users
from portal.forms import PortalForm
from portal.models import Portal


def catch_data(request):
    portal_form = PortalForm()
    portals = Portal.objects.filter(user=auth.get_user(request).username)
    context = {
        'portal_form': portal_form,
        'portals': portals,
        'user': auth.get_user(request).username
         }
    if request.method == 'POST':
        portal_form = PortalForm(request.POST or None)
        if request.POST.get('title') == '' and request.POST.get('url') == '':
            context = {
                'empty': 'Это поле обязательное!'
            }
        else:
            if len(requesbt.POST.get('title')) < 5 or len(request.POST.get('title')) > 50:
                context = {
                    'length': 'Заголовок должен быть более 5 и менее 50 символов!'
                }
            else:
                input_data = {
                    'title': request.POST.get('title'),
                    'url': request.POST.get('url'),
                    'description': request.POST.get('description')
                }
                context = {
                    'portal_form': portal_form
                }

                register_users(input_data, portals)
                return redirect('/main/')
    return render(request, 'template.html', context)