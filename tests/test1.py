# UnitTest v1.0-alpha
# Flask-Netpad
# version 1.0-alpha
# (C) Abstergo 2018
## test1.py



import unittest
from flask_netpad.netpad import *



class TestMethods(unittest.TestCase):
    '''    def test_upper(self):
            self.assertEqual('foo'.upper(), 'FOO')

        def test_isupper(self):
            self.assertTrue('FOO'.isupper())
            self.assertFalse('Foo'.isupper())
    '''

    print('Running Test..... \n')

    def setUp(self):
        pass

    def test_listNote(self):
        # test list
        self.assertTrue(listNote())
        print("Test List - Ok")

    def test_readNote(self):
        # test read 1
        nid = '5c0202df9d45733b5ce74d35'
        self.assertTrue(readNote(nid))
        print('* read1')

        # test read 2
        a = readNote(nid)
        self.assertEqual(a, readNote(nid))
        print('** read2')

        # test read 3
        b = '5bfe2b4845e2b11150682263'
        self.assertNotEqual(a, readNote(b))
        print('*** read3')
        print('Test Read Note -- OK')


    # newNote()
    def test_newNote(self):
        self.assertTrue(newNote('some slug', 'some title', 'some content'))
        print('new1')
        a = Note.objects(slug='some slug').first()
        self.assertEqual(a.slug, 'some slug')
        print(' Test New Note -- OK')




    # updateNote()
    def test_updateNote(self):
        print('Start Update Test')
        a = '5bfe2b4845e2b11150682263'
        b = Note.objects().get(id=a)
        b.title = "testing2"
        c = Note.objects().get(id=a)
        self.assertEqual(updateNote(a,b), c)
        print('*')
        b.title="Sexy"
        updateNote(a,b)
        self.assertEqual(b.title, "Sexy")
        self.assertNotEqual(b.title, "NotSexy")
        print('**')

        #Fin
        print(' Test updateNote -- OK')


    # delNote()

    # pageNote()

    # db test
        # create database
        # insert test data in db

    # errorCode()
    def test_errorCode(self):
        a = errorCode()

        b = {'code': 404, 'error': 'Object Not Found :( '}
        c = {'code': 404, 'error': 'wrong '}
        self.assertEqual(a, b)
        self.assertNotEqual(a,c)

        d = errorCode(420, "smoke")
        e = {'code': 420, 'error': 'smoke'}
        self.assertEqual(d, e)
        self.assertNotEqual(d, b)
        print('Test errorCode -- OK')

if __name__ == '__main__':
    unittest.main()