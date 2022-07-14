""" Class description goes here. """

from dataclay.exceptions.ErrorDefs import ErrorCodes

__author__ = "Alex Barcelo <alex.barcelo@bsc.es>"
__copyright__ = "2015 Barcelona Supercomputing Center (BSC-CNS)"


class DataClayException(Exception):
    """Base class for exceptions in this module."""

    pass


###########
# Account #
###########


class AccountError(DataClayException):
    pass


class AccountDoesNotExistError(AccountError):
    pass


class AccountAlreadyExistError(AccountError):
    pass


###########
# Dataset #
###########


class DatasetError(DataClayException):
    pass


class DatasetDoesNotExistError(DatasetError):
    pass


class DatasetAlreadyExistError(DatasetError):
    pass


class DatasetIsNotAccessibleError(DatasetError):
    pass


###########
# Session #
###########


class SessionError(DataClayException):
    pass


class SessionDoesNotExistError(SessionError):
    pass


class SessionAlreadyExistError(SessionError):
    pass


class SessionIsNotActiveError(SessionError):
    pass
