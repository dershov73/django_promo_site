from django.core.management.base import BaseCommand
from mainapp.models import Organization, Work, Education
from datetime import date


class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):
        organizations = [
            {'name': 'ЗАО "НСС"',
             'region': 'Ульяновск', 'tax_id': 123456, 'site': 'rt.ru'},
            {'name': 'ООО "Центр Повышения Энергетической Эффективности"',
             'region': 'Ульяновск', 'tax_id': 666122, 'site': 'www.cpee.ru'},
            {'name': 'ООО "ГК Магистраль"',
             'region': 'Москва', 'tax_id': 123456, 'site': 'www.magistral-group.com'},
        ]
        works = [
            {'organization': 'ЗАО "НСС"', 'position': 'Специалист справочной службы',
             'duties': 'Консультация абонентов по услугам связи',
             'start': date(2011, 6, 30), 'end': date(2013, 11, 17)},
            {'organization': 'ООО "Центр Повышения Энергетической Эффективности"', 'position': 'Инженер проектировщик',
             'duties': 'Проектирование внешних систем водоснабжения и водоотведения',
             'start': date(2014, 4, 18), 'end': date(2015, 3, 31)},
            {'organization': 'ООО "ГК Магистраль"', 'position': 'Инженер по планированию',
             'duties': 'Календарное, ресурсное и финансовое планирование проектов',
             'start': date(2015, 4, 1), 'end': date.today()},
        ]
        learns = [
            {'university': 'Ульяновский Государственный Технический Университет',
             'site': 'www.ulstu.ru', 'department': 'Энергетический факультет',
             'speciality': 'Промышленная теплоэнергетика',
             'start': date(2009, 9, 1), 'end': date(2014, 7, 15)
             },
            {'university': 'GeekBrains',
             'site': 'geekbrains.ru', 'department': 'Python',
             'speciality': 'Python/Django',
             'start': date(2017, 4, 6), 'end': date.today()
             },
        ]

        Organization.objects.all().delete()
        for organization in organizations:
            organization = Organization(**organization)
            organization.save()

        Work.objects.all().delete()
        for work in works:
            org_name = work["organization"]
            organization = Organization.objects.get(name=org_name)
            work['organization'] = organization
            work = Work(**work)
            work.save()

        Education.objects.all().delete()
        for learn in learns:
            learn = Education(**learn)
            learn.save()

