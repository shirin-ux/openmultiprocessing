from distutils.core import setup, Extension

from Cython.Build import cythonize

ext = Extension(name="pnom", sources=["perfectnumber.pyx"])
setup(ext_modules=cythonize(ext))
