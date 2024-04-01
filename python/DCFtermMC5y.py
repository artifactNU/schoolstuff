import argparse
import yfinance as yf
import matplotlib.pyplot as plt


def project_cash_flows(last_cash_flow, growth_rate, years=10):
    """Project future cash flows based on the last available cash flow and a constant growth rate."""
    return [
        last_cash_flow * ((1 + growth_rate) ** year) for year in range(1, years + 1)
    ]


def calculate_terminal_value(last_projected_cf, perpetuity_growth_rate, discount_rate):
    """Calculate the Terminal Value using the Perpetuity Growth Model."""
    return (
        last_projected_cf
        * (1 + perpetuity_growth_rate)
        / (discount_rate - perpetuity_growth_rate)
    )


def calculate_dcf_with_tv(projected_cash_flows, discount_rate, perpetuity_growth_rate):
    """Calculate the DCF valuation including Terminal Value."""
    present_values = [
        cf / ((1 + discount_rate) ** (i + 1))
        for i, cf in enumerate(projected_cash_flows)
    ]
    last_projected_cf = projected_cash_flows[-1]
    terminal_value = calculate_terminal_value(
        last_projected_cf, perpetuity_growth_rate, discount_rate
    )
    terminal_value_pv = terminal_value / (
        (1 + discount_rate) ** len(projected_cash_flows)
    )
    total_dcf_valuation = sum(present_values) + terminal_value_pv
    return total_dcf_valuation, present_values, terminal_value, terminal_value_pv


def calculate_growth_rate(cash_flows, periods=3):
    """Calculate the average annual growth rate based on the last 'periods' reported periods of cash flow."""
    if len(cash_flows) < periods + 1:
        raise ValueError(
            f"Need at least {periods + 1} periods of cash flows to calculate growth rate accurately."
        )

    growth_rates = []
    for i in range(1, periods):
        growth_rate = (
            cash_flows.iloc[-i] - cash_flows.iloc[-(i + 1)]
        ) / cash_flows.iloc[-(i + 1)]
        growth_rates.append(growth_rate)

    average_growth_rate = sum(growth_rates) / len(growth_rates)
    return average_growth_rate


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
        help="Discount rate as a decimal (e.g., 0.1 for 10%%).",
    )
    parser.add_argument(
        "-g",
        "--growth_rate",
        type=float,
        help="Perpetuity growth rate as a decimal (e.g., 0.02 for 2%%), optional.",
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

    if args.interactive or args.growth_rate is None:
        ticker_symbol = input("Enter a ticker symbol (e.g., AAPL): ")
        discount_rate = float(input("Enter your discount rate (e.g., 0.1 for 10%): "))
        perpetuity_growth_rate = float(
            input("Enter the perpetuity growth rate (e.g., 0.02 for 2%): ")
        )
    else:
        ticker_symbol = args.ticker
        discount_rate = args.discount_rate
        perpetuity_growth_rate = args.growth_rate

    ticker_data = yf.Ticker(ticker_symbol)
    cash_flows = ticker_data.cashflow.loc["Free Cash Flow"].dropna()

    try:
        growth_rate = calculate_growth_rate(cash_flows, 3)
    except ValueError as e:
        print(e)
        return

    latest_cash_flow = cash_flows.iloc[0]
    projected_cash_flows = project_cash_flows(latest_cash_flow, growth_rate, years=10)

    dcf_valuation, present_values, terminal_value, terminal_value_pv = (
        calculate_dcf_with_tv(
            projected_cash_flows, discount_rate, perpetuity_growth_rate
        )
    )

    market_cap = ticker_data.info["marketCap"]

    print(f"Projected cash flows: {projected_cash_flows}")
    print(f"Terminal Value (Present Value): ${terminal_value_pv:,.2f}")
    print(f"Total DCF valuation: ${dcf_valuation:,.2f}")
    print(f"Current Market Cap: ${market_cap:,.2f}")

    if dcf_valuation > market_cap:
        print("Based on DCF, the stock appears to be undervalued.")
    else:
        print("Based on DCF, the stock appears to be overvalued.")

    years = list(range(1, len(projected_cash_flows) + 1))
    terminal_year = len(projected_cash_flows) + 1

    plt.figure(figsize=(10, 5))
    plt.plot(years, projected_cash_flows, "-o", label="Projected Cash Flows")
    plt.plot([terminal_year], [terminal_value_pv], "ro", label="Terminal Value")
    plt.axhline(y=market_cap, color="g", linestyle="-", label="Current Market Cap")
    plt.title(f"DCF Analysis of {ticker_symbol.upper()}")
    plt.xlabel("Year")
    plt.ylabel("Amount ($)")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
