from django.test import TestCase
from .models import BlogPost


class BlogModelTest(TestCase):

    def test_saving_and_retrieving_posts(self):
        firstPost = BlogPost()
        firstPost.title = "First Post"
        firstPost.description = "First Description"
        firstPost.user_id = 0
        firstPost.save()

        secondPost = BlogPost()
        secondPost.title = "Second Post"
        secondPost.description = "Second Description"
        secondPost.user_id = 0
        secondPost.save()

        saved_items = BlogPost.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        self.assertEqual(first_saved_item.title, 'First Post')
        self.assertEqual(first_saved_item.description, 'First Description')
        self.assertEqual(second_saved_item.title, 'Second Post')
        self.assertEqual(second_saved_item.description, 'Second Description')