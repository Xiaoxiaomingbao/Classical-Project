from src.Lang import Lang


class Greek(Lang):
    def __init__(self):
        super().__init__()
        self.configured = False  # representing the result of configuration
        self.active = False  # representing the typing process of specific language
        self.last = ''  # the last character that has been parsed
        self.error = -1  # the index where an error begins, -1 if there is no error

    def parse(self, text):
        pass
