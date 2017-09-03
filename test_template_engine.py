import unittest
import re

VAR_TOKEN_START = '{{'
VAR_TOKEN_END = '}}'
BLOCK_TOKEN_START = '{%'
BLOCK_TOKEN_END = '%}'
TOK_REGEX = re.compile(r"(%s.*?%s|%s.*?%s)" % (
    VAR_TOKEN_START,
    VAR_TOKEN_END,
    BLOCK_TOKEN_START,
    BLOCK_TOKEN_END
))

class TestTemplateEngine(unittest.TestCase):
    def test_tokenizer(self):
        self.assertEqual(
        TOK_REGEX.split('{% each vars %}<i>{{it}}</i>{% endeach %}'),
        ['', '{% each vars %}', '<i>', '{{it}}', '</i>', '{% endeach %}', ''])

if __name__ == '__main__':
    unittest.main()
