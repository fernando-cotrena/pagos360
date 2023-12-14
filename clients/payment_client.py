from utils.configure_env_variables import URL_BASE,AUTH
from clients.base_client import BaseClient
from entities.payment_entity import PaymentRequestEntity
import json

class PaymentRequestClient(BaseClient):
    def __init__(self, auth):
        super().__init__(auth=auth)
        self.endpoint = f'{URL_BASE}/payment-request'

    def create_payment(self,payment_request):

        json_data = {'payment_request':payment_request.toJSON()}
        response = self.request.post(url=self.endpoint, headers=self.headers,json=json_data)

        return json.loads(response.text)
        
    
    def get_payments(self): 
        response = self.request.get(url=self.endpoint, headers=self.headers)

        payment_request = json.loads(response.text)['data']
        return [ PaymentRequestEntity(**payment)
              for payment in payment_request
        ]
    
    def get_payment(self,id):
        response = self.request.get(url=self.endpoint,params={'id':id}, headers=self.headers)
        
        b= 1
        payment_request =  json.loads(response.text)['data'][0]
        return PaymentRequestEntity(**payment_request)
    
 
        
        

    

