import yfinance as yf
import pandas as pd

tickers = [
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'META', 'TSLA', 'BRK-B',
    'JPM', 'JNJ', 'V', 'PG', 'UNH', 'HD', 'MA', 'DIS', 'BAC', 'XOM', 'NFLX', 'COST'
]

results = []

for ticker in tickers:
    try:
        info = yf.Ticker(ticker).info
        pe = info.get('trailingPE')
        de = info.get('debtToEquity')
        rev_growth = info.get('revenueGrowth')

        if pe and de and rev_growth:
            if pe < 30 and de < 100 and rev_growth > 0.03:
                results.append({
                    'Ticker': ticker,
                    'P/E': round(pe, 2),
                    'Debt/Equity': round(de, 2),
                    'Revenue Growth': round(rev_growth, 2)
                })
    except:
        continue

df = pd.DataFrame(results)
print(df)
df.to_csv('screener_results.csv', index=False)
print("Done! Results saved to screener_results.csv")