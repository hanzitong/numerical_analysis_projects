from setuptools import setup, find_packages

setup(name="van_der_pol",
      packages=find_packages(),
      install_requires=['matplotlib', 'pytest'])
      # install_requires=['matplotlib', 'nlopt', 'numpy', 'scipy'])


