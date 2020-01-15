from gendiff.formatters import string, plain, json
from gendiff import parsers
from gendiff import generate_diff
from tests.fixtures import expected_result


def test_string():
    assert string.output(generate_diff.get_diff(
        parsers.get_set('./tests/fixtures/before.json'),
        parsers.get_set('./tests/fixtures/after.json'),
        )) == expected_result.RESULT
    assert string.output(generate_diff.get_diff(
        parsers.get_set('./tests/fixtures/before.yml'),
        parsers.get_set('./tests/fixtures/after.yml'),
        )) == expected_result.RESULT
    assert string.output(generate_diff.get_diff(
        parsers.get_set('./tests/fixtures/before_complex.json'),
        parsers.get_set('./tests/fixtures/after_complex.json'),
        )) == expected_result.RESULT_COMPLEX


def test_plain():
    assert plain.output(generate_diff.get_diff(
        parsers.get_set('./tests/fixtures/before_complex.json'),
        parsers.get_set('./tests/fixtures/after_complex.json'),
        )) == expected_result.PLAIN_RESULT


def test_json():
    assert json.output(generate_diff.get_diff(
        parsers.get_set('./tests/fixtures/before_complex.json'),
        parsers.get_set('./tests/fixtures/after_complex.json'),
        )) == expected_result.JSON_RESULT
