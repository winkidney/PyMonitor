import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requires = [
    'psutil',
]

setup(name='PyMonitor',
      version='0.1',
      description='Monitor system status',
      classifiers=[
        "Programming Language :: Python",
      ],
      author='',
      author_email='',
      url='',
      keywords='system tools',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="none",
      )
