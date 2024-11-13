import json
from datetime import date, datetime
from decimal import Decimal

class Stock:
    def __init__(self, symbol, date, open_, high, low, close, volume):
        self.symbol = symbol
        self.date = date
        self.open = open_
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def to_dict(self):
        return{
            'type':'Stock',
            'symbol':self.symbol,
            'date':self.date.isoformat(),
            'open':str(self.open),
            'high':str(self.high),
            'low':str(self.low),
            'close':str(self.close),
            'volume':self.volume
        }
        
class Trade:
    def __init__(self, symbol, timestamp, order, price, volume, commission):
        self.symbol = symbol
        self.timestamp = timestamp
        self.order = order
        self.price = price
        self.commission = commission
        self.volume = volume

    def to_dict(self):
        return{
            'type':'Trade',
            'symbol':self.symbol,
            'timestamp':self.timestamp.isoformat(),
            'order':self.order,
            'price':str(self.price),
            'commission':str(self.commission),
            'volume':self.volume
        }


class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, (Stock, Trade)):
            return o.to_dict()
        return super().default(o)
