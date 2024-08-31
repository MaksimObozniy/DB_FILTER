from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter.models import Visit

def duration_at(visit):
    now = localtime()
    then = visit.entered_at
    delta = now - then
    result = str(delta).split('.')[0]
    return result

def storage_information_view(request):
    non_closed_visits = []

    visits = Visit.objects.filter(leaved_at__isnull=True)
    for visit in visits:
        non_closed_visits.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': duration_at(visit),
        })

    context = {
        'non_closed_visits': non_closed_visits, 
    }
    return render(request, 'storage_information.html', context)
    
