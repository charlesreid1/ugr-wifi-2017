from pymongo import MongoClient
import time

print("!"*30)
print("!"*30)
print("WARNING: ABOUT TO DROP ALL WIFI DATA FROM MONGODB")
print("!"*30)
print("!"*30)
print("\n")
print("Waiting 10 seconds...")
time.sleep(10)

# Port 27017 connects to the MongoDB Docker container
client = MongoClient('localhost', 27017)

# Get database 
db = client.wifi

# Get collections
ap = db.ap_data
client = db.client_data

# Drop collections
ap.drop()
client.drop()
