
from simian.text.text_object import TextObject
import unittest
import pygame

class TextObjectTest(unittest.TestCase):

     def setUp(self):
         pygame.init()
         self.text_object = TextObject('TestMessage',50,'comicsansms')

         """test is None"""
         self.font_object_none = self.text_object.font_object

         """Instance for methods display"""

         #self.text_object.font_object.draw_text(True,(255,0,0))


     def tearDown(self):
         self.text_object = None

     def test_message(self):
        message = self.text_object.text_message
        self.assertEqual(message,'TestMessage')

     def test_size(self):
         size = self.text_object.size
         self.assertEqual(size,50)


     def test_font(self):
         size = self.text_object.font_text
         self.assertEqual(size,'comicsansms')

    def test_font_object(self):
         font_object = self.font_object_none
         
    """
        Test methods for custom tezt
    """
     def test_is_bold_text(self):
        test = self.text_object.font_object.set_bold(True)
        is_bold = self.text_object.font_object.get_bold()
        self.assertEqual(is_bold, True)

     def test_is_underline_text(self):
        test = self.text_object.font_object.set_underline(True)
        is_underline = self.text_object.font_object.get_underline()
        self.assertEqual(is_underline, True)

     def test_is_italic_text(self):
        test = self.text_object.font_object.set_italic(True)
        is_italic = self.text_object.font_object.get_italic()
        self.assertEqual(is_italic, True)



if __name__ == '__main__':
    unittest.main()
