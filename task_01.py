#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Time and Date"""


import datetime


CURDATE = None


def get_current_date():
    """This function produces current date.

    Args:
        None

    Returns:
        current local date.
    """
    return datetime.date.today()


if __name__ == '__main__':
    CURDATE = datetime.date.today()
    print CURDATE
