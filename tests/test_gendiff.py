import pytest
import json
from gendiff import output
from gendiff.open_file import open_json

RESULT = '''{
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}'''


def test():
    assert output.generate_diff(
        open_json.get_set('./tests/fixtures/before.json'),
        open_json.get_set('./tests/fixtures/after.json'),
        ) == RESULT
