"""
The credentials created for those regions that Telegram and its domains had been blocked in there.
First, We will use JSON format to extract the proxies than, we will upload them into proxy function.
"""

import logging
import json

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
