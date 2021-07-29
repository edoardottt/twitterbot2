import argparse


def get_parser():
    """Create and return a parser (argparse.ArgumentParser instance) for main()
    to use"""
    parser = argparse.ArgumentParser(description="Twitterbot v2")
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument(
        "-v", "--version", action="store_true", help="Show the version of this program"
    )

    return parser
