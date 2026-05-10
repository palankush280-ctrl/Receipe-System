from faker import Faker
fake = Faker()
import random

def seed_db(n=10)->None:
    for i in range(0,n):
        student_name = fake.name()
        student_email = fake.email()
        student_age = random.randint(20)
        student_address = fake.address()
        
