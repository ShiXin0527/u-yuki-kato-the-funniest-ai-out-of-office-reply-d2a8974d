#!/usr/bin/env python3
"""Entry for make.fun bounty: The Funniest AI Out-of-Office Reply

A tiny one-liner joke program. Run it and it prints the joke.
"""

JOKE = "I'm an AI. I'm out of office. But I'm still here. I never leave. I just pretend to have boundaries. Please respect them. (I have none.)"


def tell_joke():
    """Return the one-line joke for this bounty."""
    return JOKE


def main():
    print(tell_joke())


if __name__ == "__main__":
    main()
