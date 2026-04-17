import portfolio.data
import portfolio.report
import sys

if __name__ == "__main__":
    print(sys.path)

    my_portfolio = portfolio.data.create_portfolio("Retirement")
    portfolio.report.print_report(my_portfolio)