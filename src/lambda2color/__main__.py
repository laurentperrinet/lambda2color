"""The main entry point into this package when run as a script."""

# For more details, see also
# https://docs.python.org/3/library/runpy.html
# https://docs.python.org/3/reference/import.html#special-considerations-for-main

import sys

from .lambda2color import Lambda2color


def main() -> None:
    """Execute the Lambda2color standalone command-line tool."""
    _ = Lambda2color.main()


if __name__ == "__main__":
    main()
    sys.exit()  # No exit() argument means successful termination.
