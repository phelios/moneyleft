from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from moneyleft.models import EntryForm, Entry

def index(request):
    return HttpResponse("Hello World")

def add_item(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        form.save()
        return HttpResponseRedirect("/")
    else:
        form = EntryForm()

    return render(request, 'add.html', {'form': form})

def list(request):
    entries = Entry.objects.all()
    return render(request, 'entry_list.html', {'entries' : entries})
