import sys
from os import path

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand

README = path.abspath(path.join(path.dirname(__file__), 'README.md'))

classifiers = [
    'License :: OSI Approved :: Apache Software License',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Operating System :: POSIX',
    'Operating System :: MacOS :: MacOS X',
    'Environment :: Web Environment',
    'Development Status :: 3 - Alpha',
]

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['forgot_password']
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(
      name='skygear_forgot_password',
      version='0.1.0',
      packages=find_packages(),
      description='Forgot Password Plugin for Skygear',
      long_description=open(README).read(),
      classifiers=classifiers,
      author='SkygearIO',
      author_email='hello@skygear.io',
      url='https://github.com/SkygearIO/forgot_password',
      license='Apache License, Version 2.0',
      install_requires=[
            'Jinja2>=2.8',
            'pyzmail36>=1.0.3',
            'skygear>=0.16.0',
            'nexmo>=2.0.0',
            'twilio>=6.10.4'
      ],
      cmdclass= {'test': PyTest},
      tests_require=[
            'pytest',
      ],
      package_data={
          'forgot_password': [
              'templates/*.html',
              'templates/*.txt',
          ],
      },
)
