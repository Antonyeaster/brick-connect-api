from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    """
    Set up runs before every test method within the class.
    The username and password within the set up method can be reused with the class
    """
    def setUp(self):
        User.objects.create_user(username='antony', password='pass')

    def test_can_list_posts(self):
        """
        Gets the username and creates a post,
        then prints the data from the post to the terminal
        """
        antony = User.objects.get(username='antony')
        Post.objects.create(owner=antony, title='a title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        """
        First login with the username and password,
        then send a post resquest to /posts/ and create a posts using title.
        Then check the count is equal to 1
        """
        self.client.login(username='antony', password='pass')
        response = self.client.post('/posts/', {'title': 'a title'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_post(self):
        """
        This test is sending a post resquest to /posts/ and create a posts using title,
        without being already signed in
        """
        response = self.client.post('/posts/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
