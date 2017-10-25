from django.shortcuts import render_to_response
from datetime import date
from .models import Work, Education, Organization

NOW = date.today()


def main(request):
    name = 'Денис'
    surname = 'Ершов'
    birth_date = date(1991, 1, 6)
    description_1 = 'Добро пожаловать на сайт начинающего django-разработчика.'
    description_2 = 'Пожалуй, лучшего django-разработчика по мнению его кота.'
    return render_to_response("index.html", {'name': name, 'surname': surname, 'birth_date': birth_date,
                                             'description_1': description_1, 'description_2': description_2, 'NOW': NOW})


def work(request):
    place_of_work = Work.objects.all()
    return render_to_response("about_work.html", {'place_of_work': place_of_work, 'NOW': NOW})


def education(request):
    place_of_learn = Education.objects.all()
    return render_to_response("about_education.html", {'place_of_learn': place_of_learn, 'NOW': NOW})


def organization(request, org_id):
    org = Organization.objects.get(id=org_id)
    return render_to_response("organization.html", {'org': org})
