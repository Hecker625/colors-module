# colors-module
A simple module to print text in color

Do colors.support () for help.

Using this module, you can write text in multiple colors:
    colors.writecolor ("Hello, world!", colors.BLUE)
    Syntax:               { text }        { text color }

You can also write text with a background:
    colors.writebg ("Hello, world!", colors.BG_GREEN)
    Syntax:            { text }       { bg color }

The last thing you can do is do both simultaneously:
    colors.highlight ("Hello, world!", colors.BLUE, colors.BG_GREEN)
    Syntax:               { text }     { text color }  { bg color }

Here are the available colors:
BLACK

RED
GREEN
YELLOW
BLUE
MAGENTA
CYAN
WHITE

# Bright colors
BRIGHT_BLACK
BRIGHT_RED
BRIGHT_GREEN
BRIGHT_YELLOW
BRIGHT_BLUE
BRIGHT_MAGENTA
BRIGHT_CYAN
BRIGHT_WHITE

# Background colors
BG_BLACK
BG_RED
BG_GREEN
BG_YELLOW
BG_BLUE
BG_MAGENTA
BG_CYAN
BG_WHITE

# Bright background colors
BG_BRIGHT_BLACK
BG_BRIGHT_RED


BG_BRIGHT_GREEN
BG_BRIGHT_YELLOW
BG_BRIGHT_BLUE
BG_BRIGHT_MAGENTA
BG_BRIGHT_CYAN
BG_BRIGHT_WHITE

(Github isn't showing the format correctly so open up the file directly)
