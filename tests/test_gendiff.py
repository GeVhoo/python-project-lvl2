from gendiff import format
from gendiff import parsers
from gendiff import generate_diff

EXPECTED_SIMPLE = './tests/fixtures/expected_result/expected_simple.txt'
EXPECTED_COMPLEX = './tests/fixtures/expected_result/expected_complex.txt'
EXPECTED_PLAIN = './tests/fixtures/expected_result/expected_plain.txt'
EXPECTED_JSON = './tests/fixtures/expected_result/expected_json.json'


def get_expected_result(path):
    with open(path) as file:
        return file.read().rstrip()


def test_string_simple():
    assert format.default(generate_diff.get_diff(
        parsers.get_set('./tests/fixtures/before.json'),
        parsers.get_set('./tests/fixtures/after.json'),
        )) == get_expected_result(EXPECTED_SIMPLE)


def test_string_yaml():
    assert format.default(generate_diff.get_diff(
        parsers.get_set('./tests/fixtures/before.yml'),
        parsers.get_set('./tests/fixtures/after.yml'),
        )) == get_expected_result(EXPECTED_SIMPLE)


def test_string_complex():
    assert format.default(generate_diff.get_diff(
        parsers.get_set('./tests/fixtures/before_complex.json'),
        parsers.get_set('./tests/fixtures/after_complex.json'),
        )) == get_expected_result(EXPECTED_COMPLEX)


def test_plain():
    assert format.plain(generate_diff.get_diff(
        parsers.get_set('./tests/fixtures/before_complex.json'),
        parsers.get_set('./tests/fixtures/after_complex.json'),
        )) == get_expected_result(EXPECTED_PLAIN)


def test_json():
    assert format.json(generate_diff.get_diff(
        parsers.get_set('./tests/fixtures/before_complex.json'),
        parsers.get_set('./tests/fixtures/after_complex.json'),
        )) == get_expected_result(EXPECTED_JSON)
