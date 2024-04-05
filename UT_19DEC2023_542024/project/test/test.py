from unittest import TestCase, main

from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(TestCase):
    def test_correct_init(self):
        new_robot = ClimbingRobot('Alpine', 'Arm', 100, 100)
        self.assertEqual('Alpine', new_robot.category)
        self.assertEqual('Arm', new_robot.part_type)
        self.assertEqual(100, new_robot.capacity)
        self.assertEqual(100, new_robot.memory)
        self.assertEqual([], new_robot.installed_software)

    def test_setter_category_if_not_in_allowed_raise_error(self):
        with self.assertRaises(ValueError) as ex:
            new_robot = ClimbingRobot('Test', 'Arm', 100, 100)
            self.assertEqual(new_robot, str(ex.exception))

    def test_get_used_capacity_method(self):
        new_robot = ClimbingRobot('Alpine', 'Arm', 10, 100)
        new_robot.installed_software = [{'name': 'clean', 'capacity_consumption': 10},
                                        {'name': 'dance', 'capacity_consumption': 10},
                                        {'name': 'trans', 'capacity_consumption': 10}]
        result = new_robot.get_used_capacity()
        self.assertEqual(30, result)

    def test_get_available_capacity(self):
        new_robot = ClimbingRobot('Alpine', 'Arm', 100, 100)
        new_robot.installed_software = [{'name': 'clean', 'capacity_consumption': 10},
                                        {'name': 'dance', 'capacity_consumption': 10},
                                        {'name': 'trans', 'capacity_consumption': 10}]
        result = new_robot.get_available_capacity()
        self.assertEqual(70, result)

    def test_get_used_memory(self):
        new_robot = ClimbingRobot('Alpine', 'Arm', 10, 100)
        new_robot.installed_software = [{'name': 'clean', 'capacity_consumption': 10, 'memory_consumption': 10},
                                        {'name': 'dance', 'capacity_consumption': 10, 'memory_consumption': 10},
                                        {'name': 'trans', 'capacity_consumption': 10, 'memory_consumption': 10}]
        result = new_robot.get_used_memory()
        self.assertEqual(30, result)

    def test_get_available_memory(self):
        new_robot = ClimbingRobot('Alpine', 'Arm', 100, 100)
        new_robot.installed_software = [{'name': 'clean', 'capacity_consumption': 10, 'memory_consumption': 10},
                                        {'name': 'dance', 'capacity_consumption': 10, 'memory_consumption': 10},
                                        {'name': 'trans', 'capacity_consumption': 10, 'memory_consumption': 10}]
        result = new_robot.get_available_memory()
        self.assertEqual(70, result)

    def test_install_software_successfully(self):
        new_robot = ClimbingRobot('Alpine', 'Arm', 100, 100)
        new_robot.installed_software = [{'name': 'clean', 'capacity_consumption': 10, 'memory_consumption': 10},
                                        {'name': 'dance', 'capacity_consumption': 10, 'memory_consumption': 10},
                                        {'name': 'trans', 'capacity_consumption': 10, 'memory_consumption': 10}]
        result = new_robot.install_software({'name': 'test', 'capacity_consumption': 10, 'memory_consumption': 10})
        self.assertEqual(f"Software 'test' successfully installed on Alpine part.", result)
        self.assertEqual(new_robot.installed_software[-1],
                         {'name': 'test', 'capacity_consumption': 10, 'memory_consumption': 10})

    def test_install_software_successfully_(self):
        new_robot = ClimbingRobot('Alpine', 'Arm', 1, 100)
        new_robot.installed_software = [{'name': 'clean', 'capacity_consumption': 10, 'memory_consumption': 10},
                                        {'name': 'dance', 'capacity_consumption': 10, 'memory_consumption': 10},
                                        {'name': 'trans', 'capacity_consumption': 10, 'memory_consumption': 10}]
        result = new_robot.install_software({'name': 'test', 'capacity_consumption': 10, 'memory_consumption': 10})
        self.assertEqual(f"Software 'test' cannot be installed on Alpine part.", result)

    def test_install_software_successfully__(self):
        new_robot = ClimbingRobot('Alpine', 'Arm', 40, 100)
        new_robot.installed_software = [{'name': 'clean', 'capacity_consumption': 10, 'memory_consumption': 10},
                                        {'name': 'dance', 'capacity_consumption': 10, 'memory_consumption': 10},
                                        {'name': 'trans', 'capacity_consumption': 10, 'memory_consumption': 10}]
        result = new_robot.install_software({'name': 'test', 'capacity_consumption': 10, 'memory_consumption': 10})
        self.assertEqual(f"Software 'test' successfully installed on Alpine part.", result)


if __name__ == '__main__':
    main()