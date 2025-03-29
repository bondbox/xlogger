# coding:utf-8

import unittest

from xkits_logger import Back
from xkits_logger import Color  # noqa:H306
from xkits_logger import Fore
from xkits_logger import Logger
from xkits_logger import Style


class TestColor(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_reset(self):
        self.assertEqual(str(Color.reset()), Style.RESET_ALL)

    def test_add_style(self):
        text1 = Color("unittest style")
        text2 = Color("unittest style")
        text1.add_style(Style.BRIGHT)
        text1.add_style(Style.UNDERLINE)
        text2.style = {Style.BRIGHT, Style.UNDERLINE}
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(text1.style, text2.style)

    def test_bold_style(self):
        text1 = Color("unittest bold")
        text2 = Color.bold(text1)
        text1.style = {Style.BRIGHT}
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_dim_style(self):
        text1 = Color("unittest dim")
        text2 = Color.dim(text1)
        text1.style = {Style.DIM}
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_normal_style(self):
        text1 = Color("unittest normal")
        text2 = Color.normal(text1)
        text1.style = {Style.NORMAL}
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_italic_style(self):
        text1 = Color("unittest italic")
        text2 = Color.italic(text1)
        text1.style = {Style.ITALIC}
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_underline_style(self):
        text1 = Color("unittest underline")
        text2 = Color.underline(text1)
        text1.style = {Style.UNDERLINE}
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_slow_blink_style(self):
        text1 = Color("unittest slow_blink")
        text2 = Color.slow_blink(text1)
        text1.style = {Style.SLOWBLINK}
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_rapid_blink_style(self):
        text1 = Color("unittest rapid_blink")
        text2 = Color.rapid_blink(text1)
        text1.style = {Style.RAPIDBLINK}
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_invert_style(self):
        text1 = Color("unittest invert")
        text2 = Color.invert(text1)
        text1.style = {Style.INVERT}
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_hide_style(self):
        text1 = Color("unittest hide")
        text2 = Color.hide(text1)
        text1.style = {Style.HIDE}
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_strikethrough_style(self):
        text1 = Color("unittest strikethrough")
        text2 = Color.strikethrough(text1)
        text1.style = {Style.STRIKETHROUGH}
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_doubly_underlined_style(self):
        text1 = Color("unittest doubly_underlined")
        text2 = Color.doubly_underlined(text1)
        text1.style = {Style.DOUBLYUNDERLINED}
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_reveal_style(self):
        text1 = Color("unittest reveal")
        text2 = Color.reveal(text1)
        text1.style = {Style.REVEAL}
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_black_foreground(self):
        text1 = Color("unittest black")
        text2 = Color.black(text1)
        text1.foreground = Fore.BLACK
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_red_foreground(self):
        text1 = Color("unittest red")
        text2 = Color.red(text1)
        text1.foreground = Fore.RED
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_green_foreground(self):
        text1 = Color("unittest green")
        text2 = Color.green(text1)
        text1.foreground = Fore.GREEN
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_yellow_foreground(self):
        text1 = Color("unittest yellow")
        text2 = Color.yellow(text1)
        text1.foreground = Fore.YELLOW
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_blue_foreground(self):
        text1 = Color("unittest blue")
        text2 = Color.blue(text1)
        text1.foreground = Fore.BLUE
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_magenta_foreground(self):
        text1 = Color("unittest magenta")
        text2 = Color.magenta(text1)
        text1.foreground = Fore.MAGENTA
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_cyan_foreground(self):
        text1 = Color("unittest cyan")
        text2 = Color.cyan(text1)
        text1.foreground = Fore.CYAN
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_white_foreground(self):
        text1 = Color("unittest white")
        text2 = Color.white(text1)
        text1.foreground = Fore.WHITE
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_lightblack_foreground(self):
        text1 = Color("unittest lightblack")
        text2 = Color.lightblack(text1)
        text1.foreground = Fore.LIGHTBLACK_EX
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_lightred_foreground(self):
        text1 = Color("unittest lightred")
        text2 = Color.lightred(text1)
        text1.foreground = Fore.LIGHTRED_EX
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_lightgreen_foreground(self):
        text1 = Color("unittest lightgreen")
        text2 = Color.lightgreen(text1)
        text1.foreground = Fore.LIGHTGREEN_EX
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_lightyellow_foreground(self):
        text1 = Color("unittest lightyellow")
        text2 = Color.lightyellow(text1)
        text1.foreground = Fore.LIGHTYELLOW_EX
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_lightblue_foreground(self):
        text1 = Color("unittest lightblue")
        text2 = Color.lightblue(text1)
        text1.foreground = Fore.LIGHTBLUE_EX
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_lightmagenta_foreground(self):
        text1 = Color("unittest lightmagenta")
        text2 = Color.lightmagenta(text1)
        text1.foreground = Fore.LIGHTMAGENTA_EX
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_lightcyan_foreground(self):
        text1 = Color("unittest lightcyan")
        text2 = Color.lightcyan(text1)
        text1.foreground = Fore.LIGHTCYAN_EX
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_lightwhite_foreground(self):
        text1 = Color("unittest lightwhite")
        text2 = Color.lightwhite(text1)
        text1.foreground = Fore.LIGHTWHITE_EX
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_black_background(self):
        text1 = Color("unittest black")
        text2 = Color.black_back(text1)
        text1.background = Back.BLACK
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_red_background(self):
        text1 = Color("unittest red")
        text2 = Color.red_back(text1)
        text1.background = Back.RED
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_green_background(self):
        text1 = Color("unittest green")
        text2 = Color.green_back(text1)
        text1.background = Back.GREEN
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_yellow_background(self):
        text1 = Color("unittest yellow")
        text2 = Color.yellow_back(text1)
        text1.background = Back.YELLOW
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_blue_background(self):
        text1 = Color("unittest blue")
        text2 = Color.blue_back(text1)
        text1.background = Back.BLUE
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_magenta_background(self):
        text1 = Color("unittest magenta")
        text2 = Color.magenta_back(text1)
        text1.background = Back.MAGENTA
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_cyan_background(self):
        text1 = Color("unittest cyan")
        text2 = Color.cyan_back(text1)
        text1.background = Back.CYAN
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_white_background(self):
        text1 = Color("unittest white")
        text2 = Color.white_back(text1)
        text1.background = Back.WHITE
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_lightblack_background(self):
        text1 = Color("unittest lightblack")
        text2 = Color.lightblack_back(text1)
        text1.background = Back.LIGHTBLACK_EX
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_lightred_background(self):
        text1 = Color("unittest lightred")
        text2 = Color.lightred_back(text1)
        text1.background = Back.LIGHTRED_EX
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_lightgreen_background(self):
        text1 = Color("unittest lightgreen")
        text2 = Color.lightgreen_back(text1)
        text1.background = Back.LIGHTGREEN_EX
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_lightyellow_background(self):
        text1 = Color("unittest lightyellow")
        text2 = Color.lightyellow_back(text1)
        text1.background = Back.LIGHTYELLOW_EX
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_lightblue_background(self):
        text1 = Color("unittest lightblue")
        text2 = Color.lightblue_back(text1)
        text1.background = Back.LIGHTBLUE_EX
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_lightmagenta_background(self):
        text1 = Color("unittest lightmagenta")
        text2 = Color.lightmagenta_back(text1)
        text1.background = Back.LIGHTMAGENTA_EX
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_lightcyan_background(self):
        text1 = Color("unittest lightcyan")
        text2 = Color.lightcyan_back(text1)
        text1.background = Back.LIGHTCYAN_EX
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))

    def test_lightwhite_background(self):
        text1 = Color("unittest lightwhite")
        text2 = Color.lightwhite_back(text1)
        text1.background = Back.LIGHTWHITE_EX
        Logger.stdout(f"text1: {text1}")
        Logger.stdout(f"text2: {text2}")
        self.assertEqual(str(text1), str(text2))


if __name__ == "__main__":
    unittest.main()
