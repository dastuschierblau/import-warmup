from portfolio import *
import sys

if __name__ == "__main__":
    print(sys.path)

    my_portfolio = data.create_portfolio("Retirement")
    report.print_report(my_portfolio)