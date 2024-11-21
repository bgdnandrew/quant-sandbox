# Quant Sandbox: QuantSandbox.io

# Author: Bogdan Andrei
# Website: bgdnandrew.com
# X/ Twitter: @bgdnandrew

# Algo #1: Correlation Analysis

"""
This module provides functionality to calculate correlations between stock prices.

The main workflow is:

1. Data Collection:
   - Uses yfinance library to fetch historical stock data
   - Takes two stock tickers and optional date range as input
   - Retrieves adjusted closing prices for the specified stocks

2. Date Processing:
   - Handles both datetime and date objects
   - Uses default 1-year lookback if dates not provided
   - Converts datetime objects to date objects for consistency

3. Correlation Analysis:
   - Aligns the price data for both stocks
   - Calculates correlation coefficient and covariance
   - Returns statistical metrics in a dictionary format

The CorrelationCalculator class serves as a namespace containing static methods for:
- Fetching individual stock data (fetch_stock_data)
- Calculating correlation metrics between pairs of stocks (calculate)
---------------- ---------------- ---------------- ---------------- ---------------- ----------------

Performance Considerations
--------------------------------
The code makes several optimizations:

- Minimizes data copying:
    . uses pandas views where possible
    . combines operations to reduce intermediate steps

- Efficient data alignment:
    . makes use of a single pandas concat operation
    . uses built-in pandas functions for calculations

- Memory management:
    . drops unnecessary data early
    . uses the most appropriate data types



Code Evolution Insights
--------------------------------
The code's evolution shows several important learning points:

- Initial challenges:
    . data alignment issues
    . error handling gaps
    . validation problems

- Improvements made:
    . centralized data processing
    . robust error handling
    . consistent date handling
    . better metadata collection

- Final optimizations:
    . reduced data manipulation steps
    . better error messages
    . more comprehensive results



Potential Improvements
--------------------------------
Some possible enhancements could include:

- Caching mechanism for frequently accessed data
- Parallel processing for multiple stock pairs
- Data source abstraction layer
- Results persistence
- Visualization components



Best Practices Demonstrated
--------------------------------

- Separation of concerns:
    . data fetching separate from calculation
    . clear method responsibilities

- Defensive programming:
    . input validation
    . error handling
    . type checking

- Code organization:
    . logical grouping of functionality
    . clear documentation
    . consistent coding style


- Data handling:
    . proper data alignment
    . missing value handling
    . type conversion management
"""

# ----------------------------------------------------------------
# Code Evolution (status on 2024-11-13; prior to the 1st commit)  |
# ----------------------------------------------------------------
# 1st Version                     |
# --------------------------------
# - no proper error handling
# - data validation issues
# - data alignment issues
#
# --------------------------------
# 2nd Version                     |
# --------------------------------
# - added error handling
# - better data validation
# - empty data checks
#
# - still encountering data
# shape and data alignment
# issues
# - need to better handle NaN
# values
#
# --------------------------------
# 3rd Version                     |
# --------------------------------
# - tried to fix dimensionality
# issues by converting to pandas
# series explicitly
#
# - lost index information
#
# --------------------------------
# 4th Version                     |
# --------------------------------
# - tried to handle dates
# explicitly
#
# - manual date alignment was
# error-prone
#
# --------------------------------
# 5th (Final) Version             |
# --------------------------------
# - combined data processing
# - single returns calculation
# - proper date handling
# - better metadata
#
# --------------------------------

# Main Lessons Learned:

# - I trust myself when it comes to data alignment,
# but I trust pandas even more
# - process related data together rather than separately
# - validate data at each step
# - convert types explicitly when needed
# - use proper exception handling with specific error
# messages

# The final version is more robust because it:
# - minimizes data manipulation steps
# - handles dates consistently
# - has better error handling
# ----------------------------------------------------------------


import yfinance as yf  # will probably need to switch to a sturdier solution soon
import pandas as pd
import numpy as np
from datetime import datetime, timedelta, date
from typing import Dict, Any, Optional  # type hints


# merely a namespace for the static methods, a place to group them
# PRO: thus, we can group related functionality without instance state;
# no need to instantiate objects
# PRO: easy future extension
class CorrelationCalculator:
    # @staticmethod:
    # - allows method to be called without instance
    # - no self param needed
    @staticmethod
    def fetch_stock_data(
        ticker: str, start_date: datetime, end_date: datetime
    ) -> pd.Series:
        """
        Fetch stock data for a given ticker and date range.

        Uses Python type hinting.
        """
        try:
            data = yf.download(ticker, start=start_date, end=end_date, progress=False)
            if data.empty or "Adj Close" not in data.columns:
                raise ValueError(f"No data found for ticker {ticker}")
            return data["Adj Close"]
        except Exception as e:
            raise ValueError(f"Error fetching data for {ticker}: {str(e)}")

    @staticmethod
    def calculate(
        ticker1: str,
        ticker2: str,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
    ) -> Dict[str, Any]:
        """
        Calculate correlation and covariance between two stocks.

        Uses Python type hinting:
            - Optional[datetime] indicates parameters can be None.
            - Dict[str, Any] specifies return type as dictionary with string keys and any value type
        """
        try:
            # 1. Date Handling
            # --------------------------------

            # set default dates if not provided
            end_date = end_date or datetime.now()
            start_date = start_date or (end_date - timedelta(days=365))

            # 2. Date Type Conversion
            # --------------------------------

            # convert datetime to date if necessary
            start_date_val = (
                start_date.date() if isinstance(start_date, datetime) else start_date
            )
            end_date_val = (
                end_date.date() if isinstance(end_date, datetime) else end_date
            )

            # 3. Data Fetching
            # --------------------------------

            # fetch stock data
            stock1_data = CorrelationCalculator.fetch_stock_data(
                ticker1, start_date, end_date
            )
            stock2_data = CorrelationCalculator.fetch_stock_data(
                ticker2, start_date, end_date
            )

            # 4. Data Alignment
            # --------------------------------

            # create df with both series
            # preserves index information
            # handles missing dates automatically
            combined_data = pd.concat([stock1_data, stock2_data], axis=1)
            combined_data.columns = [ticker1, ticker2]

            # 5. Compute Returns
            # --------------------------------

            # compute daily returns
            returns = combined_data.pct_change()
            returns = returns.dropna()  # remove any NaN values

            # 6. Correlation Calculation
            # --------------------------------

            # check for sufficient data points
            if len(returns) < 2:
                raise ValueError("Insufficient data points for correlation calculation")

            # compute correlation and covariance
            # based on pandas built-in statistical functions
            # handles missing values appropriately
            correlation = returns[ticker1].corr(returns[ticker2])
            covariance = returns[ticker1].cov(returns[ticker2])

            # validate results
            if pd.isna(correlation) or pd.isna(covariance):
                raise ValueError("Calculation resulted in NaN values")

            # get first and last dates from index
            first_date = returns.index[0]
            last_date = returns.index[-1]

            # dictionary comprehension
            return {
                "correlation": round(float(correlation), 4),
                "covariance": round(float(covariance), 6),
                "start_date": start_date_val,
                "end_date": end_date_val,
                "ticker1": ticker1,
                "ticker2": ticker2,
                "data_points": len(returns),
                "first_date": first_date.strftime("%Y-%m-%d"),
                "last_date": last_date.strftime("%Y-%m-%d"),
                "trading_days": len(combined_data),
            }

        except Exception as e:
            raise ValueError(f"Calculation error: {str(e)}")
