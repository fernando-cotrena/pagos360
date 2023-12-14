from utils.configure_env_variables import AUTH
from clients.payment_client import PaymentRequestClient
from assertpy import assert_that
from fixtures.payment_fixtures import simple_payment_request,unique_item
from utils.format_date import simple_format_date
from datetime import datetime

def test_get_payments():
  
    payment = PaymentRequestClient(auth=AUTH).get_payments()
    assert_that(payment).is_not_empty()
    assert_that(payment[0].toJSON()).contains_key('id','barcode','state','created_at','description','first_total','payer_name')
 
def test_get_payments_by_id():
  
    payment = PaymentRequestClient(auth=AUTH).get_payment(id=1849320)
    assert_that(payment.toJSON()).is_equal_to({'id':1849320},include=['id'])

