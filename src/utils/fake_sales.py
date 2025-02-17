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

def generate_sales_list(n: int):
    sales_data: list[dict[str, any]] = []
    for _ in range(n):
        sale_data = generate_sale()
        sale = Sale(**sale_data)
        
        sales_data.append({ 
            **sale.model_dump(),
            "category": sale_data["category"].value
        })
    return sales_data
    
if __name__ == "__main__":
    df = pd.DataFrame(generate_sales_list(10))
    df.to_excel("invalid_sales_data.xlsx", index=False)
    print("Excel file 'invalid_sales_data.xlsx' created successfully.")
