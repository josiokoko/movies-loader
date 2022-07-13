# import unittest
try:
    import unittest2 as unittest
except ImportError:
    import unittest
   
import json
import xmlrunner

class TestJSONLoaderMethods(unittest.TestCase):
    movies = []

    @classmethod
    def setUpClass(cls):
        with open('movies.json') as json_file:
            cls.movies = json.load(json_file)

    def test_rank(self):
        self.assertEqual(self.movies[0]['rank'], '1')
    
    def test_title(self):
        self.assertEqual(self.movies[0]['title'], 'The Shawshank Redemption')
    
    def test_id(self):
        self.assertEqual(self.movies[0]['id'], 'tt0111161')

if __name__ == '__main__':
    # runner = xmlrunner.XMLTestRunner(output='reports')
    # unittest.main(testRunner=runner)
    
    with open('reports/results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)
