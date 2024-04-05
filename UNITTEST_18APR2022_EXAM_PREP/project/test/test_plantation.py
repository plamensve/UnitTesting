from project.plantation import Plantation

from unittest import TestCase, main


class TestPlantation(TestCase):
    def test_check_correct_init(self):
        plant = Plantation(100)
        self.assertEqual(100, plant.size)
        self.assertEqual({}, plant.plants)
        self.assertEqual([], plant.workers)

    def test_setter_of_value_if_bellow_zero_raise_error(self):
        with self.assertRaises(ValueError) as ex:
            plant = Plantation(-2)
        self.assertEqual("Size must be positive number!", str(ex.exception))

    def test_hire_worker_method_if_worker_not_in_workers_raise_error(self):
        with self.assertRaises(ValueError) as ex:
            plant = Plantation(100)
            plant.workers = ['Plamen']
            plant.hire_worker('Plamen')
            self.assertEqual("Worker already hired!", str(ex.exception))

    def test_hire_worker_method_successfully(self):
        plant = Plantation(100)
        plant.workers = []
        result = plant.hire_worker('Plamen')
        self.assertEqual('Plamen', plant.workers[0])
        self.assertEqual(f"Plamen successfully hired.", result)

    def test_hire_worker_method_add_to_last_element(self):
        plant = Plantation(100)
        plant.workers = []
        result = plant.hire_worker('Plamen')
        result = plant.hire_worker('Ivan')
        self.assertEqual('Ivan', plant.workers[-1])     # TODO

    def test__len__method(self):
        plant = Plantation(100)
        plant.plants = {'Plamen': ['Rose'], 'Ivan': ['BlackRose']}
        result = plant.__len__()
        self.assertEqual(2, result)

    def test__len__method_(self):
        plant = Plantation(100)
        plant.plants = {'Plamen': ['Rose']}
        result = plant.__len__()
        self.assertEqual(1, result)

    def test_planting_method_worker_is_not_hired(self):
        with self.assertRaises(ValueError) as ex:
            plant = Plantation(100)
            plant.workers = ['Plamen']
            result = plant.planting('Ivan', 'plant')

        self.assertEqual(f"Worker with name Ivan is not hired!", str(ex.exception))

    def test_planting_method_plant_is_full(self):
        with self.assertRaises(ValueError) as ex:
            plant = Plantation(1)
            plant.workers = ['Pl', 'Iv']
            plant.plants = {'Pl': ['BlackRoseRoseRose']}
            plant.planting('Pl', 'Rose')
        self.assertEqual("The plantation is full!", str(ex.exception))

    def test_planting_method_append_plant(self):
        plant = Plantation(100)
        plant.workers = ['Plamen']
        plant.plants = {'Plamen': ['Rose']}
        result = plant.planting('Plamen', 'Rose')
        self.assertEqual(f"Plamen planted Rose.", result)
        self.assertEqual({'Plamen': ['Rose', 'Rose']}, plant.plants)

    def test_planting_method_if_worker_not_in_workers(self):
        plant = Plantation(10)
        plant.workers = ['Plamen']
        plant.plants = {}
        result = plant.planting('Plamen', 'Rose')
        self.assertEqual(f"Plamen planted it's first Rose.", result)
        self.assertEqual({'Plamen': ['Rose']}, plant.plants)

    def test__str__method(self):
        plant = Plantation(100)
        plant.workers = ['Plamen', 'Ivan']
        plant.plants = {'Plamen': ['Rose', 'BlackRose'], 'Ivan': ['Rose']}
        result = plant.__str__()
        self.assertEqual(f"Plantation size: 100\n"
                         f"Plamen, Ivan\n"
                         f"Plamen planted: Rose, BlackRose\n"
                         f"Ivan planted: Rose"
                         , result)

    def test__repr__method(self):
        plant = Plantation(10)
        plant.workers = ['Plamen', 'Ivan']
        result = plant.__repr__()
        self.assertEqual(f'Size: 10\n'
                         f'Workers: Plamen, Ivan'
                         , result)


if __name__ == '__main__':
    main()
