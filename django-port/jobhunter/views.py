from django.shortcuts import render, redirect
from .models import Application
from .forms import ApplicationForm

def application_list(request):
    applications = Application.objects.all()
    return render(request, 'application_list.html', {'applications': applications})

def application_create(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('application_list')
    else:
        form = ApplicationForm()
    return render(request, 'application_form.html', {'form': form})

def application_update(request, pk):
    application = Application.objects.get(pk=pk)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('application_list')
    else:
        form = ApplicationForm(instance=application)
    return render(request, 'application_form.html', {'form': form})

def application_delete(request, pk):
    application = Application.objects.get(pk=pk)
    application.delete()
    return redirect('application_list')
