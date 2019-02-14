from django.core.management.base import BaseCommand

from students.models import Student, StudentLab, Lab, LabSection
import random

class Command(BaseCommand):

    def handle(self, *args, **options):
        student_names = ['Matthew', 'Aloysius', 'Scott', 'Josh', 'Richard', 'Daniel', 'Tod', 'Joseph', 'Josephine', 'Johan', 'Joe']
        lab_names = ['Guess the Number', 'Mad Lab', 'Turtle', 'Contact List', 'Clock', 'Calculator']
        section_names = ['Python', 'HTML+CSS', 'JavaScript', 'Django']

        # PURGE DATA
        StudentLab.objects.all().delete()
        Student.objects.all().delete()
        Lab.objects.all().delete()
        LabSection.objects.all().delete()

        for i, section_name in enumerate(section_names):
            lab_section = LabSection(name=section_name, index=(i+1))
            lab_section.save()

            for j in range(3):
                lab_name = random.choice(lab_names)
                lab = Lab(name=lab_name, section=lab_section, index=(j+1))
                lab.save()

        lab_sections = LabSection.objects.all()
        for student_name in student_names:
            student = Student(name=student_name)
            student.save()

            for lab_section in lab_sections:
                for lab in lab_section.lab_set.all():
                    if random.randint(1,10) == 1:
                        continue
                    student_lab = StudentLab(student=student, lab=lab, grade=random.choice([True, True, True, True, False]))
                    student_lab.save()
