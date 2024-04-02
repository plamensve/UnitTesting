from project.truck_driver import TruckDriver

from unittest import TestCase, main


class TestTruckDriver(TestCase):
    def test_check_correct_init(self):
        truck_driver = TruckDriver('Ivan', 10)

        self.assertEqual('Ivan', truck_driver.name)
        self.assertEqual(10, truck_driver.money_per_mile)
        self.assertEqual({}, truck_driver.available_cargos)
        self.assertEqual(0, truck_driver.earned_money)
        self.assertEqual(0, truck_driver.miles)

    def test_earned_money_setter_if_money_is_bellow_0_raise_error(self):
        with self.assertRaises(ValueError) as ex:
            td = TruckDriver('Ivan', 10)
            td.earned_money = -10

        self.assertEqual(f"{td.name} went bankrupt.", str(ex.exception))

    def test_add_cargo_offer_if_cargo_in_available_cargos(self):
        with self.assertRaises(Exception) as ex:
            td = TruckDriver('Ivan', 10)
            td.available_cargos = {'Ruse': 50}
            result = td.add_cargo_offer('Ruse', 50)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_offer_if_cargo_not_in_available_cargos(self):
        td = TruckDriver('Ivan', 10)
        td.available_cargos = {}
        result = td.add_cargo_offer('Ruse', 50)
        result1 = td.add_cargo_offer('Borovo', 10)

        self.assertEqual(f"Cargo for 50 to Ruse was added as an offer.", result)
        self.assertEqual({'Ruse': 50, 'Borovo': 10}, td.available_cargos)

    def test_drive_best_cargo_offer(self):
        td = TruckDriver('Ivan', 10)
        td.available_cargos = {}
        result = td.drive_best_cargo_offer()

        self.assertEqual("There are no offers available.", result)

    def test_drive_best_cargo_offer_(self):
        td = TruckDriver('Ivan', 10)
        td.available_cargos = {'Ruse': 50, 'Borovo': 10}
        td.earned_money = 0
        td.miles = 0

        result = td.drive_best_cargo_offer()

        self.assertEqual(50, td.miles)
        self.assertEqual(500, td.earned_money)
        self.assertEqual(f"Ivan is driving 50 to Ruse.", result)

    def test_eat_method(self):
        td = TruckDriver('Ivan', 10)
        td.available_cargos = {'Ruse': 500, 'Borovo': 10}
        td.drive_best_cargo_offer()
        td.earned_money = 100
        td.eat(500)

        self.assertEqual(80, td.earned_money)

    def test_sleep_method(self):
        td = TruckDriver('Ivan', 10)
        td.available_cargos = {'Ruse': 1000, 'Borovo': 10}
        td.drive_best_cargo_offer()
        td.earned_money = 100
        td.sleep(1000)

        self.assertEqual(55, td.earned_money)

    def test_pump_gas(self):
        td = TruckDriver('Ivan', 10)
        td.available_cargos = {'Ruse': 1500, 'Borovo': 10}
        td.drive_best_cargo_offer()
        td.earned_money = 1000
        td.pump_gas(1500)

        self.assertEqual(500, td.earned_money)

    def test_repair_truck(self):
        td = TruckDriver('Ivan', 10)
        td.available_cargos = {'Ruse': 10000, 'Borovo': 10}
        td.earned_money = 10000
        td.repair_truck(10000)
        self.assertEqual(2500, td.earned_money)

    def test__repr__method(self):
        td = TruckDriver('Ivan', 10)
        td.available_cargos = {'Ruse': 10000}
        td.drive_best_cargo_offer()
        result = td.__repr__()
        self.assertEqual(f"Ivan has 10000 miles behind his back.", result)


if __name__ == '__main__':
    main()
