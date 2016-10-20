from setuptools import setup, find_packages

from btfmonday import __version__

setup(
    name='btfmonday',
    version=__version__,
    description='Beautiful Monday',
    author='Beautiful Monday',
    author_email='btfmonday@gmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'btfmonday = btfmonday.cmd.main:main'
        ]
    }
)
