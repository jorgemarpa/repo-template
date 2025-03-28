#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from importlib import metadata
import os

# reads version number from package metadata
__version__ = metadata.version(__package__)
PACKAGEDIR = os.path.abspath(os.path.dirname(__file__))

from .myclass import MyClass  # noqa
