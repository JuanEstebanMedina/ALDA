import random
import string
import os


def random_number(start=1000000, end=99999999):
    """
    Generates a random number within a specified range.

    Args:
        start (int): The lower bound of the range (inclusive). Default is 1,000,000.
        end (int): The upper bound of the range (inclusive). Default is 99,999,999.

    Returns:
        int: A randomly generated number within the range.
    """
    return random.randint(start, end)


def random_string(length=10, alphabet=string.ascii_letters + string.digits):
    """
    Generates a random alphanumeric string of a specified length.

    Args:
        length (int): The length of the string to generate. Default is 10.
        alphabet (str): The set of characters to use for the string. Default is letters and digits.

    Returns:
        str: A randomly generated string.
    """
    return "".join(random.choices(alphabet, k=length))


def random_string_from_file(filename):
    """
    Selects a random string from a file, where each line is treated as a potential string.

    Args:
        filename (str): The path to the file containing strings.

    Returns:
        str: A randomly selected string from the file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File {filename} not found.")
    with open(filename, "r") as file:
        lines = file.readlines()
    return random.choice([line.strip() for line in lines if line.strip()])


def random_list_of_ids(size=5, start=1000000, end=99999999):
    """
    Generates a list of random IDs within a specified range.

    Args:
        size (int): The number of IDs to generate. Default is 5.
        start (int): The lower bound of the range (inclusive). Default is 1,000,000.
        end (int): The upper bound of the range (inclusive). Default is 99,999,999.

    Returns:
        list: A list of randomly generated IDs.
    """
    return [random.randint(start, end) for _ in range(size)]


def random_set_of_ids(size=5, start=1000000, end=99999999):
    """
    Generates a set of unique random IDs within a specified range.

    Args:
        size (int): The number of IDs to generate. Default is 5.
        start (int): The lower bound of the range (inclusive). Default is 1,000,000.
        end (int): The upper bound of the range (inclusive). Default is 99,999,999.

    Returns:
        set: A set of unique randomly generated IDs.
    """
    return {random.randint(start, end) for _ in range(size)}


def random_alphanumeric_id(min_length=9, max_length=15, chars="ABCDEFG0987654321"):
    """
    Generates a random alphanumeric ID of a specified length.

    Args:
        min_length (int): The minimum length of the ID. Default is 9.
        max_length (int): The maximum length of the ID. Default is 15.
        chars (str): The set of characters to use for the ID. Default is "ABCDEFG0987654321".

    Returns:
        str: A randomly generated alphanumeric ID.
    """
    length = random.randint(min_length, max_length)
    return "".join(random.choices(chars, k=length))


def random_email(domain_list=None):
    """
    Generates a random email address.

    Args:
        domain_list (list): A list of domains to choose from. Default is ["gmail.com", "yahoo.com", "outlook.com"].

    Returns:
        str: A randomly generated email address.
    """
    if domain_list is None:
        domain_list = ["gmail.com", "yahoo.com", "outlook.com"]
    user = random_string(
        length=random.randint(5, 10), alphabet=string.ascii_lowercase + string.digits
    )
    domain = random.choice(domain_list)
    return f"{user}@{domain}"


def random_colombian_address():
    """
    Generates a random Colombian address.

    Returns:
        str: A randomly generated address in the Colombian format.
    """
    streets = ["Calle", "Carrera", "Avenida", "Diagonal", "Transversal"]
    zones = ["Norte", "Sur", "Este", "Oeste", "Centro"]
    street_num = random.randint(1, 150)
    house_num = random.randint(1, 100)
    return f"{random.choice(streets)} {street_num} #{house_num}-{random.randint(1, 50)}, {random.choice(zones)}"


def random_existing_value_from_list(lst):
    """
    Returns a random element from a non-empty list.

    Args:
        lst (list): The list to choose a value from.

    Returns:
        element: A randomly selected element from the list.

    Raises:
        ValueError: If the list is empty.
        TypeError: If the input is not a list.
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if not lst:
        raise ValueError("List cannot be empty")
    return random.choice(lst)


# if __name__ == "__main__":
# print("Random Number:", random_number())
# print("Random String:", random_string())
# print("Random ID Set:", random_set_of_ids())
# print("Random Alphanumeric ID:", random_alphanumeric_id())
# print("Random Email:", random_email())
# print("Random Colombian Address:", random_colombian_address())
