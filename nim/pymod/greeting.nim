##   python path/to/pmgen.py greeting.nim

import strutils  # `%` operator

import pymod
import pymodpkg/docstrings

proc greet*(audience: string): string {.exportpy.} =
  docstring"""Greet the specified audience with a familiar greeting."""
  return "Hello, $1!" % audience

initPyModule("hw", greet)
