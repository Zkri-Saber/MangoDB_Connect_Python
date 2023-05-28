
from pymongo import MongoClient


MANGODB_URL = "mongodb+srv://user:password@myatlasclusteredu.6easdgk.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MANGODB_URL)

# Access the "library" database
db = client["library"]

# Access the "books" collection
collection = db["books"]

# Print success message
print("Document inserted successfully.")

