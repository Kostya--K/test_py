"""
-----
Utils
-----
"""


def slugify(string):
    """Replace non-alphanumeric symbols to underscore in string.
    Args:
        string (str): string to replace
    Returns:
        str: replace string
    """
    return ''.join(s if s.isalnum() else '_' for s in string).strip('_')
