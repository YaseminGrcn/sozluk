from django.shortcuts import render, render_to_response
from django.views.generic import View
from sozluk.models import Entry


def post_list(request):
    template_path = 'sozluk/entry_list.html'
    context = {}
    all_entry = Entry.objects.all()
    entry_list = []
    if all_entry:
        for entry in all_entry:
            entry_list.append(entry)
    context['entry_body'] = entry_list
    return render(request, template_path, context)
