import json
from datetime import date, datetime
from decimal import Decimal
from marshmallow import Schema, fields, post_load

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


def custom_decoder(obj):
    """Object hook for JSON deserialization"""
    if 'type' not in obj:
        return obj
        
    obj_type = obj.get('type')
    
    if obj_type == 'Stock':
        return Stock(
            symbol=obj['symbol'],
            date=date.fromisoformat(obj['date']),
            open_=Decimal(obj['open']),
            high=Decimal(obj['high']),
            low=Decimal(obj['low']),
            close=Decimal(obj['close']),
            volume=obj['volume']
        )
        
    elif obj_type == 'Trade':
        return Trade(
            symbol=obj['symbol'],
            timestamp=datetime.fromisoformat(obj['timestamp']),
            order=obj['order'],
            price=Decimal(obj['price']),
            volume=obj['volume'],
            commission=Decimal(obj['commission'])
        )
        
    return obj

class StockSchema(Schema):
    symbol = fields.Str()
    date = fields.Date()
    open = fields.Decimal(as_string=True, data_key="open_")  # using data_key for open_
    high = fields.Decimal(as_string=True)
    low = fields.Decimal(as_string=True)
    close = fields.Decimal(as_string=True)
    volume = fields.Integer()

    @post_load
    def make_stock(self, data, **kwargs):
        return Stock(**data)
    
class TradeSchema(Schema):
    symbol = fields.Str()
    timestamp = fields.DateTime()
    order = fields.Str()
    price = fields.Decimal(as_string=True)
    volume = fields.Integer()
    commission = fields.Decimal(as_string=True)

    @post_load
    def make_trade(self, data, **kwargs):
        return Trade(**data)
    

def serialize_with_marshmallow(*args):
    pass

def deserialize_with_marshmallow(*args):
    pass