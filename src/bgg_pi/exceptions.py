"""Exceptions for bgg-pi."""

class BggError(Exception):
    """Base exception for BGG errors."""


class BggLoginError(BggError):
    """Error logging in to BGG."""
