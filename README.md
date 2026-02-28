# Stock Screener

A Python tool that screens S&P 500 stocks based on value investing criteria.

## What it does
Pulls real-time stock data using Yahoo Finance and filters stocks based on:
- P/E Ratio under 30 (not overvalued)
- Debt/Equity under 100 (manageable debt)
- Revenue Growth over 3% (growing business)

## How to run it

1. Install dependencies:
pip install yfinance pandas

2. Run the screener:
python3 finance_screener.py

3. Results are saved to screener_results.csv

## Example output
| Ticker | P/E | Debt/Equity | Revenue Growth |
|--------|-----|-------------|----------------|
| MSFT | 24.56 | 31.54 | 0.17 |
| GOOGL | 28.81 | 16.13 | 0.18 |
| DIS | 15.62 | 40.91 | 0.05 |

## Built with
- Python
- yfinance
- pandas
