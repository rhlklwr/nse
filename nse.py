from nsetools import Nse

nse = Nse()
print(nse)


def top_gainers():
    return nse.get_top_gainers()


def top_losers():
    return nse.get_top_losers()


def adv_dec():
    return nse.get_advances_declines()


if __name__ == "__main__":
    print(
        top_gainers(),
        top_losers(),
        adv_dec()
    )
