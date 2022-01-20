import unittest

func = __import__("func")

class TestFunc(unittest.TestCase):

  def test_func(self):
    resp, code = func.main({})
    self.assertEqual(resp["predictions"], [1,2,3])
    self.assertEqual(code, 200)

if __name__ == "__main__":
  unittest.main()