import yfinance as yf
import matplotlib.pyplot as plt


def project_cash_flows(last_cash_flow, growth_rate, years=5):
    """project future cash flows based on the last available cash flow and a constant growth rate."""
    return [
        last_cash_flow * ((1 + growth_rate) ** year) for year in range(1, years + 1)
    ]


def calculate_dcf(projected_cash_flows, discount_rate):
    """calculate the DCF valuation given projected cash flows and a discount rate."""
    present_values = [
        cf / ((1 + discount_rate) ** (i + 1))
        for i, cf in enumerate(projected_cash_flows)
    ]
    dcf_valuation = sum(present_values)
    return dcf_valuation, present_values


def main():
    ticker_symbol = input("enter a ticker symbol (e.g., AAPL): ")
    ticker_data = yf.Ticker(ticker_symbol)
    cash_flows = ticker_data.cashflow.loc["Free Cash Flow"].dropna()

    # growth rate based on the most recent two years of cash flow
    growth_rate = (cash_flows.iloc[0] - cash_flows.iloc[1]) / cash_flows.iloc[1]
    projected_cash_flows = project_cash_flows(cash_flows.iloc[0], growth_rate)

    discount_rate = float(input("enter your discount rate (e.g., 0.1 for 10%): "))
    dcf_valuation, present_values = calculate_dcf(projected_cash_flows, discount_rate)

    print(f"projected cash flows: {projected_cash_flows}")
    print(f"DCF valuation: ${dcf_valuation:,.2f}")

    # plotting
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


# ticker_data = yf.Ticker("AAPL")
# print(
#     ticker_data.cashflow.index
# )  # This will print the rows' names, i.e., the types of cash flows


# # Assuming you have already fetched the ticker data as `ticker_data`
# cash_flow_data = ticker_data.cashflow

# # Access specific metrics
# free_cash_flow = cash_flow_data.loc["Free Cash Flow"]
# capital_expenditure = cash_flow_data.loc["Capital Expenditure"]
# operating_cash_flow = cash_flow_data.loc["Operating Cash Flow"]

# # Print the most recent values
# print(f"Most recent Free Cash Flow: {free_cash_flow.iloc[0]}")
# print(f"Most recent Capital Expenditure: {capital_expenditure.iloc[0]}")
# print(f"Most recent Operating Cash Flow: {operating_cash_flow.iloc[0]}")
