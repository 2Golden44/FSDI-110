import pymongo
import certifi

con_string = "mongodb+srv://<db_username>:<Mari19>@fsdi-107.090zq.mongodb.net/?retryWrites=true&w=majority&appName=FSDI-107"

client = pymongo.MongoClient(con_string, tlsCAFile=certifi.where())
db = client.get_database("FSDI-107")
