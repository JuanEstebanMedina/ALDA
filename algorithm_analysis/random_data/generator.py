import random
import string
import os

# Module to generate random data
def random_number(start=1000000, end=99999999):
    return random.randint(start, end)

def random_string(length=10, alphabet=string.ascii_letters + string.digits):
    return ''.join(random.choices(alphabet, k=length))

def random_string_from_file(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File {filename} not found.")
    with open(filename, 'r') as file:
        lines = file.readlines()
    return random.choice([line.strip() for line in lines if line.strip()])

def random_set_of_ids(size=5, start=1000000, end=99999999):
    return {random.randint(start, end) for _ in range(size)}

def random_alphanumeric_id(min_length=9, max_length=15, chars="ABCDEFG0987654321"):
    length = random.randint(min_length, max_length)
    return ''.join(random.choices(chars, k=length))

def random_email(domain_list=None):
    if domain_list is None:
        domain_list = ["gmail.com", "yahoo.com", "outlook.com"]
    user = random_string(length=random.randint(5, 10), alphabet=string.ascii_lowercase + string.digits)
    domain = random.choice(domain_list)
    return f"{user}@{domain}"

def random_colombian_address():
    streets = ["Calle", "Carrera", "Avenida", "Diagonal", "Transversal"]
    zones = ["Norte", "Sur", "Este", "Oeste", "Centro"]
    street_num = random.randint(1, 150)
    house_num = random.randint(1, 100)
    return f"{random.choice(streets)} {street_num} #{house_num}-{random.randint(1, 50)}, {random.choice(zones)}"

# if __name__ == "__main__":
    # print("Random Number:", random_number())
    # print("Random String:", random_string())
    # print("Random ID Set:", random_set_of_ids())
    # print("Random Alphanumeric ID:", random_alphanumeric_id())
    # print("Random Email:", random_email())
    # print("Random Colombian Address:", random_colombian_address())
