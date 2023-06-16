import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api.mindee.net/v1/products/mindee/expense_receipts/v5/predict"
API_KEY = os.getenv('API_KEY')

# FILE_PATH = "/Users/calvinjmin/Desktop/test_receipt.jpg"

def post_mindee_api( FILE_PATH ):
    response = None

    with open(FILE_PATH, "rb") as myfile:
        files = {"document": myfile}
        headers = {"Authorization": API_KEY}
        response = requests.post(API_URL, files=files, headers=headers)

    return response


