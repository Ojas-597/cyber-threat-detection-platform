from pymongo import MongoClient

MONGO_URL = "mongodb://localhost:27017"

client = MongoClient(MONGO_URL)

db = client["cybersecurity_platform"]

# Collections
users_collection = db["users"]
threats_collection = db["threats"]
packets_collection = db["network_packets"]
incidents_collection = db["incident_responses"]
blockchain_collection = db["blockchain_logs"]
