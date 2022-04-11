from django.test import TestCase
from .models import Post, Review

# Create your tests here.
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Post(title = 'blog', content ='hello', link ='https//:www.google.com')

# Testing instance
def test_instance(self):
    self.assertTrue(isinstance(self.blog,Post))

   # Testing Save Method
def test_save_method(self):
    self.james.save_editor()
    editors = Post.objects.all()
    self.assertTrue(len(editors) > 0)

