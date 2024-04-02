from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):
    def test_correct_init(self):
        self.toy_store = ToyStore()
        self.assertEqual(self.toy_store.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })

    def test_add_toy_method_shelf_not_in_store(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store = ToyStore()
            self.toy_store.add_toy('K', 'ToyTestName')
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_method_if_toy_in_the_shelf(self):
        self.toy_store = ToyStore()
        self.toy_store.add_toy('A', 'ToyTestName')
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('A', 'ToyTestName')
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_but_shelf_is_not_empty(self):
        self.toy_store = ToyStore()
        self.toy_store.add_toy('A', 'ToyTestName')
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('A', 'Test')

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_successfully(self):
        self.toy_store = ToyStore()
        result = self.toy_store.add_toy('A', 'ToyTestName')
        self.assertEqual(f"Toy:ToyTestName placed successfully!", result)
        self.assertEqual(self.toy_store.toy_shelf['A'], 'ToyTestName')

    def test_remove_toy_if_shelf_not_exist_raise_error(self):
        self.toy_store = ToyStore()
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy('T', 'Test')
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_if_shelf_not_exist_raise_error_(self):
        self.toy_store = ToyStore()
        self.toy_store.add_toy('A', 'Test')
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy('A', 'Test1')
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_if_shelf_not_exist_raise_error__(self):
        self.toy_store = ToyStore()
        self.toy_store.add_toy('A', 'Test')
        result = self.toy_store.remove_toy('A', 'Test')
        self.assertEqual(f"Remove toy:Test successfully!", result)
        self.assertEqual(self.toy_store.toy_shelf['A'], None)


if __name__ == '__main__':
    main()
