import argparse
import yfinance as yf
import matplotlib.pyplot as plt


def project_cash_flows(last_cash_flow, growth_rate, years=5):
    """Project future cash flows based on the last available cash flow and a constant growth rate."""
    return [
        last_cash_flow * ((1 + growth_rate) ** year) for year in range(1, years + 1)
    ]


def calculate_dcf(projected_cash_flows, discount_rate):
    """Calculate the DCF valuation given projected cash flows and a discount rate."""
    present_values = [
        cf / ((1 + discount_rate) ** (i + 1))
        for i, cf in enumerate(projected_cash_flows)
    ]
    dcf_valuation = sum(present_values)
    return dcf_valuation, present_values


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Perform DCF analysis on a given stock ticker."
    )
    parser.add_argument(
        "-t",
        "--ticker",
        type=str,
        help="Ticker symbol for the stock (e.g., AAPL), optional if using interactive mode.",
    )
    parser.add_argument(
        "-d",
        "--discount_rate",
        type=float,
        help="Discount rate as a decimal (e.g., 0.1 for 10%%), optional if using interactive mode.",
    )
    parser.add_argument(
        "-i",
        "--interactive",
        action="store_true",
        help="Run in interactive mode. Overrides other arguments.",
    )
    return parser.parse_args()


def main():
    args = parse_arguments()

    if args.interactive:
        ticker_symbol = input("Enter a ticker symbol (e.g., AAPL): ")
        discount_rate = float(input("Enter your discount rate (e.g., 0.1 for 10%): "))
    else:
        if args.ticker is None or args.discount_rate is None:
            print(
                "Missing arguments. Use -i to run in interactive mode or provide both -t and -d arguments."
            )
            return
        ticker_symbol = args.ticker
        discount_rate = args.discount_rate

    ticker_data = yf.Ticker(ticker_symbol)
    cash_flows = ticker_data.cashflow.loc["Free Cash Flow"].dropna()

    # Growth rate based on the most recent two years of cash flow
    growth_rate = (cash_flows.iloc[0] - cash_flows.iloc[1]) / cash_flows.iloc[1]
    projected_cash_flows = project_cash_flows(cash_flows.iloc[0], growth_rate)

    dcf_valuation, present_values = calculate_dcf(projected_cash_flows, discount_rate)

    print(f"Projected cash flows: {projected_cash_flows}")
    print(f"DCF valuation: ${dcf_valuation:,.2f}")

    # Plotting
    years = range(1, len(projected_cash_flows) + 1)
    plt.figure(figsize=(10, 5))
    plt.plot(years, projected_cash_flows, "-o", label="Projected Cash Flows")
    plt.plot(years, present_values, "-o", label="Present Value of Cash Flows")
    plt.title(f"DCF Analysis of {ticker_symbol.upper()}")
    plt.xlabel("Year")
    plt.ylabel("Amount ($)")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
