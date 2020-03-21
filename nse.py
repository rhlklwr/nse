# This is an test code and will not be deploy in production.

# import relevant package for National stock exchange
from nsetools import Nse

# instantiate NSE class
nse = Nse()
print(nse)

# function to get the data


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
