import pandas as pd
from faker import Faker
from datetime import date, timedelta
import random

from src.contracts import Sale, SaleCategory

fake = Faker()


def generate_sale():
    return {
        "email": fake.email(),
        "date": date.today() - timedelta(days=random.randint(0, 365)),
        "price": round(random.uniform(10.0, 1000.0), 2),
        "product": fake.word().capitalize(),
        "quantity": random.randint(1, 100),
        "category": random.choice(list(SaleCategory)),
    }

def generate_invalid_key_value():
    invalid_sale = {
        "email": "not-an-email",
        "date": "00-00-0000",
        "price": round(random.uniform(-1000.0, -10.0), 2),
        "product": "",
        "quantity": random.randint(-100, -1),
        "category": "invalid-category"
    }

    sale_keys = invalid_sale.keys()
    selected_key = list(sale_keys)[random.randint(0, len(sale_keys)-1)]
    selected_value = invalid_sale[selected_key]

    return selected_key, selected_value




def corrupt_sale(sale: Sale):
    selected_key, selected_value = generate_invalid_key_value()
    
    return {
        **sale.model_dump(),
        "category": sale.category.value,
        selected_key: selected_value
    }



def generate_sales_list(n: int, valid: bool = True):
    sales_data: list[dict[str, any]] = []
    for _ in range(n):
        sale_data = generate_sale()
        sale = Sale(**sale_data)
        
        if not valid and random.randint(0, 9) % 2 == 0:
            sales_data.append(corrupt_sale(sale))
        else:
            sales_data.append({ 
                **sale.model_dump(),
                "category": sale.category.value
            })
    return sales_data
    
def create_file(file_name: str, valid: bool = True):
    df = pd.DataFrame(generate_sales_list(20, valid))
    df.to_excel(f"data/{file_name}.xlsx", index=False)
    print(f"Excel file '{file_name}.xlsx' created successfully.")


if __name__ == "__main__":
    create_file("sales_data")
    create_file("invalid_sales_data", valid=False)
