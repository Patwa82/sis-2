import csv
from django.core.management.base import BaseCommand
from course_management.models import CollegeProgram, Branch, Subject

class Command(BaseCommand):
    help = 'Import College Program data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Split the dates field if there are two dates (start and end)
                dates = row['dates'].split(',')
                start_date = dates[0] if len(dates) > 0 else None
                end_date = dates[1] if len(dates) > 1 else None

                # Insert or get CollegeProgram
                program, created = CollegeProgram.objects.get_or_create(
                    program=row['program'],
                    description=row['description'],
                    enrollment_term=row['enrollment_term'],
                    defaults={'dates': row['dates']}
                )

                # Insert or get Branch
                branch, created = Branch.objects.get_or_create(
                    name=row['branch_name'],
                    program=program
                )

                # Insert or get Subject
                subject, created = Subject.objects.get_or_create(
                    name=row['subject_name'],
                    branch=branch
                )

            self.stdout.write(self.style.SUCCESS("Data imported successfully"))
