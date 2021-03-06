"""
Hyperparameter search study
===========================

The hyperparameter search study is designed to get some visualisation and results processing after running an hyperparameter search. It will provide you an overview of evaluations done during the search as well as a search trajectory with respect to your objective value. Finally you will find the best set of hyperparameters found by the search.

The command line is::

    deephyper-analytics hps --path $path --name $name

An example use of this command line can be as follow::

    deephyper-analytics hps -p ../../database/testdb/data/TEST/test_de03094c/results.csv -n newnotebook

"""

import os
import argparse
from deephyper.core.plot.jn_loader import NbEdit

HERE = os.path.dirname(os.path.abspath(__file__))


def hps_analytics(path_to_data_file, nb_name='dh-analytics-hps'):
    path_to_data_file = os.path.abspath(path_to_data_file)
    editor = NbEdit(os.path.join(HERE, 'stub/hps_analytics.ipynb'),
                    path_to_save=f"{nb_name}.ipynb")

    try:
        venv_name = os.environ.get('VIRTUAL_ENV').split('/')[-1]
        editor.setkernel(venv_name)
    except Exception:
        pass

    editor.edit(0, "{{path_to_data_file}}", path_to_data_file)

    editor.edit(1, "{{path_to_data_file}}", f"'{path_to_data_file}'")

    editor.write()

    editor.execute()


def add_subparser(subparsers):
    subparser_name = 'hps'
    function_to_call = main

    parser_parse = subparsers.add_parser(
        subparser_name, help='Tool to generate analytics on a single HPS experiment (jupyter notebook).')
    parser_parse.add_argument('-p',
                              '--path', type=str, help='A CSV file generated by the search.')
    parser_parse.add_argument('-n', '--name', type=str,
                              default='dh-analytics-hps',
                              help='Name of the produced jupyter notebook.')

    return subparser_name, function_to_call


def main(path, name, *args, **kwargs):
    hps_analytics(path_to_data_file=path, nb_name=name)
