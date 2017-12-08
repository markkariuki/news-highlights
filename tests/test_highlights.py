import unittest
from app.models import High

class HighTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the highlights class
    '''

def setUp(self):
    '''
    Set up method that will run before every Test
    '''
    self.new_highlight = High(1234,'Python Must Be Crazy','A thrilling new Python Series','/khsjha27hbs',8.5,129993)

def test_instance(self):
    self.assertTrue(isinstance(self.new_highlight,High))
