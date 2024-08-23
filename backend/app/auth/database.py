from .models import Login
from pymongo import MongoClient,errors


default_user = Login(email="student1@wethinkcode.co.za",password="12345")

# class mongo():
    
#     @classmethod
#     async def open_connection(cls) -> MongoClient:
#         try:
#             client =  MongoClient("mongodb://localhost:27017")
#             return client
#         except:
#             raise errors.ConnectionFailure
        
#     @classmethod
#     async def close_connection(cls,client: MongoClient):
#         client.close()


