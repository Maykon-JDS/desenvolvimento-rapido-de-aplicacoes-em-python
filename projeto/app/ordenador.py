"""This module does blah blah."""

import uuid

import types

from inspect import signature

class Ordenador:

    """This module does blah blah."""

    @staticmethod
    def ordenar_simples(objeto, dado):

        """This module does blah blah."""

        if type(getattr(objeto, dado)) == types.MethodType:

            return signature(getattr(objeto, dado)).return_annotation
