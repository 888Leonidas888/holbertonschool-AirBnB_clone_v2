#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Clase para probar la funcionalidad de la consola"""

    def setUp(self):
        """Configurtación inical para las pruebas"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Limpiar de las pruebas"""
        del self.console

    def test_do_quit(self):
        """Prueba para verificar que do_quit devueleve True"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.console.onecmd("EOF"))
            self.assertEqual(mock_stdout.getvalue(), "")
