import json


class PaymentRequestEntity:
    
    def __init__ (self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
            
    def toJSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))
    
    def add(self,value):
        self.__dict__.update(value)
    
   
class ItemsEntity:

    def __init__ (self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def toJSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))

    