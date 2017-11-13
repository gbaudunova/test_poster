from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .forms import MainForms
from .tasks import register_users


def catch_data(request):
    form = MainForms()
    context = {
        'title': 'Main',
        'form': form,
    }

    if request.method == 'POST':
        portals = [
            request.POST.get('hackernews')
        ]
        input_data = {
            'title': request.POST.get('title'),
            'url': request.POST.get('url'),

        }
        register_users(input_data)

        return redirect('/')
    return render(request, 'template.html', context)

