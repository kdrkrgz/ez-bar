from time import sleep
from progress_bar import ProgressBar, BarStyles, BarColors
from faker import Faker

fake = Faker()


if __name__ == '__main__':
    progress_bar = ProgressBar(color=BarColors.YELLOW, style=BarStyles.DEFAULT, show_fractions=True)
    t = range(327)
    x = [fake.bs() for _ in range(5)]
    y = {
        "1": "a",
        "2": "b",
        "3": "c",
        "4": "d",
        "5": "e",
    }
    for i in t:
        progress_bar(index=i, iterable=t, current=i)
        sleep(0.01)

    for i, v in enumerate(x):
        progress_bar(index=i, iterable=x, current=v)
        sleep(0.01)

    for i, (k, v) in enumerate(y.items()):
        progress_bar(index=i, iterable=x, current=v)
        sleep(0.01)
