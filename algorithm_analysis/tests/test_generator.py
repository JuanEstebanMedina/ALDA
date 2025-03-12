import pytest
import string
from algorithm_analysis.random_data import generator


def test_random_number():
    num = generator.random_number()
    assert isinstance(num, int)
    assert 1000000 <= num <= 99999999


def test_random_string():
    rand_str = generator.random_string(12)
    assert isinstance(rand_str, str)
    assert len(rand_str) == 12
    assert all(c in string.ascii_letters + string.digits for c in rand_str)


def test_random_string_from_file(tmp_path):
    file_path = tmp_path / "sample_words.txt"
    sample_words = "apple\nbanana\ncherry\n"
    file_path.write_text(sample_words)

    rand_str = generator.random_string_from_file(str(file_path))
    assert rand_str in ["apple", "banana", "cherry"]

    with pytest.raises(FileNotFoundError):
        generator.random_string_from_file("not_existing_file.py")


def test_random_string_from_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        generator.random_string_from_file("nonexistent_file.txt")


def test_random_set_of_ids():
    ids = generator.random_set_of_ids(10)
    assert isinstance(ids, set)
    assert len(ids) == 10
    for id_ in ids:
        assert isinstance(id_, int)
        assert 1000000 <= id_ <= 99999999


def test_random_alphanumeric_id():
    rand_id = generator.random_alphanumeric_id()
    assert isinstance(rand_id, str)
    assert 9 <= len(rand_id) <= 15
    valid_chars = set("ABCDEFG0987654321")
    assert all(c in valid_chars for c in rand_id)


def test_random_email():
    email = generator.random_email()
    assert "@" in email and "." in email.split("@")[-1]


def test_random_colombian_address():
    address = generator.random_colombian_address()
    assert isinstance(address, str)
    assert any(char.isdigit() for char in address)
    assert any(char.isalpha() for char in address)
