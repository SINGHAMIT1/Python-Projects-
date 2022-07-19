"""
Colorama is one of the built-in Python modules to display the text in different colors.
It is used to make the code more readable.
Three formatting options are available in this module for coloring text.
These are Back, Fore and Style.
"""

import colorama
from colorama import Fore,Back,Style
colorama.init(autoreset=True)
print(Fore.BLACK+Style.BRIGHT+Back.CYAN+"I am AMIT SINGHA an upcoming PhD student of ECE in IUPUI ")
print(Fore.BLACK+Style.BRIGHT+Back.LIGHTMAGENTA_EX+"How are you"+Fore.BLACK+Back.RED+"I am Fine")
print(Fore.BLACK+Back.WHITE+"Life is hard but I will fight and win for sure")