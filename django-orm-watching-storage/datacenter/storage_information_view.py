from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def duration_at(visits):
    now = localtime()
    then = visits.entered_at
    delta = now - then
    result = (str(delta).split('.')[0])
    return result


def storage_information_view(request):
    # Программируем здесь

    visit = Visit.objects.all()
    for visits in visit:
        if visits.leaved_at == None:
            owner = visits.passcard
            
    non_closed_visits = [
        {
            'who_entered': owner.owner_name,
            'entered_at': visits.entered_at,
            'duration': duration_at(visits),
        }
    ]
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
