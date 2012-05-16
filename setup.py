from setuptools import setup, find_packages
setup(
 name='sqlalchemy_psycopg_extensions',
 version='0.0.1',
 author='Kozea',
 license='BSD',
 install_requires=['sqlalchemy>=0.7', 'psycopg2'],
 packages=find_packages()
)
