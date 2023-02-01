from textwrap import dedent

from sphinxcontrib.plantuml.encode import encode

def test_encode():
    text = dedent(
        '''
        Alice -> Bob: Authentication Request
        Bob --> Alice: Authentication Response
        '''
    ).strip()

    assert encode(text) == 'Syp9J4vLqBLJSCfFib9mB2t9ICqhoKnEBCdCprC8IYqiJIqkuGBAAUW2rJY256DHLLoGdrUS2W0='
