# 泛拉丁文，包括拉丁文元音字母所有带上横线的形式

class Latin:
    def __int__(self):
        self.exempt = ['', ' ', '/', '\'', '`', '"', ',', '.', '!', '?', '-', '(', ')']
        self.ligature = {'a': 'æ', 'o': 'œ', 'A': 'Æ', 'O': 'Œ'}
        self.macron = {'a': 'ā', 'e': 'ē', 'i': 'ī', 'o': 'ō', 'u': 'ū', 'y': 'ȳ', 'A': 'Ā', 'E': 'Ē', 'I': 'Ī',
                       'O': 'Ō',
                       'U': 'Ū', 'Y': 'Ȳ', 'æ': 'ǣ', 'Æ': 'Ǣ'}
        self.last = ''
        self.parsed = ""
        self.error = -1  # -1表示无错误，若有错误，error值为错误开始处的index
        self.location = []

    def parse(self, text):
        pass

    def locate(self, index):
        pass
