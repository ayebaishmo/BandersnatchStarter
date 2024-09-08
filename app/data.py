from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database:

    def __init__(self, collection_name):
        load_dotenv()
        self.client = MongoClient(getenv("DB_URL"), tlsCAFile=where())
        self.db = self.client['monster_database']
        self.collection = self.db[collection_name]

    def seed(self, amount):
        """
        Seeds the collection with amount of random monsters
        using the monsterlab librarry
        """
        monsters = [Monster().to_dict() for _ in range(amount)]
        self.collection.insert_many(monsters)

    def reset(self):
        """
        Resests the collection by deleting all documents
        """
        self.collection.delete_many({})

    def count(self) -> int:
        """
        Returns the number of documents in the collection
        """
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        """
        Returns a DataFrame containing all documents in the
        collection
        """
        cursor = self.collection.find({})
        df = DataFrame(list(cursor))
        return df

    def html_table(self) -> str:
        """
        Returns the html table representation of the DataFrame
        or none of the collection is empty
        """
        df = self.dataframe()
        if df.empty:
            return None
        return df.to_html(index=False)
