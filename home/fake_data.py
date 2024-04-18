import faker
from home import models as md
import random

fake = faker.Faker()


career_fields = [
    "Data Science and Analytics",
    "Healthcare",
    "Cybersecurity",
    "Artificial Intelligence and Machine Learning",
    "Renewable Energy",
    "Financial Services",
    "Environmental Science and Conservation",
    "Digital Marketing and Social Media Management",
    "Education and Training"
]

# NumOfData = 4

def create_data():
    for depart in career_fields:
        md.Department.objects.create(department=depart)

def create_stu(NumOfData) -> None:

    depart_data = md.Department.objects.all()

    for _ in range(NumOfData):

        # Gatting Random Department
        dapartment_index = random.randint(0, len(depart_data) -1)
        department = depart_data[dapartment_index]


        # Generating student uid
        previos_id = md.Student_UID.objects.order_by('-id').first()
        latest_roll = previos_id.uid.split("-")[1]
        rollnum = int(latest_roll)+1
        student_UID = f"STU-{rollnum}"
        

        name = fake.name()
        email = fake.email()
        address = fake.address()
        age = random.randint(18, 50)


        student_uid_instance = md.Student_UID.objects.create(
            uid=student_UID
        )

        md.student.objects.create(
            department = department,
            student_UID = student_uid_instance,
            name = name,
            age = age,
            email = email,
            address = address,
        )