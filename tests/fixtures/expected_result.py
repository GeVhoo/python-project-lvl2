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

PLAIN_RESULT = """Property 'common.setting2' was removed
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: 'complex value'
Property 'common.setting6' was removed
Property 'group1.baz' was changed. From 'bas' to 'bars'
Property 'group2' was removed
Property 'group3' was added with value: 'complex value'"""

JSON_RESULT = '''{
    "common": {
        "condition": "children",
        "value": {
            "setting1": {
                "condition": "same",
                "value": "Value 1"
            },
            "setting2": {
                "condition": "removed",
                "value": "200"
            },
            "setting3": {
                "condition": "same",
                "value": true
            },
            "setting4": {
                "condition": "add",
                "value": "blah blah"
            },
            "setting5": {
                "condition": "add",
                "value": {
                    "key5": "value5"
                }
            },
            "setting6": {
                "condition": "removed",
                "value": {
                    "key": "value"
                }
            }
        }
    },
    "group1": {
        "condition": "children",
        "value": {
            "baz": {
                "after_value": "bars",
                "before_value": "bas",
                "condition": "changed"
            },
            "foo": {
                "condition": "same",
                "value": "bar"
            }
        }
    },
    "group2": {
        "condition": "removed",
        "value": {
            "abc": "12345"
        }
    },
    "group3": {
        "condition": "add",
        "value": {
            "fee": "100500"
        }
    }
}'''
