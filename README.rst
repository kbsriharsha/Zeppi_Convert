===============================
Zeppi_Convert
===============================

.. image:: https://img.shields.io/travis/mecsys/Zeppi_ConvertX.svg
        :target: https://travis-ci.org/mecsys/Zeppi_ConvertX

.. image:: https://img.shields.io/pypi/v/Zeppi_ConvertX.svg
        :target: https://pypi.python.org/pypi/Zeppi_ConvertX



Zeppi_Convert is a python library which can convert the zeppelin notebooks to python or any other formats. It has the built in capability to extract the code from different kind of interpreter cells.

Zeppi_Convert got three arguments,

* i : input file to be converted(required)
* o : output file to be returned(optional)(default: outputs a zeppiconvert.txt file)
* int : specific interpreter cells to be converted (optional) (deafult: extracts the code from all the cells)

Usage
======================


From the command line, use the keyword ``zeppi-convert`` to convert a zeppelin notebook (.json) to any other format output format

    ``$ zeppi-convert -i <input_filename> -o <output_filename> -int <interpreter_type>``

Example1: Extract the code from all the cells and output a python file

    ``$ zeppi_convert -i mynotebook.json -o mypython.py``

Example2: Convert a zeppelin notebook to any text format

    ``$ zeppi_convert -i mynotebook.json -o myfile.txt``

Example3: Extract the code from a specific interpreter cells

    ``$ zeppi_convert -i mynotebook.json -o myfile.txt -int pyspark``
