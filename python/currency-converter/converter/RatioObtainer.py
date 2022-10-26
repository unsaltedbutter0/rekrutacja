import json, datetime as dt, requests


class RatioObtainer:
    base = None
    target = None

    file = json.load(open('ratios.json', 'r'))
    write_file = open('ratios.json', 'w')

    def __init__(self, base, target):
        self.base = base
        self.target = target

    def was_ratio_saved_today(self):
        # TODO DONE
        # This function checks if given ratio was saved today and if the file with ratios is created at all
        # should return false when file doesn't exist or if there's no today's exchange rate for given values at all
        # should return true otherwise
        for data in self.file:
            if self.base == data['base_currency'] and self.target == data['target_currency']:
                if dt.datetime.today() - dt.datetime.strptime(data["date_fetched"], "%Y-%m-%d") < dt.timedelta(days=1):
                    return True
        return False
        pass

    def fetch_ratio(self):
        # TODO
        # This function calls API for today's exchange ratio
        # Should ask API for today's exchange ratio with given base and target currency
        # and call save_ratio method to save it
        url = 'https://api.exchangerate.host/latest?base=' + self.base
        data = requests.get(url).json()
        ratio = data['rates'][self.target]
        self.save_ratio(ratio)
        pass

    def save_ratio(self, ratio):
        # TODO
        # Should save or update exchange rate for given pair in json file
        # takes ratio as argument
        # example file structure is shipped in project's directory, yours can differ (as long as it works)
        x = 0
        for data in self.file:
            if self.base == data['base_currency'] and self.target == data['target_currency']:
                data['ratio'] = ratio
                data["date_fetched"] = str(dt.date.today())
                x = 1
                break
        if x == 0:
            self.file.append({
                                "base_currency": self.base,
                                "target_currency": self.target,
                                "date_fetched": str(dt.date.today()),
                                "ratio": ratio})
        json.dump(self.file, self.write_file, indent=4)

        pass

    def get_matched_ratio_value(self):
        # TODO
        # Should read file and receive exchange rate for given base and target currency from that file
        for data in self.file:
            if self.base == data['base_currency'] and self.target == data['target_currency']:
                return data['ratio']
        pass
