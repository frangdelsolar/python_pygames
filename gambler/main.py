from agent import Agent


def main():
    a = Agent()

    while a.live:
        a.update()

        if a.days % 360 == 0:
            a.show()

main()