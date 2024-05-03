from dotenv import load_dotenv
import os
load_dotenv()

VERSION =  os.getenv('VERSION','0.0.0')
CONNECTION_STRING = os.getenv('MONGODB_URI','mongodb://localhost:27017')
