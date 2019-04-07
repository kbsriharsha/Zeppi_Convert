===============================
Zeppi_Convert
===============================

.. image:: https://img.shields.io/travis/kbsriharsha/Zeppi_Convert.svg
        :target: https://travis-ci.org/kbsriharsha/Zeppi_Convert

.. image:: https://img.shields.io/pypi/v/Zeppi_Convert.svg
        :target: https://pypi.python.org/pypi/Zeppi_Convert



Zeppi_Convert is a python library which convert the zeppelin notebooks to python or any other format

* Free software: MIT license

## Usage

From the command line, use Zeppi_Convert to convert a zeppelin notebook (.json) to any other format output format

    $ Zeppi_Convert -i <input_filename> -o <output_filename>

where `<output format>` is the desired output format and `<input notebook>` is the
filename of the Jupyter notebook.

### Example: Convert a zeppelin notebook to python file

Convert Juptyer notebook file, `mynotebook.ipynb`, to HTML using:

    $ Zeppi_Convert -i mynotebook.json -o mypython.py

This command takes an input zeppelin notebook and return a python file
