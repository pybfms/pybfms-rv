
import os
from setuptools import setup

import sys, os.path, platform, warnings

from distutils import log
from distutils.core import setup, Command
#from Cython.Build import cythonize
#from distutils.core import Distribution as _Distribution
#from distutils.core import Extension as _Extension
#from distutils.dir_util import mkpath
#from distutils.command.build_ext import build_ext as _build_ext
#from distutils.command.bdist_rpm import bdist_rpm as _bdist_rpm
#from distutils.errors import DistutilsError, CompileError, LinkError, DistutilsPlatformError

VERSION = None
with open("etc/ivpm.info") as fp:
  for line in fp:
    if line.find("version=") != -1:
      VERSION = line[line.find("=")+1:].strip()
      break

if VERSION is None:
  print("Error: null version")

if "BUILD_NUM" in os.environ:
  VERSION += "." + os.environ["BUILD_NUM"]

try:
    from wheel.bdist_wheel import bdist_wheel
except ImportError:
    bdist_wheel = None

cmdclass = {
}
if bdist_wheel:
    cmdclass['bdist_wheel'] = bdist_wheel

setup(
  name = "rv_bfms",
  version=VERSION,
  packages=['rv_bfms'],
  package_dir = {'' : 'src'},
  package_data = {'rv_bfms': ['hdl/*.v']},
  author = "Matthew Ballance",
  author_email = "matt.ballance@gmail.com",
  description = ("rv_bfms provides bus functional models for the ready/valid protocol"),
  license = "Apache 2.0",
  keywords = ["SystemVerilog", "Verilog", "RTL", "cocotb"],
  url = "https://github.com/pybfms/rv_bfms",
  setup_requires=[
    'setuptools_scm',
  ],
  cmdclass=cmdclass,
  install_requires=[
    'cocotb',
  ],
)

