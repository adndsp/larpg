from setuptools import setup, find_packages

setup(
    name = 'larpg',
    version = '0.0.0',
    install_requires = [
        ],

    tests_require = [
        'nose>=1.0.0'
        ],
    packages = find_packages(),
    include_package_data = True,
    test_suite = 'nose.collector',
    zip_safe = False,
    entry_points = {}
    )
