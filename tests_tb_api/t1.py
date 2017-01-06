# encoding=utf-8


class TextService(object):
    def upper(self, text):
        return {
            'text': text.upper()
        }

    def method_exception(self):
        raise Exception('Exception in-side method')
