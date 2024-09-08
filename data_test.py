import unittest
from app.data import Database
from pandas import DataFrame


class TestData(unittest.TestCase):
    """
    Unit tests for the Database class methods that 
    interact with a MongoDB collection.
    These tests check the behavior of seed, reset, 
    count, dataframe, and html_table methods.
    """

    def setUp(self):
        """
        Set up a Database instance to be used in the tests. 
        The collection_name is set to 'monsters'.
        """
        self.db = Database(collection_name='monsters')
    
    def test_seed(self):
        """
        Test the seed method by inserting 1000 records 
        into the database and checking if the count matches.
        """
        self.db.seed(amount=1000)
        self.assertEqual(self.db.count(), 1000)
    
    def test_reset(self):
        """
        Test the reset method by clearing the database and 
        verifying the count is 0.
        """
        # self.db.seed(amount=1000)
        self.db.reset()
        self.assertEqual(self.db.count(), 0)

    def test_count(self):
        """
        Test the count method by asserting that the number 
        of records in the database is 1000.
        Assumes the database is already populated.
        """
        # self.db.seed(amount=1000)
        self.assertEqual(self.db.count(),1000)

    def test_dataframe(self):
        """
        Test the dataframe method by seeding 100 records and 
        ensuring the returned object is a DataFrame.
        """
        self.db.seed(amount=100)
        df = self.db.dataframe()
        self.assertIsInstance(df, DataFrame)
    
    def test_html_table(self):
        """
        Test the html_table method by seeding 10 records and 
        checking if the returned object is a string
        representing an HTML table.
        """
        self.db.seed(amount=10)
        table = self.db.html_table()
        self.assertIsInstance(table, str)

if __name__ == '__main__':
    unittest.main()
