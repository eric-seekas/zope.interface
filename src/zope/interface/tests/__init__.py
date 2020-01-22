from zope.interface._compat import _should_attempt_c_optimizations


class OptimizationTestMixin(object):
    """
    Helper for testing that C optimizations are used
    when appropriate.
    """

    def _getTargetClass(self):
        """
        Define this to return the implementation in use,
        without the 'Py' or 'Fallback' suffix.
        """
        raise NotImplementedError

    def _getFallbackClass(self):
        """
        Define this to return the fallback Python implementation.
        """
        # Is there an algorithmic way to do this? The C
        # objects all come from the same module so I don't see how we can
        # get the Python object from that.
        raise NotImplementedError

    def test_optimizations(self):
        used = self._getTargetClass()
        fallback = self._getFallbackClass()

        if _should_attempt_c_optimizations():
            self.assertIsNot(used, fallback)
        else:
            self.assertIs(used, fallback)
