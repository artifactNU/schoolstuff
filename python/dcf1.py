import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import argparse


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
        description="Discounted Cash Flow (DCF) Analysis with Visualizations"
    )
    parser.add_argument(
        "ticker", type=str, help="Ticker symbol for the stock (e.g., AAPL)"
    )
    parser.add_argument(
        "discount_rate",
        type=float,
        help="Discount rate as a decimal (e.g., 0.1 for 10%)",
    )
    return parser.parse_args()


def main():
    args = parse_arguments()

    ticker_data = yf.Ticker(args.ticker)
    cash_flows = ticker_data.cashflow.loc[
        "Total Cash From Operating Activities"
    ].dropna()

    if len(cash_flows) < 2:
        print(f"Not enough data to calculate growth rate for {args.ticker}")
        return

    growth_rate = (cash_flows.iloc[0] - cash_flows.iloc[1]) / cash_flows.iloc[1]
    projected_cash_flows = project_cash_flows(cash_flows.iloc[0], growth_rate)

    dcf_valuation, present_values = calculate_dcf(
        projected_cash_flows, args.discount_rate
    )

    print(f"Projected Cash Flows: {projected_cash_flows}")
    print(f"DCF Valuation: ${dcf_valuation:,.2f}")

    # Plotting
    years = range(1, len(projected_cash_flows) + 1)
    plt.figure(figsize=(10, 5))
    plt.plot(years, projected_cash_flows, "-o", label="Projected Cash Flows")
    plt.plot(years, present_values, "-o", label="Present Value of Cash Flows")
    plt.title(f"DCF Analysis of {args.ticker.upper()}")
    plt.xlabel("Year")
    plt.ylabel("Amount ($)")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
