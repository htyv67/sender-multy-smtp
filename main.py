#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Project Name: Bulk Sender Randomizer
# Author: [@zanzanmax]
# Copyright: [2024]
# Licensed under the [BSD License]

import logging
import re
import secrets
import random
import base64
import datetime
import glob
import string
import sys
import time
import os
import pyfiglet
import requests
import socket
import termcolor
import email
import email.utils
from multiprocessing.dummy import Pool
from email.utils import formatdate
from email.utils import make_msgid
import smtplib 
from smtplib import SMTPConnectError
from smtplib import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from termcolor import colored
from random import choice
from colorama import Fore, init
from email.message import EmailMessage
import html
from unidecode import unidecode
from progress.bar import Bar
from tqdm import tqdm
import keyboard
import threading
# Define color variables
red = Fore.LIGHTRED_EX
cyan = Fore.LIGHTCYAN_EX
white = Fore.WHITE
green = Fore.LIGHTGREEN_EX

def banner():
    os.system("cls||clear")
    my_banner = pyfiglet.figlet_format("Bulk Send", font="slant", justify="center")
    print(cyan + my_banner)
    print(f"\t\t{cyan}[ {green}Created By ZANZAN {white}] - [V 2.0] @zanzanmax \n")

def send_options():
    user_choice = input(" [?] Select The Sending Speed Mode, Enter 'slow' or 'fast': ")
    if user_choice == 'slow' or user_choice == 's' or user_choice == 'S':
        delay_time = input(" [?] Enter the delay time (in seconds) between sending emails: ")
        slow_send(delay_time)
    elif user_choice == 'fast' or user_choice == 'f' or user_choice == 'F':
        send_order = input(" [?] Select the sending order, Enter 'random' or 'sequential': ")
        if send_order == 'random' or send_order == 'r' or send_order == 'R':
            num_threads = input(" [?] Enter the number of threads for sending emails: ")
            fast_send_random(num_threads)
        elif send_order == 'sequential' or send_order == 's' or send_order == 'S':
            num_threads = input(" [?] Enter the number of threads for sending emails: ")
            fast_send_sequential(num_threads)
        else:
            print(" [!] Invalid sending order. Please enter 'random' or 'sequential'.")
            send_options()
    else:
        print(" [!] Invalid option. Please enter 'slow' or 'fast'.")
        send_options()



def main():
    banner()
    send_options()

if __name__ == "__main__":
    main()
