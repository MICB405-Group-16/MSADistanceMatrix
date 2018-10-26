from unittest import TestCase
from MSADistanceMatrix import MSADistanceMatrix

class TestMSADistanceMatrix(TestCase):
    def setUp(self):
        self.matrix = MSADistanceMatrix()

    def test_get_distance_matrix_string(self):
        csv_matrix = self.matrix.get_distance_matrix_string('data/all_variants_trimal.mfa')
        self.assertEqual(csv_matrix, "Sequence,ref,Bat,Cat\nref,0,6,26\nBat,6,0,22\nCat,26,22,0\n")
