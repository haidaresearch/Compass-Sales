!pip install pandas openpyxl faker

import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker('id_ID') # Use Indonesian locale for more realistic names and addresses


product_data = [
    {'product_id': 'VL01', 'product_name': 'Velocity Black', 'collection': 'Velocity', 'price': '798000'},
    {'product_id': 'VL02', 'product_name': 'Velocity Grey', 'collection': 'Velocity', 'price': '798000'},
    {'product_id': 'VL03', 'product_name': 'Velocity Black Gum', 'collection': 'Velocity', 'price': '798000'},
    {'product_id': 'VL04', 'product_name': 'Velocity White Gum', 'collection': 'Velocity', 'price': '798000'},
    {'product_id': 'VL05', 'product_name': 'Velocity Blue Yellow', 'collection': 'Velocity', 'price': '798000'},
    {'product_id': 'VL06', 'product_name': 'Velocity Lilac', 'collection': 'Velocity', 'price': '1258000'},
    {'product_id': 'VL07', 'product_name': 'Velocity Mint', 'collection': 'Velocity', 'price': '1258000'},
    {'product_id': 'VL08', 'product_name': 'Velocity Fuchsia', 'collection': 'Velocity', 'price': '1258000'},
    {'product_id': 'PR01', 'product_name': 'Proto 2 Low', 'collection': 'Proto', 'price': '1338000'},
    {'product_id': 'PR02', 'product_name': 'Proto 2 Hi', 'collection': 'Proto', 'price': '1398000'},
    {'product_id': 'RG01', 'product_name': 'Retrograde Low Black White', 'collection': 'Retrograde', 'price': '538000'},
    {'product_id': 'RG02', 'product_name': 'Retrograde Low Cream', 'collection': 'Retrograde', 'price': '538000'},
    {'product_id': 'RG03', 'product_name': 'Retrograde Low Triple Black', 'collection': 'Retrograde', 'price': '538000'},
    {'product_id': 'RG04', 'product_name': 'Retrograde Low White Blue', 'collection': 'Retrograde', 'price': '538000'},
    {'product_id': 'RG05', 'product_name': 'Retrograde Camp Low Camel', 'collection': 'Retrograde', 'price': '568000'},
    {'product_id': 'RG06', 'product_name': 'Retrograde Hi Decon Black White', 'collection': 'Retrograde', 'price': '568000'},
    {'product_id': 'RG07', 'product_name': 'Retrograde Hi Decon Cream', 'collection': 'Retrograde', 'price': '568000'},
    {'product_id': 'RG08', 'product_name': 'Retrograde Hi Decon Triple Black', 'collection': 'Retrograde', 'price': '568000'},
    {'product_id': 'RG09', 'product_name': 'Retrograde Camp Hi Olive', 'collection': 'Retrograde', 'price': '598000'},
    {'product_id': 'RG10', 'product_name': 'Retrograde Slip On Black', 'collection': 'Retrograde', 'price': '458000'},
    {'product_id': 'RG11', 'product_name': 'Retrograde Slip On Herringbone Black', 'collection': 'Retrograde', 'price': '498000'},
    {'product_id': 'RG12', 'product_name': 'Retrograde Slip On Herringbone White', 'collection': 'Retrograde', 'price': '498000'},
    {'product_id': 'RG13', 'product_name': 'Retrograde Slip On Waffle Indigo', 'collection': 'Retrograde', 'price': '538000'},
    {'product_id': 'RG14', 'product_name': 'Retrograde Slip On Patch Indigo', 'collection': 'Retrograde', 'price': '538000'},
    {'product_id': 'RG15', 'product_name': 'Retrograde Slip On Stripe Indigo', 'collection': 'Retrograde', 'price': '538000'},
    {'product_id': 'RG16', 'product_name': 'Retrograde Slip On Kawung Cream', 'collection': 'Retrograde', 'price': '598000'},
    {'product_id': 'RG17', 'product_name': 'Retrograde Slip On Kawung Camel', 'collection': 'Retrograde', 'price': '598000'},
    {'product_id': 'GZ01', 'product_name': 'Gazelle Low Black White', 'collection': 'Gazelle', 'price': '408000'},
    {'product_id': 'GZ02', 'product_name': 'Gazelle Low Cream', 'collection': 'Gazelle', 'price': '408000'},
    {'product_id': 'GZ03', 'product_name': 'Gazelle Low Black Gum', 'collection': 'Gazelle', 'price': '408000'},
    {'product_id': 'GZ04', 'product_name': 'Gazelle Low White Blue', 'collection': 'Gazelle', 'price': '408000'},
    {'product_id': 'GZ05', 'product_name': 'Gazelle Low White Red', 'collection': 'Gazelle', 'price': '408000'},
    {'product_id': 'GZ06', 'product_name': 'Gazelle Low Weaves Sand', 'collection': 'Gazelle', 'price': '468000'},
    {'product_id': 'GZ07', 'product_name': 'Gazelle Low Weaves Graphite', 'collection': 'Gazelle', 'price': '468000'},
    {'product_id': 'GZ08', 'product_name': 'Gazelle Low Ice Cream', 'collection': 'Gazelle', 'price': '408000'},
    {'product_id': 'GZ09', 'product_name': 'Gazelle Hi Black White', 'collection': 'Gazelle', 'price': '438000'},
    {'product_id': 'GZ10', 'product_name': 'Gazelle Hi Cream', 'collection': 'Gazelle', 'price': '438000'},
    {'product_id': 'GZ11', 'product_name': 'Gazelle Hi Black Gum', 'collection': 'Gazelle', 'price': '438000'},
    {'product_id': 'GZ12', 'product_name': 'Gazelle Hi White Blue', 'collection': 'Gazelle', 'price': '438000'},
    {'product_id': 'GZ13', 'product_name': 'Gazelle Hi White Red', 'collection': 'Gazelle', 'price': '438000'},
    {'product_id': 'GZ14', 'product_name': 'Gazelle Hi Ice Cream', 'collection': 'Gazelle', 'price': '438000'},
    {'product_id': 'GZ15', 'product_name': 'Gazelle Popsicle Red', 'collection': 'Gazelle', 'price': '498000'},
    {'product_id': 'GZ16', 'product_name': 'Gazelle Popsicle Blue', 'collection': 'Gazelle', 'price': '498000'},
    {'product_id': 'GZ17', 'product_name': 'Gazelle Popsicle Green', 'collection': 'Gazelle', 'price': '498000'},
    {'product_id': 'GZ18', 'product_name': 'Gazelle Popsicle Yellow', 'collection': 'Gazelle', 'price': '498000'},
    {'product_id': 'TR01', 'product_name': 'Tribune Darbotz Black White', 'collection': 'Tribune', 'price': '698000'},
    {'product_id': 'TR02', 'product_name': 'Tribune 4884 Black', 'collection': 'Tribune', 'price': '638000'},
    {'product_id': 'TR03', 'product_name': 'Tribune 4884 Brown', 'collection': 'Tribune', 'price': '638000'},
    {'product_id': 'TR04', 'product_name': 'Tribune 4884 Tan', 'collection': 'Tribune', 'price': '638000'},
    {'product_id': 'TR05', 'product_name': 'Tribune Black Gum', 'collection': 'Tribune', 'price': '568000'},
    {'product_id': 'TR06', 'product_name': 'Tribune Navy Gum', 'collection': 'Tribune', 'price': '568000'},
    {'product_id': 'TR07', 'product_name': 'Tribune Red Gum', 'collection': 'Tribune', 'price': '568000'},
    {'product_id': 'TR08', 'product_name': 'Tribune White Blue', 'collection': 'Tribune', 'price': '568000'},
    {'product_id': 'TR09', 'product_name': 'Tribune White Green', 'collection': 'Tribune', 'price': '568000'},
]

