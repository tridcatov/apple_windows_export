import re

class DateResolver:
    def __init__(self):
        self.month_map = {
            "января" : 1,
            "февраля" : 2,
            "марта" : 3,
            "апреля" : 4,
            "мая" : 5,
            "июня" : 6,
            "июля" : 7,
            "августа" : 8,
            "сентября" : 9,
            "октября" : 10,
            "ноября" : 11,
            "декабря" : 12
        }
        months_regex = "|".join(self.month_map.keys())
        pattern = "(\d\d?)\s({})\s(\d\d\d\d)".format(months_regex)
        self.p = re.compile(pattern, re.X)

    def resolve(self, str):
        match = self.p.search(str)
        if match is None:
            return None
        
        day = int(match.group(1))
        month_name = match.group(2)
        month = int(self.month_map[month_name])
        year = int(match.group(3))
        return day, month, year
