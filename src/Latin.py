from src.Lang import Lang


class Latin(Lang):
    def __int__(self, model=0):
        super().__init__()
        self.configured = False  # representing the result of configuration
        self.active = False  # representing the typing process of specific language
        self.ligature = {'a': 'æ', 'o': 'œ', 'A': 'Æ', 'O': 'Œ'}
        self.macron = {'a': 'ā', 'e': 'ē', 'i': 'ī', 'o': 'ō', 'u': 'ū', 'y': 'ȳ', 'A': 'Ā', 'E': 'Ē', 'I': 'Ī',
                       'O': 'Ō', 'U': 'Ū', 'Y': 'Ȳ', 'æ': 'ǣ', 'Æ': 'Ǣ'}
        self.last = ''  # the last character that has been parsed
        self.error = -1  # the index where an error begins, -1 if there is no error
        self.model = model  # 0 for ligature (by default) and 1 for non-ligature

    def parse(self, text):
        pass
