import random
from start.constants import email_length, generator_collection, password_length


def random_email_generate():
    return ''.join(random.choice(generator_collection) for _ in range(email_length)).lower() + '@qa.qa'


def random_password_generate():
    return ''.join(random.choice(generator_collection) for _ in range(password_length))
