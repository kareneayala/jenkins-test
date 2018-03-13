from setuptools import setup, find_packages
tests_require = [
    'mock',
    'nose',
    ]

setup(
    name= 'sample',
    version= '1.3.0',
    description= 'A sample Python project',
    install_requires=['peppercorn'],
    tests_require=tests_require,
    test_suite = 'nose.collector'
)
