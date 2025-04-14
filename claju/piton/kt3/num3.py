import unittest
import os
import json
import io
import sys
from tempfile import NamedTemporaryFile
from unittest.mock import patch

def display_order(order):
    return f"Заказ: {order['type']}, Цена: {order['price']}"

def file_exists(filename):
    return os.path.exists(filename)

def save_coffee_order(filename, order):
    orders = []
    if file_exists(filename):
        try:
            with open(filename, 'r') as f:
                content = f.read()
                if content: 
                    orders = json.loads(content)
        except json.JSONDecodeError:
            orders = []
    
    orders.append(order)
    with open(filename, 'w') as f:
        json.dump(orders, f)

def load_orders(filename):
    if not file_exists(filename):
        return []
    
    try:
        with open(filename, 'r') as f:
            content = f.read()
            return json.loads(content) if content else []
    except json.JSONDecodeError:
        return []

class TestCoffeeApp(unittest.TestCase):
    def setUp(self):
        self.temp_file = NamedTemporaryFile(delete=False)
        self.filename = self.temp_file.name
        self.temp_file.close()
        self.test_order = {'type': 'латте', 'price': 3.5}
    
    def tearDown(self):
        if os.path.exists(self.filename):
            os.unlink(self.filename)
    
    def test_display_order(self):
        result = display_order(self.test_order)
        self.assertEqual(result, "Заказ: латте, Цена: 3.5")
    
    def test_file_exists(self):
        self.assertTrue(file_exists(self.filename))
        self.assertFalse(file_exists('nonexistent_file.json'))
    
    def test_save_and_load_orders(self):
        save_coffee_order(self.filename, self.test_order)
        
        orders = load_orders(self.filename)
        self.assertEqual(len(orders), 1)
        self.assertEqual(orders[0]['type'], 'латте')
        self.assertEqual(orders[0]['price'], 3.5)
    
    def test_load_empty_orders(self):
        orders = load_orders('nonexistent_file.json')
        self.assertEqual(orders, [])
    
    def test_save_to_empty_file(self):
        with open(self.filename, 'w') as f:
            pass

        save_coffee_order(self.filename, self.test_order)

        orders = load_orders(self.filename)
        self.assertEqual(len(orders), 1)
    
    def test_display_order_output(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            print(display_order(self.test_order))
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "Заказ: латте, Цена: 3.5")

if __name__ == '__main__':
    unittest.main()