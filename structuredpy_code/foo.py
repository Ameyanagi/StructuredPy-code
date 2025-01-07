def foo(bar: str) -> str:
    """Summary line.

    Extended description of function.

    Args:
        bar: Description of input argument.

    Returns:
        Description of return value
    """

    return bar


def add(a: int | float, b: int | float) -> int | float:
    """Add two numbers together.

    Args:
        a: First number.
        b: Second number.

    Returns:
        The sum of the two numbers.
    """
    return a + b


if __name__ == "__main__":  # pragma: no cover
    pass
