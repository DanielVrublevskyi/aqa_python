from faker import Faker

fake = Faker("en_US")

def generate_first_name():
        return fake.first_name()

def generate_last_name():
    return fake.last_name()

def generate_email():
    return f"auto_{fake.uuid4()[:8]}@example.com"

def generate_password():
    return fake.password(
        length=12,
        special_chars=False,
        digits=True,
        upper_case=True,
        lower_case=True
    )