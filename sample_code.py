# pip install tableland
from tableland import Database

# Initialize the database connection
private_key = "....03"
db = Database(
    private_key=private_key,
    provider_uri="https://eth-sepolia.g.alchemy.com/v2/demo",  # Replace with your chain RPC provider URL
)
print("db read")
# Define the table and SQL statement
table_name = "propertydata1_..."
statement = f"SELECT * FROM {table_name}"

# Execute the read query
data = db.read(statement)

# Print the result
print(data)

#Define SQL statement
statement = f"""
    INSERT INTO {table_name} (Title, Price, Area, BHK, Bathrooms, Furnished, Facing, PropertyType, Description, IsLuxury, YearOfConstruction)
    VALUES 
    ('Luxury Apartment', 25000000, '3500 sqft', 4, 3, 'Yes', 'South', 'Apartment', 'High-end apartment with a sea view.', 'Yes', 2021),
    ('Cozy Studio', 15000000, '1500 sqft', 1, 1, 'No', 'West', 'Studio', 'Compact studio in a prime location.', 'No', 2019)
"""
#write data to table
write_event = db.write(statement)

if write_event["error"] is not None:
    print(f"Error: {write_event['error']}")
else:
    print(f"Successfully inserted into table {table_name}. Transaction hash: {write_event['transaction_hash']}")

