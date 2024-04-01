from unittest import TestCase, main

from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(TestCase):
    def setUp(self):
        self.robot = ClimbingRobot('Alpine', 'Arm', 10, 10)

    def test_correct_init(self):
        self.assertEqual('Alpine', self.robot.category)
        self.assertEqual('Arm', self.robot.part_type)
        self.assertEqual(10, self.robot.capacity)
        self.assertEqual(10, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)

    def test_category_setter_if_not_in_allowed_categories_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = 'Test'

        self.assertEqual(f"Category should be one of {self.robot.ALLOWED_CATEGORIES}", str(ve.exception))

    def test_install_software_if_capacity_is_not_enough(self):
        software = {'name': 'Soft1', 'capacity_consumption': 2, 'memory_consumption': 1}
        self.test_robot = ClimbingRobot('Alpine', 'Arm', 1, 1)

        result = self.test_robot.install_software(software)

        self.assertEqual(f"Software '{software['name']}' cannot be installed on Alpine part.", result)

    def test_install_software_if_memory_is_not_enough(self):
        software = {'name': 'Soft1', 'capacity_consumption': 1, 'memory_consumption': 2}
        self.test_robot = ClimbingRobot('Alpine', 'Arm', 2, 1)

        result = self.test_robot.install_software(software)

        self.assertEqual(f"Software '{software['name']}' cannot be installed on Alpine part.", result)

    def test_install_software_if_memory_and_capacity_are_not_enough(self):
        software = {'name': 'Soft1', 'capacity_consumption': 2, 'memory_consumption': 2}
        self.test_robot = ClimbingRobot('Alpine', 'Arm', 1, 1)

        result = self.test_robot.install_software(software)

        self.assertEqual(f"Software '{software['name']}' cannot be installed on Alpine part.", result)

    def test_install_software_if_memory_and_capacity_are_enough(self):
        software = {'name': 'Soft1', 'capacity_consumption': 1, 'memory_consumption': 1}
        self.test_robot = ClimbingRobot('Alpine', 'Arm', 5, 5)
        result = self.test_robot.install_software(software)

        self.assertEqual("Software 'Soft1' successfully installed on Alpine part.", result)
        self.assertEqual([{'name': 'Soft1', 'capacity_consumption': 1, 'memory_consumption': 1}],
                         self.test_robot.installed_software)

    def test_install_software_if_memory_and_capacity_are_equal(self):
        software = {'name': 'Soft1', 'capacity_consumption': 5, 'memory_consumption': 5}
        self.test_robot = ClimbingRobot('Alpine', 'Arm', 5, 5)
        result = self.test_robot.install_software(software)

        self.assertEqual("Software 'Soft1' successfully installed on Alpine part.", result)
        self.assertEqual([{'name': 'Soft1', 'capacity_consumption': 5, 'memory_consumption': 5}],
                         self.test_robot.installed_software)

    def test_get_used_capacity(self):
        software = {'name': 'Soft1', 'capacity_consumption': 1, 'memory_consumption': 1}
        software2 = {'name': 'Soft2', 'capacity_consumption': 1, 'memory_consumption': 1}
        self.test_robot = ClimbingRobot('Alpine', 'Arm', 5, 5)
        self.test_robot.install_software(software)
        self.test_robot.install_software(software2)
        result_1 = self.test_robot.get_used_capacity()
        self.assertEqual(2, result_1)

    def test_get_available_capacity(self):
        software = {'name': 'Soft1', 'capacity_consumption': 1, 'memory_consumption': 1}
        software2 = {'name': 'Soft2', 'capacity_consumption': 1, 'memory_consumption': 1}
        self.test_robot = ClimbingRobot('Alpine', 'Arm', 5, 5)
        self.test_robot.install_software(software)
        self.test_robot.install_software(software2)
        result = self.test_robot.get_available_capacity()
        self.assertEqual(3, result)

    def test_get_used_memory(self):
        software = {'name': 'Soft1', 'capacity_consumption': 1, 'memory_consumption': 1}
        software2 = {'name': 'Soft2', 'capacity_consumption': 1, 'memory_consumption': 1}
        self.test_robot = ClimbingRobot('Alpine', 'Arm', 5, 5)
        self.test_robot.install_software(software)
        self.test_robot.install_software(software2)
        result = self.test_robot.get_used_memory()
        self.assertEqual(2, result)

    def test_get_available_memory(self):
        software = {'name': 'Soft1', 'capacity_consumption': 1, 'memory_consumption': 1}
        software2 = {'name': 'Soft2', 'capacity_consumption': 1, 'memory_consumption': 1}
        self.test_robot = ClimbingRobot('Alpine', 'Arm', 5, 5)
        self.test_robot.install_software(software)
        self.test_robot.install_software(software2)
        result = self.test_robot.get_available_memory()
        self.assertEqual(3, result)


if __name__ == '__main__':
    main()
