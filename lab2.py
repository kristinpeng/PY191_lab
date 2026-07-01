import curses

text = """Hello world!
This is a tiny text editor.
Edit me!"""

cursor = 0


def draw(screen):
    screen.clear()

    display = text[:cursor] + "|" + text[cursor:]
    # ----------------------------------------

    for row, line in enumerate(display.split("\n")):
        screen.addstr(row, 0, line)

    screen.addstr(
        len(display.split("\n")) + 1,
        0,
        "← → Move   Type Insert   Backspace Delete   Enter New Line   Esc Quit"
    )

    screen.refresh()


def main(screen):
    global text, cursor, display

    while True:
        draw(screen)

        key = screen.getch()

        if key == 27:
            break

        # ==========================================================

        elif key == curses.KEY_LEFT:

            if cursor > 0:
                cursor -= 1

            display = text[:cursor] + "|" + text[cursor:]
        # ----------------------------------------

        elif key == curses.KEY_RIGHT:

            if cursor < len(text):
                cursor += 1

            display = text[:cursor] + "|" + text[cursor:]

        # ----------------------------------------
        elif key in (8, 127, curses.KEY_BACKSPACE):

            if cursor > 0:
                text = text[:cursor - 1] + text[cursor:]
                cursor -= 1

            display = text[:cursor] + "|" + text[cursor:]

        # ----------------------------------------

        elif key == 10:

            text = text[:cursor] + "\n" + text[cursor:]
            cursor += 1

            display = text[:cursor] + "|" + text[cursor:]

        # ==========================================================

        elif 32 <= key <= 126:

            text = text[:cursor] + chr(key) + text[cursor:]
            cursor += 1

            display = text[:cursor] + "|" + text[cursor:]

        # ----------------------------------------

        elif key == curses.KEY_UP:
            count = 0
            if cursor > 0:
                while cursor > 0 and text[cursor - 1] != "\n":
                    cursor -= 1
                    count += 1
                if cursor != 0:
                    if cursor > 0:
                        cursor -= 1
                        while cursor > 0 and text[cursor - 1] != "\n":
                            cursor -= 1

                    for i in range(count):
                        if cursor < len(text) and text[cursor] != "\n":
                            cursor += 1

        elif key == curses.KEY_DOWN:
            count = 1
            if cursor > 0:
                while cursor > 0 and text[cursor - 1] != "\n":
                    cursor -= 1
                    count += 1
            while cursor < len(text) and text[cursor] != "\n":
                cursor += 1
            cursor += 1
            if text[cursor] != "\n":
                for i in range(count-1):
                    if cursor < len(text) and text[cursor] != "\n":
                        cursor += 1


curses.wrapper(main)
