#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os

PACKAGEDIR = os.path.abspath(os.path.dirname(__file__))

from .version import __version__  # noqa
from .myclass import MyClass  # noqa
