import unittest

from PyCB.gerber.router import Router, ActionNotFound


class TestRouter(unittest.TestCase):
    def setUp(self):
        self.router = Router()

    def test_add_new_action(self):
        action_pattern = "A/#"

        @self.router.action(action_pattern)
        def new_action(_):
            pass

        action = self.router.get_action(action_pattern)
        self.assertEqual(new_action, action)

    def test_call_undefined_action(self):
        self.assertRaises(ActionNotFound, self.router.call, "U/N/Defined")
