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
