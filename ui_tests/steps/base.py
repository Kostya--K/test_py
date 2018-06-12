"""
----------
Base steps
----------
"""


class BaseSteps(object):
    """Base steps."""

    def __init__(self, app):
        """Constructor.

        Args:
            app (object): application instance
        """
        self.app = app

    def _open(self, page):
        current_page = self.app.current_page
        if page.__class__ != current_page.__class__:

            if getattr(page, 'navigate_items', None):
                current_page.navigate(page.navigate_items)

            else:
                page.open()

        return page
