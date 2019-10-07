
import os
from setuptools import setup

setup(
  name = "rv_bfms",
  packages=['rv_bfms'],
  package_dir = {'' : 'src'},
  author = "Matthew Ballance",
  author_email = "matt.ballance@gmail.com",
  description = ("rv_bfms provides bus functional models for the ready/valid protocol"),
  license = "Apache 2.0",
  keywords = ["SystemVerilog", "Verilog", "RTL", "CocoTB"],
  url = "https://github.com/sv-bfms/rv_bfms",
  setup_requires=[
    'setuptools_scm',
  ],
)