# Create Product Dimension Table
dim_product = pd.DataFrame(product_data)

dim_product['initial_stock'] = dim_product['collection'].apply(lambda x: random.randint(100, 500) if x != 'Proto' else random.randint(50, 150)) # Proto has less stock

# Add a size range to the product dimension
dim_product['available_sizes'] = [list(range(35, 46))] * len(dim_product)


# --- Generate Fake Data for other Dimensions ---

# Date Dimension Table
end_date = datetime.now()
start_date = end_date - timedelta(days=5*365) # Approximately 5 years

date_list = pd.date_range(start=start_date, end=end_date, freq='D')
dim_date = pd.DataFrame({'date_id': date_list})
dim_date['year'] = dim_date['date_id'].dt.year
dim_date['month'] = dim_date['date_id'].dt.month
dim_date['day'] = dim_date['date_id'].dt.day
dim_date['day_of_week'] = dim_date['date_id'].dt.dayofweek # Monday=0, Sunday=6
dim_date['day_name'] = dim_date['date_id'].dt.day_name()
dim_date['quarter'] = dim_date['date_id'].dt.quarter
dim_date['week_of_year'] = dim_date['date_id'].dt.isocalendar().week.astype(int)


# Customer Dimension Table (Generate 500 fake customers)
num_customers = 500
customers = []
for i in range(num_customers):
    customer_id = f'{i+1:05d}'
    first_name = fake.first_name()
    last_name = fake.last_name()
    address = fake.street_address()
    city = fake.city()
    province = fake.state()
    postal_code = fake.postcode()
    email = fake.email()
    phone_number = fake.phone_number()
    join_date = fake.date_between(start_date=start_date, end_date=end_date)
    customers.append({
        'customer_id': customer_id,
        'first_name': first_name,
        'last_name': last_name,
        'address': address,
        'city': city,
        'province': province,
        'postal_code': postal_code,
        'email': email,
        'phone_number': phone_number,
        'join_date': join_date
    })
