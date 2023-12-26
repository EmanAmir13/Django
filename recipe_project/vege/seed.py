from faker import Faker

fake = Faker()
import random
from .models import *


def seed_db(n=10) -> None:
    try:
        for i in range(0, n):
            department_obj = Department.objects.all()
            random_index = random.randint(0, len(department_obj)-1)
            student_id = f'STU-0{random.randint(100, 999)}'
            department = department_obj[random_index]
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(20, 30)
            student_address = fake.address()

            student_id_obj = StudentID.objects.create(student_id=student_id)

            student_obj = Student.objects.create(
                department=department,
                student_id=student_id,
                student_name=student_name,
                student_email=student_email,
                student_age=student_age,
                student_address=student_address
            )
    except Exception as e:
        print(e)
