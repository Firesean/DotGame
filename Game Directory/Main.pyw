#! Python 3.7
# Project Name : DotGame
# Author : Sean Morgan
# Date : September of 2019
# Description : Using a grid of dots you will connect between each dot until all dots are
# linked. Completing a square with the lines between the dots will allow you to gain a point
# Most Points win.
# Each turn you will place a line between dots if you manage to get a box out of your turn you can go one more time.
#
import Interface
import tkinter as tk
import DotGame
GAME = DotGame.DotGame()
UI = Interface.Interface(tk.Tk(), 650, GAME)
