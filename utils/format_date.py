
from datetime import datetime


def simple_format_date(value_date):
    return datetime.strptime(value_date, '%Y-%m-%d')