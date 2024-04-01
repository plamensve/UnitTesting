from project.robot import Robot

from unittest import TestCase, main


class TestRobot(TestCase):
    def setUp(self):
        self.main_robot = Robot('1', 'Military', 100, 1000)

    def test_correct_init(self):
        self.main_robot = Robot('1', 'Military', 100, 1000)
        self.assertEqual(self.main_robot.robot_id, '1')
        self.assertEqual(self.main_robot.category, 'Military')
        self.assertEqual(self.main_robot.available_capacity, 100)
        self.assertEqual(self.main_robot.price, 1000)
        self.assertEqual(self.main_robot.hardware_upgrades, [])
        self.assertEqual(self.main_robot.software_updates, [])

    def test_category_setter_if_not_allowed_categories_raise_error(self):
        with self.assertRaises(ValueError) as ex:
            robot = Robot('1', 'Test', 100, 1000)
        self.assertEqual(f"Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'",
                         str(ex.exception))

    def test_price_setter_if_below_zero_raise_error(self):
        with self.assertRaises(ValueError) as ex:
            robot = Robot('1', 'Military', 100, -1)
        self.assertEqual("Price cannot be negative!", str(ex.exception))

    def test_upgrade_method_if_hardware_component_in_hardware_upgrades(self):
        robot = Robot('1', 'Military', 100, 1000)
        robot.hardware_upgrades = ['Test']
        result = robot.upgrade('Test', 1)
        self.assertEqual(f"Robot {robot.robot_id} was not upgraded.", result)

    def test_upgrade_method_upgrading_the_robot(self):
        robot = Robot('1', 'Military', 100, 1000)
        robot.hardware_upgrades = []
        result = robot.upgrade('Test', 1)
        self.assertEqual(f'Robot {robot.robot_id} was upgraded with {"Test"}.', result)
        self.assertEqual(robot.hardware_upgrades[0], 'Test')
        self.assertEqual(robot.price, 1001.5)

    def test_update_method(self):
        robot = Robot('1', 'Military', 100, 1000)
        robot.software_updates = [2, 3, 4]
        result = robot.update(1, 1)
        self.assertEqual(f"Robot {robot.robot_id} was not updated.", result)

        robot = Robot('1', 'Military', 101, 1000)
        robot.software_updates = [2, 3, 4]
        result = robot.update(5, 1000)
        self.assertEqual(f"Robot {robot.robot_id} was not updated.", result)

        robot = Robot('1', 'Military', 101, 1000)
        robot.software_updates = [2, 3, 4]
        result = robot.update(5, 1)
        self.assertEqual(f'Robot {robot.robot_id} was updated to version 5.', result)
        self.assertEqual(robot.software_updates[-1], 5)
        self.assertEqual(robot.available_capacity, 100)

    def test___gt__method(self):
        robot1 = Robot('1', 'Military', 101, 1000)
        robot2 = Robot('2', 'Military', 101, 1)

        result = robot1.__gt__(robot2)
        self.assertEqual(f'Robot with ID {robot1.robot_id} '
                         f'is more expensive than Robot with ID {robot2.robot_id}.', result)

        robot1 = Robot('1', 'Military', 101, 1000)
        robot2 = Robot('2', 'Military', 101, 1000)

        result1 = robot1.__gt__(robot2)
        self.assertEqual(f'Robot with ID {robot1.robot_id} '
                         f'costs equal to Robot with ID {robot2.robot_id}.', result1)

        robot1 = Robot('1', 'Military', 101, 1)
        robot2 = Robot('2', 'Military', 101, 1000)

        result2 = robot1.__gt__(robot2)
        self.assertEqual(f'Robot with ID {robot1.robot_id} '
                         f'is cheaper than Robot with ID {robot2.robot_id}.', result2)


if __name__ == '__main__':
    main()