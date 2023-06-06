import json

class CConfig():
    def __init__(self):
        self.markets = []

        CONFIG_PATH = "C:\\Users\\annna\\OneDrive\\Desktop\\scripts\\wad\\config"

        mrktCFG = open(CONFIG_PATH + '\\markets.cfg')
        mrktDATA = json.load(mrktCFG)

        for i in mrktDATA["markets"]:
            self.markets.append(
                [
                    i['name'],
                    i['config']
                ]
            )

    def getMarket(self, name):
        activeMarket = ""
        activeMarketIndex = None

        # try to find market in markets list
        for idx, names in enumerate(self.markets):
            if names[0] == name:
                activeMarket = names[0]
                activeMarketIndex = idx

        # if doesnt exists raise exception
        if not activeMarket and not activeMarketIndex:
            raise Exception("Market not found")

        # read market config
        CONFIG_PATH = "C:\\Users\\annna\\OneDrive\\Desktop\\scripts\\wad\\config"
        mrktCFG = open(CONFIG_PATH + '\\' + self.markets[activeMarketIndex][1])
        mrktDATA = json.load(mrktCFG)

        mrktINFO = []
        for key, value in mrktDATA.items():
            mrktINFO.append([key, value])

        if not mrktINFO:
            raise Exception("Market Config is empty")
        else:
            return mrktINFO