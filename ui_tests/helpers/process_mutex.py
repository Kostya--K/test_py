"""
-------------------
Interprocess locker
-------------------
"""

import portalocker


class Lock(object):
    """Process mutex."""

    def __init__(self, filename):
        self.filename = filename
        self.handle = open(self.filename, 'w')

    def acquire(self):
        """Acquire lock."""
        portalocker.lock(self.handle, portalocker.LOCK_EX)

    def release(self):
        """Release lock."""
        portalocker.lock(self.handle, portalocker.LOCK_UN)

    def __enter__(self):
        """Enter to context."""
        self.acquire()
        return self

    def __exit__(self, ext_type, exc_val, exc_tb):
        """Exit from context."""
        self.release()

    def __del__(self):
        """Delete object."""
        self.handle.close()
