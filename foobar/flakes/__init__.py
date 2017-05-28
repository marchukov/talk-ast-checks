"""
Module with custom source code checks.

This module provides a set of flakes8 checks that are enabled
there through the entry points set in setup.py.

Those code checks are local to this project.
"""


import ast


class KwArgsChecker(object):
    """Check public methods to use keyword arguments."""

    name = 'KwArgsChecker'
    version = '0.1'

    def __init__(self, tree):
        self.tree = tree

    def _failure_msg(self, node):
        return (node.lineno,
                node.col_offset,
                'X001 only keyword arguments are allowed in public methods',
                self.name)

    def run(self):
        """Method is called by flake to run this checker."""
        for node in ast.walk(self.tree):
            # Skip everything that is not a function definition
            if not isinstance(node, ast.FunctionDef):
                continue
            # Skip non-public methods (including constructors in this case)
            if node.name.startswith('_'):
                continue

            arguments = node.args
            # If we have positional arguments defined
            if arguments.args:
                # More than one positional argument
                if len(arguments.args) > 1:
                    yield self._failure_msg(node)
                # Only one positional argument. We allow only 'self' or 'cls'
                if arguments.args[0].arg not in ['self', 'cls']:
                    yield self._failure_msg(node)
            # If we take '*args'
            if arguments.vararg:
                yield self._failure_msg(node)
