# Two models are supported: ligature and non-ligature, represented by 0 and 1 respectively.

class Latin:
    def __int__(self, model=0):
        self.ligature = {'a': 'æ', 'o': 'œ', 'A': 'Æ', 'O': 'Œ'}
        self.macron = {'a': 'ā', 'e': 'ē', 'i': 'ī', 'o': 'ō', 'u': 'ū', 'y': 'ȳ', 'A': 'Ā', 'E': 'Ē', 'I': 'Ī',
                       'O': 'Ō', 'U': 'Ū', 'Y': 'Ȳ', 'æ': 'ǣ', 'Æ': 'Ǣ'}
        self.last = ''  # the last character input to the command line
        self.parsed = ""  # parsed text
        self.error = -1  # the index where an error begins, -1 if there is no error
        self.model = model  # ligature model by default

    def parse(self, text):
        pass

