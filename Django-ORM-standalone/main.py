import os
import django
import datetime
import math
from django.utils.timezone import localtime, now

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard, Visit  # noqa: E402


def find_suspicious_visits(visits, min_duration_minutes=1000): 
    suspicious_visits = []
    for visit in visits:
        if visit.leaved_at is None:
            leaved_at = now() 
        else:
            leaved_at = visit.leaved_at 
        delta = leaved_at - visit.entered_at
        duration_in_minutes = delta.total_seconds() / 60 
        if duration_in_minutes > min_duration_minutes:
            suspicious_visits.append(visit)
    return suspicious_visits
    

if __name__ == '__main__':
    passcards = Passcard.objects.all()
    for passcards in passcards:
        visits = Visit.objects.filter(passcard=passcards)
        suspicious_visits = find_suspicious_visits(visits)
        first_suspect = suspicious_visits
        print(first_suspect)
        