dim_customer = pd.DataFrame(customers)

# Store Dimension Table
stores = [
    {'store_id': '01', 'store_name': 'Shopee', 'city': None, 'province': None, 'channel': 'Online'},
    {'store_id': '02', 'store_name': 'Tokopedia', 'city': None, 'province': None, 'channel': 'Online'},
    {'store_id': '03', 'store_name': 'TikTok', 'city': None, 'province': None, 'channel': 'Online'},
    {'store_id': '04', 'store_name': 'Website', 'city': None, 'province': None, 'channel': 'Online'},
    {'store_id': '05', 'store_name': 'Modular', 'city': 'Kota Administrasi Jakarta Selatan', 'province': 'DKI Jakarta', 'channel': 'Offline'},
]
dim_store = pd.DataFrame(stores)

# Payment Method Dimension Table
payment_methods = [
    {'payment_method_id': '1', 'payment_method_name': 'Credit Card'},
    {'payment_method_id': '2', 'payment_method_name': 'Debit Card'},
    {'payment_method_id': '3', 'payment_method_name': 'Bank Transfer'},
    {'payment_method_id': '4', 'payment_method_name': 'E-Wallet'},
    {'payment_method_id': '5', 'payment_method_name': 'Cash'},
]
dim_payment = pd.DataFrame(payment_methods)


# --- Generate Fake Fact Data (Sales Transactions) ---

num_transactions = 15000 # Aiming for at least 10,000 transactions
transactions = []

for i in range(num_transactions):
    transaction_id = f'{i+1:08d}'
    date_info = random.choice(date_list)
    customer_info = random.choice(customers)
    store_info = random.choice(stores)
    product_info = random.choice(product_data)
    payment_method_info = random.choice(payment_methods)

    # Business Logic Adjustments:
    # - Cash is only available in physical stores
    if store_info['channel'] == 'Online' and payment_method_info['payment_method_name'] == 'Cash':
        payment_method_info = random.choice([p for p in payment_methods if p['payment_method_name'] != 'Cash'])

    # - Quantity is usually 1 or 2 per transaction item
    quantity = random.choice([1, 1, 1, 2]) # More likely to buy 1

    # Calculate item total
    product_price = int(dim_product[dim_product['product_id'] == product_info['product_id']]['price'].iloc[0])
    item_total = quantity * product_price

    transactions.append({
        'transaction_id': transaction_id,
        'date_id': date_info.date(), # Store date part only
        'customer_id': customer_info['customer_id'],
        'store_id': store_info['store_id'],
        'product_id': product_info['product_id'],
        'product_price': product_price, # Include price in fact table
        'quantity': quantity,
        'item_total': item_total,
        'payment_method_id': payment_method_info['payment_method_id'],
        'transaction_time': fake.time_object()
    })

fact_sales = pd.DataFrame(transactions)

# Ensure date_id in fact table is datetime object to merge
fact_sales['date_id'] = pd.to_datetime(fact_sales['date_id'])

# --- Prepare for Download ---

# Create an Excel writer object
output_filename = 'compass_sales_data.xlsx'
with pd.ExcelWriter(output_filename, engine='openpyxl') as writer:
    # Write each DataFrame to a separate sheet
    fact_sales.to_excel(writer, sheet_name='Fact_Sales', index=False)
    dim_date.to_excel(writer, sheet_name='Dim_Date', index=False)
    dim_customer.to_excel(writer, sheet_name='Dim_Customer', index=False)
    dim_product.to_excel(writer, sheet_name='Dim_Product', index=False)
    dim_store.to_excel(writer, sheet_name='Dim_Store', index=False)
    dim_payment.to_excel(writer, sheet_name='Dim_PaymentMethod', index=False)

print(f"Fake sales data and saved to {output_filename}")

# --- Download the file ---
from google.colab import files
files.download(output_filename)