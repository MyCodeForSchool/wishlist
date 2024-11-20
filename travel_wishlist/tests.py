#import the necessary objects
from django.test import TestCase
from django.urls import reverse

from .models import Place

# Create your tests here. Django automatically makes a test database & destroys it afterward for each test case
class TestHomePage(TestCase):

    def test_home_page_shows_empty_list_message_for_empty_database(self):
        home_page_url = reverse('place_list') #turn the url path with the name place_list into a url for the request
        response = self.client.get(home_page_url) #saves the response
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html') #makes assertions about the response
        self.assertContains(response, 'You have no places in your wishlist.')

class TestWishList(TestCase):

    fixtures = ['test_places'] #loads the data from the fixture file

    def test_wishlist_contians_not_visited_places(self):
        response = self.client.get(reverse('place_list'))
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
        self.assertContains(response, 'Tokyo')
        self.assertContains(response, 'New York')
        self.assertNotContains(response, 'San Francisco')
        self.assertNotContains(response, 'Moab')

class TestVisitedPlacesPage(TestCase):

    def test_visited_shows_no_places_message(self):
        visited_page_url = reverse('places_visited') #turn the url path with the name place_list into a url for the request
        response = self.client.get(visited_page_url) #saves the response
        self.assertTemplateUsed(response, 'travel_wishlist/visited.html') #makes assertions about the response
        self.assertContains(response, 'You have not visited any places yet.')

class TestVisitedPlaces(TestCase):

    fixtures = ['test_places'] #loads the data from the fixture file

    def test_wishlist_contians_not_visited_places(self):
        response = self.client.get(reverse('places_visited'))
        self.assertTemplateUsed(response, 'travel_wishlist/visited.html')
        self.assertContains(response, 'San Francisco')
        self.assertContains(response, 'Moab')
        self.assertNotContains(response, 'Tokyo')
        self.assertNotContains(response, 'New York')

class TestAddNewPlace(TestCase):
    def test_add_new_unvisited_place(self):
        add_place_url = reverse('place_list')
        new_place_data = {'name': 'Tokyo', 'visited': False}

        response = self.client.post(add_place_url, new_place_data, follow=True)

        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        response_places = response.context['places']
        self.assertEqual(1, len(response_places))#checks only one place
        tokyo_from_response = response_places[0]

        tokyo_from_database = Place.objects.get(name='Tokyo', visited=False)

        self.assertEqual(tokyo_from_database, tokyo_from_response)

class TestVisitPlace(TestCase):

    fixtures = ['test_places']

    def test_visits_place(self):
        visit_place_url = reverse('place_was_visited', args=(2,))
        response = self.client.post(visit_place_url, follow=True)
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        self.assertNotContains(response, 'New York')
        self.assertContains(response, 'Tokyo')

        new_york = Place.objects.get(pk=2)
        self.assertTrue(new_york.visited)

    def test_non_existent_place(self):
        visit_nonexistent_place_url = reverse('place_was_visited', args=(123456,))
        response = self.client.post(visit_nonexistent_place_url, follow=True)
        self.assertEqual(404, response.status_code)


