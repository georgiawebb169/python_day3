from dotenv import load_dotenv
import os 

load_dotenv()

secret =os.getenv('secret')

print(secret)


