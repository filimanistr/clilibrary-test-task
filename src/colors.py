
def sky(text: str) -> str:
    """returns colored text from red -> yellow -> white"""
    return f'\x1b[1;38;5;255m{text}\x1b[0m'

def green(text: str) -> str:
    """returns green colored text"""
    return f'\x1b[0;38;5;47m{text}\x1b[0m'

def yellow(text: str) -> str:
    """returns yellow colored text"""
    return f'\x1b[0;38;5;226m{text}\x1b[0m'

def red(text: str):
    """returns red colored text"""
    return f'\x1b[0;38;5;196m{text}\x1b[0m'
