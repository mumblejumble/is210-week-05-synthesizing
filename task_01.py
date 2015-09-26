#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_01"""


import datetime


CURDATE = None


def get_current_date():
    """returning today's date from imported datetime"""
    return datetime.date.today()


if __name__ == '__main__':
    print datetime.date.today()
    CURDATE = datetime.date.today()
