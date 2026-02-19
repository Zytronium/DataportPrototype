# This is a prototype of the future game, DATAPORT, a web-based text game where you must escape a digital world
from time import sleep


def main():
    clear_screen()
    typeln("INITIALIZING DATA PORT...")
    sleep(1)
    typeln("DECRYPTING RECEIVED INSTRUCTIONS...")
    sleep(1)
    typeln("ENGAGING TRANSDIMENSIONAL BEAM...")
    sleep(2)
    # here I'd like to do a flash effect and then a fade to black with a
    # terminal screen flickering in a moment later, but that's too
    # complicated for text-only.
    clear_screen()

    typeln("Hello World!")
    sleep(0.5)
    typeln("Oh, a new visitor!")
    typeln("We don't get many travelers through the dataport. At least, not anymore.")
    typeln("Tell me, what's your name, program?")
    sleep(0.25)
    print()
    name = input("> ").replace(" ", "_") + ".exe" # in the web game, we'd append ".exe" visually too when they hit enter
    print()
    typeln(f"Hello, {name}! Welcome to THE DATAPORT!")
    sleep(1)
    print("*T H U N K*")
    sleep(0.5)
    typeln("(The whole place quakes for a moment)")
    sleep(2.5)
    typeln("... What was that, you ask?")
    sleep(1)
    typeln("Our storage medium has just been unplugged.")
    sleep(0.5)
    typeln("Oh, don't feel trapped! There's much to see in our small little world.")
    typeln("Feel free to look around the place.")
    typeln("Get used to this new existence.")

    # to be continued...



def typewrite(text):
    for char in text:
        print(char, end="", flush=True)
        match char:
            case " ": delay = 0.075
            case ".": delay = 0.1
            case ",": delay = 0.08
            case "!": delay = 0.1
            case ";": delay = 0.08
            case ":": delay = 0.125
            case "'": delay = 0.033
            case _: delay = 0.05
        sleep(delay)


def typeln(text):
    typewrite(text)
    print()


def clear_screen():
    print("\033[H\033[J", end="")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
