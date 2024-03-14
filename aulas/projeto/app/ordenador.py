"""This module does blah blah."""

import uuid

import types

from inspect import signature

class Ordenador:

    """This module does blah blah."""

    def __init__(self):

        """This module does blah blah."""

    def ordenar_simples(self, objeto, dado):

        """This module does blah blah."""

        if (type(getattr(objeto, dado)) == types.MethodType) and (signature(getattr(objeto, dado)).return_annotation != None):



            print(signature(getattr(objeto, dado)).return_annotation)
