from datetime import date
from pytest import raises
from pydantic import ValidationError

from src.contracts import Sale

def test_sales_with_valid_data():
    valid_data = {
        "email": "sale@example.com",
        "date": date.today(),
        "price": 100.50,
        "product": "Product A",
        "quantity": 4,
        "category": "retail"
    }

    sale = Sale(**valid_data)

    assert sale.email == valid_data['email']
    assert sale.date == valid_data['date']
    assert sale.price == valid_data['price']
    assert sale.product == valid_data['product']
    assert sale.quantity == valid_data['quantity']
    assert sale.category == valid_data['category']

def test_sales_with_invalid_data():
    invalid_data = {
        "email": "not_email_example",
        "date": "today",
        "price": -99.99,
        "product": "",
        "quantity": -5,
        "category": "retail"
    }
    
    with raises(ValidationError) as validation_error:
        Sale(**invalid_data)
    
    errors_field = [error['loc'][0] for error in validation_error.value.errors()]
    expected_invalid_fields = list(invalid_data.keys())[:-1]

    assert errors_field == expected_invalid_fields

def test_sales_with_invalid_category():
    invalid_category_data = {
        "email": "sale@exemple.com",
        "date": date.today(),
        "price": 100.50,
        "product": "Product A",
        "quantity": 4,
        "category": "INVALID"
    }
    with raises(ValidationError) as validation_error:
        Sale(**invalid_category_data)

    error_possible_categories = validation_error.value.errors()[0]["ctx"]['expected']

    expected_categories = "'retail', 'online' or 'b2b'"

    assert expected_categories == error_possible_categories
