from gendiff import render
from gendiff import parser
from gendiff import generate_diff
from tests.fixtures import expected_result

RESULT = '''{
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''

RESULT_COMPLEX = '''{
    common: {
        setting1: Value 1
      - setting2: 200
        setting3: true
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
      - setting6: {
            key: value
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
    }
  - group2: {
        abc: 12345
    }
  + group3: {
        fee: 100500
    }
}'''


def test():
    assert render.string_diff(generate_diff.get_diff(
        parser.get_set('./tests/fixtures/before.json'),
        parser.get_set('./tests/fixtures/after.json'),
        )) == RESULT
    assert render.string_diff(generate_diff.get_diff(
        parser.get_set('./tests/fixtures/before.yml'),
        parser.get_set('./tests/fixtures/after.yml'),
        )) == RESULT
    assert render.string_diff(generate_diff.get_diff(
        parser.get_set('./tests/fixtures/before_complex.json'),
        parser.get_set('./tests/fixtures/after_complex.json'),
        )) == RESULT_COMPLEX
