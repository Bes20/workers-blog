from django.shortcuts import render
from .models import Workers
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/login')
def all_workers(request):
    workers = Workers.objects.all()
    return render(request, 'workers_list.html', {'work': workers})
