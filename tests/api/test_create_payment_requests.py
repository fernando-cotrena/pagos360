from utils.configure_env_variables import AUTH
from clients.payment_client import PaymentRequestClient
from assertpy import assert_that
from fixtures.payment_fixtures import simple_payment_request,unique_item
from utils.format_date import simple_format_date
from datetime import datetime

def test_simple_payment_request(simple_payment_request):
  
    payment = PaymentRequestClient(auth=AUTH).create_payment(payment_request=simple_payment_request)

    assert_that(payment).is_equal_to({'type':'payment_request','state':'pending'},include=['type','state'])
    assert_that(payment).is_equal_to(simple_payment_request.toJSON(),include=['description','first_total','payer_name'])
   
 
def test_payment_request_with_item(simple_payment_request,unique_item):
    
    payment_request = simple_payment_request
    payment_request.add({'items':unique_item})

    payment = PaymentRequestClient(auth=AUTH).create_payment(payment_request=payment_request)

    assert_that(payment).is_equal_to({'type':'payment_request','state':'pending'},include=['type','state'])
    assert_that(payment).is_equal_to(payment_request.toJSON(),include=['description','first_total','payer_name','items'])
    assert_that(simple_format_date(payment['created_at'][:10])).is_equal_to_ignoring_time(datetime.today())
    