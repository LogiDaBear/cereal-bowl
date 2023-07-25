from django.test import TestCase

from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Cereal

class CerealTest(TestCase):

      
      @classmethod
      def setUpTestData(cls):
          testuser1 = get_user_model().objects.create_user(
              username='testuser1', password='1234'
          )
  
          testuser1.save()

          testuser2 = get_user_model().objects.create_user(
              username='testuser2', password='1234'
          )
  
          testuser2.save()
  
          test_cereal = Cereal.objects.create(
              reviewer = testuser1,
              brand = 'Wheaties',
              rating = '5', 
          )
          test_cereal.save()

          test_cereal_2 = Cereal.objects.create(
              reviewer = testuser2,
              brand = 'Cocoa Pebbles',
              rating = '10'
          )
          test_cereal_2.save()

      def test_cereal(self):
           cereal = Cereal.objects.get(id=1)
           reviewer = str(cereal.reviewer)
           rating = str(cereal.rating)
           brand = str(cereal.brand)

           self.assertEqual(reviewer, 'testuser1')
           self.assertEqual(rating, '5')
           self.assertEqual(brand, 'Wheaties')

      def test_cereal_2(self):
           cereal = Cereal.objects.get(id=2)
           reviewer = str(cereal.reviewer)
           rating = str(cereal.rating)
           brand = str(cereal.brand)

           
           self.assertEqual(reviewer, 'testuser2')
           self.assertEqual(rating, '10')
           self.assertEqual(brand, 'Cocoa Pebbles')

           

