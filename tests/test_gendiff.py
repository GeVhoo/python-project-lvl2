from gendiff import format
from gendiff import loader
from gendiff import diff

EXPECTED_SIMPLE = './tests/fixtures/expected_result/expected_simple.txt'
EXPECTED_COMPLEX = './tests/fixtures/expected_result/expected_complex.txt'
EXPECTED_PLAIN = './tests/fixtures/expected_result/expected_plain.txt'
EXPECTED_JSON = './tests/fixtures/expected_result/expected_json.json'


def get_expected_result(path):
    with open(path) as file:
        return file.read().rstrip()


def test_string_simple():
    assert format.default(diff.get(
        loader.load('./tests/fixtures/before.json'),
        loader.load('./tests/fixtures/after.json'),
        )) == get_expected_result(EXPECTED_SIMPLE)


def test_string_yaml():
    assert format.default(diff.get(
        loader.load('./tests/fixtures/before.yml'),
        loader.load('./tests/fixtures/after.yml'),
        )) == get_expected_result(EXPECTED_SIMPLE)


def test_string_complex():
    assert format.default(diff.get(
        loader.load('./tests/fixtures/before_complex.json'),
        loader.load('./tests/fixtures/after_complex.json'),
        )) == get_expected_result(EXPECTED_COMPLEX)


def test_plain():
    assert format.plain(diff.get(
        loader.load('./tests/fixtures/before_complex.json'),
        loader.load('./tests/fixtures/after_complex.json'),
        )) == get_expected_result(EXPECTED_PLAIN)


def test_json():
    assert format.json(diff.get(
        loader.load('./tests/fixtures/before_complex.json'),
        loader.load('./tests/fixtures/after_complex.json'),
        )) == get_expected_result(EXPECTED_JSON)
