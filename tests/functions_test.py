import unittest
from main import *

class TestFunctions(unittest.TestCase):
    #def setUp(self):
        #pass

    def test_distance(self):
        tulos = distance((3, 3), (5, 9))
        self.assertEqual(str(6.32455532), str(tulos)[:10])

    def test_generate_points(self):
        testpoints = generate_points(3, 100, 100, 10)
        self.assertLess(testpoints[0][0], (95))
        self.assertLess(testpoints[1][1], (95))
        self.assertGreater(distance(testpoints[0], testpoints[1]), 10)

    def test_add_super_triangle(self):
        testx, testy = 100, 100
        self.assertEqual(add_super_triangle(testx, testy), ((-1, -1), (200, -1), (-1, 200)))

    def test_is_collinear(self):
        testpoints = ((1, 2), (2, 4), (3, 6))
        testpoints2 = ((1, 3), (2, 4), (3, 6))
        self.assertTrue(is_collinear(testpoints[0], testpoints[1], testpoints[2]))
        self.assertFalse(is_collinear(testpoints2[0], testpoints2[1], testpoints2[2]))

    def test_circumcircle(self):
        triangletest = ((3, 3), (4, 4), (5, 3.5))
        triangletest2 = ((1, 2), (2, 3), (2, 3))
        triangletest3 = ((0, 1), (2, 3), (3, 3))
        self.assertAlmostEqual(circumcircle(*triangletest)[0][0], 4.083333333)
        self.assertAlmostEqual(circumcircle(*triangletest)[0][1], 2.916666667)
        self.assertEqual(circumcircle(*triangletest2)[0], None)
        self.assertEqual(circumcircle(*triangletest2)[1], None)
        self.assertAlmostEqual(circumcircle(*triangletest3)[1], 2.549509756796)

    def test_inside_circumcircle(self):
        testtriangle = ((1, 1), (3, 1), (3, 3))
        self.assertTrue(inside_circumcircle((2, 1.5), testtriangle))
        self.assertFalse(inside_circumcircle((3, 3.5), testtriangle))
        self.assertFalse(inside_circumcircle((0, 0), ((1, 2), (2, 4), (3, 6))))

    def test_get_edges(self):
        testtriangle = ((1,1), (2, 2), (3,5))
        self.assertEqual(get_edges(testtriangle), (((1, 1), (2, 2)), ((2, 2), (3, 5)), ((3, 5), (1, 1))))

    def test_shared_edge(self):
        testtriangles = [((1, 1), (3, 1), (3, 3)), ((2, 2), (3, 1), (3, 3))]
        testedge = ((3, 3), (3, 1))
        self.assertEqual(shared_edge(testedge, testtriangles), 2)
        self.assertEqual(shared_edge(tuple(reversed(testedge)), testtriangles), 2)

    def test_generate_rooms(self):  
        testpoints = [(319, 159), (753, 464), (186, 783), (681, 584), (459, 169)]
        testdistance = 10
        testrooms = generate_rooms(testpoints, testdistance)
        self.assertEqual(len(testrooms), 5)     #Paranna testiä.

    def test_generate_start_point(self):
        testpoints = [(11, 11), (777, 11), (11, 777), (777, 777), (600, 666), (555, 543), (25, 75), (75, 25), (600, 200), (799, 500), (599, 50), (50, 600), (432, 123), (321, 567), (765, 350), (222, 666)]
        testdistance = 10
        teststartpoint = generate_start_point(testpoints, 800, 800, testdistance)
        testexamples = [(11, 11), (777, 11), (11, 777), (777, 777)]
        self.assertTrue(teststartpoint in testexamples)

    def test_pathing(self):
        teststart = (0, 0)
        testtriangles = [((0, 0), (1, 1), (2, 4)), ((1, 1), (3, 1), (3, 3)), ((2, 2), (3, 1), (3, 3))]
        testpath = pathing(testtriangles, teststart)
        self.assertEqual(len(testpath), 6)      #Paranna testiä.
