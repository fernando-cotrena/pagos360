from utils.configure_env_variables import AUTH
from clients.payment_client import PaymentRequestClient
from assertpy import assert_that
from fixtures.payment_fixtures import simple_payment_request,unique_item
from datetime import datetime

import json


def test_create_and_get_payment_request(simple_payment_request):
  
      
    payment = PaymentRequestClient(auth=AUTH).create_payment(payment_request=simple_payment_request)    
    
    get_payment = PaymentRequestClient(auth=AUTH).get_payment(id=payment['id'])

    assert_that(get_payment.toJSON()).is_equal_to({'state':'pending'},include=['state'])
    assert_that(get_payment.toJSON()).is_equal_to(simple_payment_request.toJSON(),include=['description','first_total','payer_name'])

    
 
