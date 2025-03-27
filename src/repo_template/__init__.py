#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os

__version__ = "0.1.1"
PACKAGEDIR = os.path.abspath(os.path.dirname(__file__))

from .myclass import MyClass  # noqa
