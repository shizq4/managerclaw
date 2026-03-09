"""
Bob's API module for managerclaw project.
"""


def hello():
    """Return a greeting message."""
    return "Hello from Bob's API!"


def greet(name: str) -> str:
    """Return a personalized greeting.
    
    Args:
        name: The name to greet.
    
    Returns:
        A greeting message.
    """
    return f"Hello, {name}! Welcome to Bob's API."
