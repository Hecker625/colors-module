# Reset
RESET = "\033[0m"

def support ():
    print("""
This is the help page for the colors module.

Using this module, you can write text in multiple colors:
    colors.writecolor ("Hello, world!", colors.BLUE)
    Syntax:               { text }        { text color }

You can also write text with a background:
    colors.writebg ("Hello, world!", colors.BG_GREEN)
    Syntax:            { text }       { bg color }

The last thing you can do is do both simultaneously:
    colors.highlight ("Hello, world!", colors.BLUE, colors.BG_GREEN)
    Syntax:               { text }     { text color }  { bg color }

https://github.com/Hecker625/colors-module
    """)

def writecolor (text, color):
    print (color+text+RESET)

def writebg (text, color):
    print (color+text+RESET)

def highlight (text, color, bgcolor):
    print (color+bgcolor+text+RESET)

# Standard colors
BLACK   = "\033[30m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"

# Bright colors
BRIGHT_BLACK   = "\033[90m"
BRIGHT_RED     = "\033[91m"
BRIGHT_GREEN   = "\033[92m"
BRIGHT_YELLOW  = "\033[93m"
BRIGHT_BLUE    = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN    = "\033[96m"
BRIGHT_WHITE   = "\033[97m"

# Background colors
BG_BLACK   = "\033[40m"
BG_RED     = "\033[41m"
BG_GREEN   = "\033[42m"
BG_YELLOW  = "\033[43m"
BG_BLUE    = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN    = "\033[46m"
BG_WHITE   = "\033[47m"

# Bright background colors
BG_BRIGHT_BLACK   = "\033[100m"
BG_BRIGHT_RED     = "\033[101m"
BG_BRIGHT_GREEN   = "\033[102m"
BG_BRIGHT_YELLOW  = "\033[103m"
BG_BRIGHT_BLUE    = "\033[104m"
BG_BRIGHT_MAGENTA = "\033[105m"
BG_BRIGHT_CYAN    = "\033[106m"
BG_BRIGHT_WHITE   = "\033[107m"