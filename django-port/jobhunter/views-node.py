``
from django.shortcuts import render, redirect
from .models import Application
import requests

def application_list(request):
    applications = Application.objects.all()
    return render(request, 'application_list.html', {'applications': applications})

def application_create(request):
    if request.method == 'POST':
        coverletter_id = request.POST['coverletter_id']
        role_id = request.POST['role_id']
        resume_id = request.POST['resume_id']
        date_submitted = request.POST['date_submitted']
        response = requests.post('http://localhost:3000/applications', json={
            'coverletter_id': coverletter_id,
            'role_id': role_id,
            'resume_id': resume_id,
            'date_submitted': date_submitted
        })
        if response.status_code == 201:
            return redirect('application_list')
        else:
            return render(request, 'application_create.html', {'error': 'Error creating application'})
    return render(request, 'application_create.html')

def application_update(request, pk):
    application = Application.objects.get(pk=pk)
    if request.method == 'POST':
        coverletter_id = request.POST['coverletter_id']
        role_id = request.POST['role_id']
        resume_id = request.POST['resume_id']
        date_submitted = request.POST['date_submitted']
        response = requests.put(f'http://localhost:3000/applications/{pk}', json={
            'coverletter_id': coverletter_id,
            'role_id': role_id,
            'resume_id': resume_id,
            'date_submitted': date_submitted
        })
        if response.status_code == 200:
            return redirect('application_list')
        else:
            return render(request, 'application_update.html', {'error': 'Error updating application'})
    return render(request, 'application_update.html', {'application': application})

def application_delete(request, pk):
    application = Application.objects.get(pk=pk)
    response = requests.delete(f'http://localhost:3000/applications/{pk}')
    if response.status_code == 204:
        return redirect('application_list')
    else:
        return render(request, 'application_delete.html', {'error': 'Error deleting application'})
