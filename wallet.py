import pandas as pd
import json

class Wallet:

    def __init__(self):
        pass

    def load_wallet(self):
        f = open("ledger.json")
        transactions = json.load(f)