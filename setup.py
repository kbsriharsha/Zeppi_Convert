from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.rst'), encoding='utf-8') as readme_file:
    readme = readme_file.read()

setup(
    name = 'Zeppi_Convert',
    version = '0.1.2',
    keywords="zeppelin convert to python notebooks interpreter",
    description="Convert your zeppelin notebooks to python",
    long_description=readme,
    author = "Harsha Karpurapu",
    author_email='kbsriharsha@gmail.com',
    url='https://github.com/kbsriharsha/Zeppi_Convert',
    packages = find_packages(exclude=['contrib']),
    license="MIT",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points = {
        'console_scripts': [
            'zeppi-convert = Zeppi_Convert.__main__:main'
        ]
    })
