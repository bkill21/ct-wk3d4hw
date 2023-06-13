import unittest
from wk3d4hw import Cart

class TestCart(unittest.TestCase):

    def test_add(self):
        my_cart = Cart('cart')
        my_cart.add("Pizza", 2)
        result = my_cart.cart
        expected = {'PIZZA': 2}
        self.assertEqual(result, expected)

    def test_remove(self):
        my_cart = Cart('cart')
        result = my_cart.remove("tuna", 3)
        expected = "This item does not exist in your cart."
        self.assertEqual(result, expected)

    def test_print(self):
        my_cart = Cart('cart')
        result = my_cart.show()
        self.assertEqual(result, "Your cart is currently empty")

if __name__ == '__main__':
    unittest.main()