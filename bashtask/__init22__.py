# -*- coding: utf-8 -*-
__author__ = "Antonio Sánchez (asanchez@plutec.net)"
__version__ = "0.6"
__copyright__ = "Copyright (c) 2014 Antonio Sánchez"
__license__ = "GPL2"

import bashtask
import database

__all__ = ['bashtask']

def insert(command, priority=None):
    bashtask.insert(command, priority)

def create_database():
    database.Database().create_db()
    