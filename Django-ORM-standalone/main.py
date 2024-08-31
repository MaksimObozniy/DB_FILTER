import os
import django
import datetime
import math
from django.utils.timezone import localtime, now

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard, Visit  # noqa: E402


def find_suspicious_visits(visits, min_duration_minutes=1000): #передаем список посетитетелей и время, которое ищем, будь то 10 минт или час
    suspicious_visits = [] #создаем пустой список куда будем их добавлять
    for visit in visits:
        if visit.leaved_at is None: #делаем проверку на то, есть ли время выхода
            leaved_at = now() #если нет, то он сейчас там и записываем туда нынешнее время
        else:
            leaved_at = visit.leaved_at #обратная ситуация соответственно есть время выхода
        delta = leaved_at - visit.entered_at
        duration_in_minutes = delta.total_seconds() / 60 #переводим в удобный формат
        if duration_in_minutes > min_duration_minutes:  #проверяем, что время не больше 60 минут, если больше то добавляем в список
            suspicious_visits.append(visit)
    return suspicious_visits
    

if __name__ == '__main__':
    passcards = Passcard.objects.all()
    for passcards in passcards:
        visits = Visit.objects.filter(passcard=passcards)
        suspicious_visits = find_suspicious_visits(visits)
        first_suspect = suspicious_visits
        print(first_suspect)
        
