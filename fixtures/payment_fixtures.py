import pytest
from entities.payment_entity import PaymentRequestEntity,ItemsEntity
from datetime import datetime
from faker import Faker
import random


faker = Faker(['es_ES'])

@pytest.fixture
def simple_payment_request():
    return  PaymentRequestEntity(**{
        'description':f'payment {datetime.now().strftime("%y%m%d_%H%M%S%f")}',
        'first_due_date':faker.future_datetime().strftime('%d-%m-%Y'),
        'first_total':   round(random.uniform(100.5, 750.5),2),
        'payer_name': faker.first_name(),
    })

@pytest.fixture
def unique_item():
       return [ItemsEntity(**{
        'description': f'item {datetime.now().strftime("%y%m%d_%H%M%S%f")}',
        'amount': round(random.uniform(100.5, 750.5),2)
    })]
