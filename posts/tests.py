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


class PostDetailViewTests(APITestCase):
    """ Set up used to create 2 users and posts to use within the class tests"""
    def setUp(self):
        antony = User.objects.create_user(username='antony', password='pass')
        freddie = User.objects.create_user(username='freddie', password='pass')
        Post.objects.create(
            owner=antony, title='a title', description='antonys description'
        )
        Post.objects.create(
            owner=freddie, title='another title', description='freddies description'
        )

    def test_can_retrieve_post_using_valid_id(self):
        """For retrieving a post with a valid id"""
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_post_using_invalid_id(self):
        """Can't retrieve a post with a invalid id"""
        response = self.client.get('/posts/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_post(self):
        """ 
        Login as one of the set up users and retreive a post, update the title 
        filters through the primary keys and gets the first one, adds the new title
        """
        self.client.login(username='antony', password='pass')
        response = self.client.put('/posts/1/', {'title': 'a new title'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_other_users_post(self):
        """ 
        Login with one of the set up users,
        attempt to update the title with the other users post id
        """
        self.client.login(username='antony', password='pass')
        response = self.client.put('/posts/2/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

