"""
Author: Madhurima Rawat

This Streamlit application is designed for a comprehensive stock market prediction project. It includes functionality for navigating different project sections, visualizing data, evaluating models, and predicting stock prices using preprocessed datasets. The app incorporates background customization, dropdown and radio button inputs, and interactive visualizations.

This script is used for the deployed app on Streamlit.

Libraries used:
- Streamlit: For building the web-based interactive application framework.
- Pandas: Used for data manipulation and analysis, especially with data frames.
- OS: For handling file and directory paths within the system.
- Matplotlib: Used for generating static plots and charts.
- NumPy: For numerical computations and array operations.
- Plotly: For creating interactive and dynamic visual plots.
- Pickle: Used for loading pre-trained machine learning models.
- Scikit-learn (implied): For model handling and text feature extraction.
- TextBlob: For basic natural language processing tasks.

Functions are explained below:

This Streamlit app provides an interactive platform for analyzing stock market data and models, including numerical, text-based, and hybrid approaches. The app allows users to explore data, view visualizations, evaluate models, and make predictions.

Functions Used:
- display_stock_market_description: Shows a detailed description of the stock market.
- display_project_description: Provides an overview of the project goals and scope.
- display_company_data_table: Displays a table of company-related data.
- display_numerical_dataset_info: Shows information about numerical datasets.
- display_numerical_data_visualizations: Displays visualizations for numerical datasets.
- display_numerical_model_performance: Shows evaluation metrics for numerical models.
- display_numerical_model_visualization: Visualizes numerical model outputs.
- display_numerical_model_predicted: Predicts stock closing prices.
- display_text_model_performance: Evaluates text-based model performance.
- display_text_model_visualization: Visualizes outputs from text-based models.
- display_text_model_prediction: Makes predictions using text-based models.
- display_hybrid_model_performance: Evaluates hybrid model performance.
- display_hybrid_model_visualization: Visualizes outputs from hybrid models.
- display_hybrid_model_prediction: Predicts using hybrid models.
- display_project_database: Provides information on InfluxDB database setup.
- display_project_dashboard: Links or embeds the Grafana dashboard.
- display_project_flask_app: Links or embeds the Flask app for predictions.
- display_contact_information: Shows contact info for the project team.
- display_resources_information: Lists various project-related resources and illustrations.
"""

# Importing Streamlit for building the web-based interactive application framework
import streamlit as st

# Importing Pandas for data manipulation and analysis
import pandas as pd

# Importing OS module for handling file and directory paths
import os

# Importing Matplotlib for generating static plots and charts
import matplotlib.pyplot as plt

# Importing NumPy for numerical computations and array operations
import numpy as np

# Importing Plotly for creating interactive and dynamic visual plots
import plotly.graph_objects as go

# Importing Pickle for loading pre-trained machine learning models
import pickle

# Importing TfidfVectorizer from scikit-learn for text feature extraction
from sklearn.feature_extraction.text import TfidfVectorizer

# Importing TextBlob for basic natural language processing tasks
from textblob import TextBlob

# Setting the page title
# This title will only be visible when running the app locally.
# In the deployed app, the title will be displayed as "Title - Streamlit," where "Title" is the one we provide.
# If we don't set the title, it will default to "Streamlit"
st.set_page_config(page_title="Stock Prediction")

# To show Font Awesome icons
css_example = """
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"> """


# Function to display information about stock market
def display_stock_market_description():

    # Stock Market Overview Markdown
    stock_market_overview = """
    ## Stock Market Overview

    The stock market is a complex system where investors buy and sell shares of publicly traded companies. Understanding fundamental concepts and terminologies is essential for navigating and analyzing market activities effectively.

    ### 1. **What is the Stock Market?**
    - **Definition**: A platform where investors can buy and sell shares of publicly listed companies.
    - **Components**:
    - **Stock Exchanges**: Physical or electronic venues where trading occurs (e.g., NYSE, NASDAQ, BSE).
    - **Listed Companies**: Businesses that have issued shares to the public through an initial public offering (IPO).
    - **Investors**: Individuals or institutions that purchase shares to gain ownership stakes and potential returns.

    ### 2. **Key Terminologies**

    #### a. **Stock (Share)**
    - **Definition**: A unit of ownership in a company.
    - **Types**:
    - **Common Stock**: Provides voting rights and potential dividends.
    - **Preferred Stock**: Typically no voting rights but has a higher claim on assets and dividends.

    #### b. **Stock Exchange**
    - **Definition**: An organized market where securities are bought and sold.
    - **Examples**:
    - **New York Stock Exchange (NYSE)**
    - **NASDAQ**
    - **Bombay Stock Exchange (BSE)**

    #### c. **Index**
    - **Definition**: A statistical measure representing the performance of a group of stocks.
    - **Examples**:
    - **BSE Sensex (BSESN)**: Tracks 30 major companies on the BSE.
    - **S&P 500**: Tracks 500 large-cap U.S. companies.
    - **NASDAQ Composite**: Includes over 3,000 stocks listed on NASDAQ.

    #### d. **Bid and Ask Price**
    - **Bid Price**: The highest price a buyer is willing to pay for a stock.
    - **Ask Price**: The lowest price a seller is willing to accept for a stock.
    - **Spread**: The difference between the bid and ask prices.

    #### e. **Market Order vs. Limit Order**
    - **Market Order**: An order to buy or sell immediately at the current market price.
    - **Limit Order**: An order to buy or sell at a specific price or better.

    #### f. **Volume**
    - **Definition**: The number of shares traded during a specific period.
    - **Significance**: Indicates the activity level and liquidity of a stock.

    #### g. **Volatility**
    - **Definition**: A measure of how much a stock's price fluctuates over a given period.
    - **Types**:
    - **High Volatility**: Large price swings, indicating higher risk.
    - **Low Volatility**: Smaller price movements, indicating lower risk.

    #### h. **Liquidity**
    - **Definition**: The ease with which a stock can be bought or sold without affecting its price.
    - **High Liquidity**: Stocks can be traded quickly with minimal price impact.
    - **Low Liquidity**: Trades may significantly impact the stock price.

    #### i. **Dividend**
    - **Definition**: A portion of a company's earnings distributed to shareholders.
    - **Types**:
    - **Cash Dividend**: Paid in cash.
    - **Stock Dividend**: Paid in additional shares.

    ### 3. **How the Stock Market Works**

    - **Initial Public Offering (IPO)**:
    - **Definition**: The process by which a private company offers shares to the public for the first time.
    - **Purpose**: To raise capital for expansion, pay off debt, or provide liquidity to existing shareholders.

    - **Secondary Market**:
    - **Definition**: The market where previously issued securities are traded among investors.
    - **Function**: Provides liquidity and enables price discovery.

    - **Trading Mechanism**:
    - **Order Matching**: Buy and sell orders are matched through an exchange's order book.
    - **Execution**: Once matched, the trade is executed, and ownership of the shares is transferred.

    ### 4. **Investment Strategies**

    #### a. **Fundamental Analysis**
    - **Definition**: Evaluating a company's financial health, performance, and intrinsic value.
    - **Components**:
    - **Financial Statements**: Income statement, balance sheet, cash flow statement.
    - **Ratios**: Price-to-earnings (P/E), debt-to-equity, return on equity (ROE).
    - **Qualitative Factors**: Management quality, competitive advantage, industry conditions.

    #### b. **Technical Analysis**
    - **Definition**: Analyzing statistical trends from trading activity, such as price and volume.
    - **Tools**:
    - **Charts**: Line charts, bar charts, candlestick charts.
    - **Indicators**: Moving averages, Relative Strength Index (RSI), MACD.

    #### c. **Quantitative Analysis**
    - **Definition**: Using mathematical and statistical models to evaluate securities.
    - **Approach**:
    - **Algorithmic Trading**: Automated trading based on predefined criteria.
    - **Risk Management Models**: Assessing and mitigating financial risks.

    ### 5. **Risk and Return**

    - **Risk**: The possibility of losing some or all of the invested capital.
    - **Return**: The gain or loss generated by an investment.
    - **Risk-Return Tradeoff**: Higher potential returns typically come with higher risk.

    ### 6. **Regulatory Bodies**

    - **Securities and Exchange Commission (SEC)**: U.S. regulatory body overseeing securities markets.
    - **Securities and Exchange Board of India (SEBI)**: Regulatory authority for securities markets in India.
    - **Role**:
    - **Protecting Investors**: Ensuring transparency and fairness in the markets.
    - **Regulating Exchanges**: Setting rules and guidelines for trading activities.
    - **Preventing Fraud**: Detecting and penalizing fraudulent activities.

    ### 7. **Market Participants**

    - **Retail Investors**: Individual investors buying and selling securities for personal accounts.
    - **Institutional Investors**: Entities like mutual funds, pension funds, and insurance companies managing large portfolios.

    ### 8. **Bull and Bear Markets**: 
    - A **bull market** refers to a phase where stock prices are rising or are expected to rise, signaling optimism and confidence among investors.
    - A **bear market** describes a situation where prices are falling or are expected to fall, reflecting pessimism and caution in the market. Investors typically take long positions during bull markets and short positions during bear markets, depending on their market outlook.
    """

    # Display the overview in Streamlit
    st.markdown(stock_market_overview)


# Function to Display Project Description
def display_project_description():
    st.markdown(
        """
     <h3>Project Description</h3>
    <p>This project aims to analyze and visualize the trends in the stock market using historical financial data. The data is retrieved from Yahoo Finance and analyzed using Python libraries like Pandas and Matplotlib. The visualizations include line graphs, candlestick charts, and scatter plots to showcase the trends in stock prices and volumes.</p>

    <img src="https://img.freepik.com/premium-vector/flat-design-stock-market-analysis_23-2148590818.jpg" style="width: 100%;">
    
    <br>
    <br>
    <h3>Project Overview</h3>

    <p>Our project aims to forecast stock prices by combining numerical data and textual analysis. We utilize historical stock data and insights from financial news to create a robust prediction model.</p>

    <h4>Methodology</h4>

    <ol>
        <li><strong>Data Collection</strong>: We gather historical stock prices of major companies and store them in an InfluxDB database for efficient time-series analysis.</li>
        <li><strong>Data Visualization</strong>: We use Grafana to create dashboards that visualize stock prices and forecast outcomes in real-time.</li>
        <li><strong>Textual Analysis</strong>: Using Natural Language Processing (NLP) tools like NLTK and spaCy, we analyze financial news to gain insights that enhance our predictions.</li>
        <li><strong>Machine Learning</strong>: We are experimenting with advanced models such as ARIMA, LSTM, and Transformers, integrating both numerical and textual data to improve forecasting accuracy.</li>
        <li><strong>Collaboration</strong>: The project is managed through GitHub, allowing our team to collaborate effectively and keep track of changes.</li>
    </ol>

    <h3>Tools Used</h3>

    <ul>
        <li><strong>InfluxDB</strong>: A time-series database for managing stock data.</li>
        <li><strong>Grafana</strong>: A visualization tool for creating dashboards.</li>
        <li><strong>NLP Libraries</strong>: NLTK and spaCy for textual analysis.</li>
        <li><strong>Machine Learning Models</strong>: ARIMA, LSTM, and Transformers for stock price prediction.</li>
    </ul>

    """,
        unsafe_allow_html=True,
    )


# Function to display the company data table with logos and details
def display_company_data_table():
    st.markdown(
        """
    <h4>This are all the datasets that are used in the analysis.</h4>

    <table style="width:100%; border-collapse:collapse;">
        <thead>
            <tr style="border-bottom:1px solid #ddd; text-align:left;">
                <th>Company</th>
                <th>Description</th>
                <th>Data Range</th>
                <th>Dataset Shape</th>
                <th>Starting Stock Date</th>
                <th>Current Stock Date</th>
                <th>Starting Stock Price</th>
                <th>Current Stock Price</th>
            </tr>
        </thead>
        <tbody>
            <!-- Google -->
            <tr>
                <td><img src="https://www.freepnglogos.com/uploads/google-logo-png/google-logo-png-suite-everything-you-need-know-about-google-newest-0.png"
                        height="40" /> <br> Alphabet Inc. (Google) [GOOG]</td>
                <td>Specializes in Internet-related services and products, including search engines, online advertising, and
                    cloud computing.</td>
                <td>2014-03-27 : 2024-10-17</td>
                <td>(2659, 5)</td>
                <td>2014-03-27</td>
                <td>2024-10-17</td>
                <td>$27.8542</td>
                <td>$164.51</td>
            </tr>
            <!-- Amazon -->
            <tr>
                <td><img src="https://pngimg.com/uploads/amazon/amazon_PNG5.png" height="40" /> <br> Amazon.com Inc. [AMZN]
                </td>
                <td>Started as an online bookstore, now a leader in e-commerce and cloud computing through AWS.</td>
                <td>1997-05-16 : 2024-10-17</td>
                <td>(6901, 5)</td>
                <td>1997-05-16</td>
                <td>2024-10-17</td>
                <td>$0.0863</td>
                <td>$187.53</td>
            </tr>
            <!-- Apple -->
            <tr>
                <td><img src="https://th.bing.com/th/id/R.0ac491574e7ddb71dc2cab65a8bb501f?rik=5NzURUJ1L37UYg&riu=http%3a%2f%2fpurepng.com%2fpublic%2fuploads%2flarge%2fpurepng.com-apple-logologobrand-logoiconslogos-251519938788qhgdl.png&ehk=kQ%2bTI4imrP%2fg9UWIfehFMJOqAn1A3RQTROHV%2f1ORknk%3d&risl=&pid=ImgRaw&r=0"
                        height="40" /> <br> Apple Inc. [AAPL]</td>
                <td>Renowned for innovative consumer electronics, software, and services, including the iPhone and Mac
                    computers.</td>
                <td>1980-12-12 : 2024-10-17</td>
                <td>(11053, 5)</td>
                <td>1980-12-12</td>
                <td>2024-10-17</td>
                <td>$0.0992</td>
                <td>$232.15</td>
            </tr>
            <!-- Meta Platforms -->
            <tr>
                <td><img src="https://static.vecteezy.com/system/resources/previews/024/273/862/original/meta-logo-transparent-free-png.png"
                        height="40" /> <br> Meta Platforms [META]</td>
                <td>Owner of Facebook, a global leader in social media and digital advertising.</td>
                <td>2012-05-18 : 2024-10-17</td>
                <td>(3124, 5)</td>
                <td>2012-05-18</td>
                <td>2024-10-17</td>
                <td>$38.1174</td>
                <td>$576.93</td>
            </tr>
            <!-- Microsoft -->
            <tr>
                <td><img src="https://upload.wikimedia.org/wikipedia/commons/4/44/Microsoft_logo.svg" height="40" /> <br>
                    Microsoft Corp. [MSFT]</td>
                <td>A leading developer of software, consumer electronics, and personal computers.</td>
                <td>1986-03-13 : 2024-10-17</td>
                <td>(9728, 5)</td>
                <td>1986-03-13</td>
                <td>2024-10-17</td>
                <td>$0.0603</td>
                <td>$416.72</td>
            </tr>
            <!-- Netflix -->
            <tr>
                <td><img src="https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg" height="40" /> <br>
                    Netflix Inc. [NFLX]</td>
                <td>Global streaming entertainment service with a vast library of TV series and films.</td>
                <td>2002-05-23 : 2024-10-17</td>
                <td>(5640, 5)</td>
                <td>2002-05-23</td>
                <td>2024-10-17</td>
                <td>$1.1964</td>
                <td>$687.65</td>
            </tr>
            <!-- Nvidia -->
            <tr>
                <td><img src="https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/235_Nvidia_logo-512.png"
                        height="40" /> <br> Nvidia Corp. [NVDA]</td>
                <td>Specializes in graphics processing units and AI technology.</td>
                <td>1999-01-22 : 2024-10-17</td>
                <td>(6477, 5)</td>
                <td>1999-01-22</td>
                <td>2024-10-17</td>
                <td>$0.0377</td>
                <td>$136.93</td>
            </tr>
            <!-- Tata Consultancy Services (TCS) -->
            <tr>
                <td><img src="https://companieslogo.com/img/orig/TCS.NS-7401f1bd.png?t=1631949260" height="40" /> <br> Tata
                    Consultancy Services [TCS]</td>
                <td>Leading global IT services, consulting, and business solutions provider.</td>
                <td>2013-11-01 : 2024-10-17</td>
                <td>(2758, 5)</td>
                <td>2013-11-01</td>
                <td>2024-10-17</td>
                <td>$543.0</td>
                <td>$11.8</td>
            </tr>
        </tbody>        
    </table>
    """,
        unsafe_allow_html=True,
    )


# Directory containing the preprocessed datasets
DATASET_DIR = "Codes/Historical_Data_Analysis/Preprocessed_Dataset"


# Function to load dataset based on ticker symbol and display its information
def display_numerical_dataset_info(ticker):
    # Define the dataset file path
    dataset_path = os.path.join(DATASET_DIR, f"Preprocessed_{ticker}_Dataset.csv")

    # Check if file exists
    if not os.path.isfile(dataset_path):
        st.error(f"No dataset found for ticker symbol: {ticker}")
        return

    # Load the dataset with 'date' as the index
    df = pd.read_csv(dataset_path, index_col="date")
    df.index.name = "Date"  # Rename index label to 'Date'

    # Display company information based on the ticker symbol
    company_info = {
        "AAPL": "Apple Inc.",
        "GOOG": "Alphabet Inc. (Google)",
        "AMZN": "Amazon.com Inc.",
        "META": "Meta Platforms",
        "MSFT": "Microsoft Corp.",
        "NFLX": "Netflix Inc.",
        "NVDA": "Nvidia Corp.",
        "TCS": "Tata Consultancy Services",
    }

    # Display company name
    company_name = company_info.get(ticker, "Unknown Company")
    st.write(f"**Company Name:** {company_name}")

    # Show dataset details
    st.write("**Dataset Information:**")
    st.write(f"- **Shape:** {df.shape}")
    st.write(f"- **Date Range:** {df.index[0]} to {df.index[-1]}")

    # Capitalize column names for display
    df.columns = [col.capitalize() for col in df.columns]

    # Display starting stock information (first row) and current stock information (last row)
    st.write("**Starting Stock:**")
    st.write(df.iloc[0])

    st.write("**Current Stock:**")
    st.write(df.iloc[-1])

    # Display the first five rows of the dataset (with 'Date' as the index label)
    st.write("**First Five Rows:**")
    st.dataframe(df.head())


# Function to display visualizations for the selected ticker
def display_numerical_data_visualizations(ticker):
    # Define the dataset file path
    dataset_path = os.path.join(DATASET_DIR, f"Preprocessed_{ticker}_Dataset.csv")

    # Check if the dataset file exists
    if not os.path.isfile(dataset_path):
        st.error(f"No dataset found for ticker symbol: {ticker}")
        return

    # Load the dataset
    df = pd.read_csv(dataset_path, index_col="date", parse_dates=True)

    # Calculate Moving Average
    df["Moving Average"] = df["close"].rolling(window=20).mean()

    # Calculate RSI
    delta = df["close"].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df["RSI"] = 100 - (100 / (1 + rs))

    # Create the line graph for Open, High, Low, Close prices
    st.subheader(f"{ticker} Price Visualization")
    price_fig = go.Figure()

    price_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["open"],
            mode="lines",
            name="Open",
            line=dict(color="#fade2a", width=2, dash="dash"),
        )
    )
    price_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["high"],
            mode="lines",
            name="High",
            line=dict(color="#f2495c", width=2, dash="dash"),
        )
    )
    price_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["low"],
            mode="lines",
            name="Low",
            line=dict(color="#5794f2", width=2, dash="dash"),
        )
    )
    price_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["close"],
            mode="lines",
            name="Close",
            line=dict(color="#73bf69", width=4),
            opacity=0.5,
        )
    )

    price_fig.update_layout(
        title="Stock Price Visualization",
        xaxis_title="Date",
        yaxis_title="Price in USD ($)",
        template="plotly_white",
    )
    st.plotly_chart(price_fig)

    # Bar chart for Volume
    st.subheader(f"{ticker} Volume Visualization")

    volume_fig = go.Figure()

    # Set the pastel orange bar color and white outline color
    volume_fig.add_trace(
        go.Bar(
            x=df.index,
            y=df["volume"],
            marker=dict(
                color="teal",  # Pastel Orange for bars
                line=dict(color="teal", width=1),  # White for outline
            ),
            opacity=1,  # Adjust opacity as needed
        )
    )

    volume_fig.update_layout(
        title="Volume Bar Chart",
        xaxis_title="Date",
        yaxis_title="Volume",
        template="plotly_white",
    )

    st.plotly_chart(volume_fig)

    # Moving Average Plot
    st.subheader(f"{ticker} Moving Average Visualization")
    ma_fig = go.Figure()

    ma_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["close"],
            mode="lines",
            name="Close",
            line=dict(color="#ff7f50", width=2),
        )
    )
    ma_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Moving Average"],
            mode="lines",
            name="20-Day Moving Average",
            line=dict(color="#008080", width=2, dash="dash"),
        )
    )

    ma_fig.update_layout(
        title="Moving Average of Closing Price",
        xaxis_title="Date",
        yaxis_title="Price in USD ($)",
        template="plotly_white",
    )
    st.plotly_chart(ma_fig)

    # RSI Plot
    st.subheader(f"{ticker} RSI Visualization")
    rsi_fig = go.Figure()

    rsi_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["RSI"],
            mode="lines",
            name="RSI",
            line=dict(color="#C71585", width=2),
        )
    )  # Different color for RSI
    rsi_fig.add_hline(
        y=70,
        line_dash="dash",
        line_color="#39FF14",
        annotation_text="Overbought (70)",
        annotation_position="top right",
    )
    rsi_fig.add_hline(
        y=30,
        line_dash="dash",
        line_color="yellow",
        annotation_text="Oversold (30)",
        annotation_position="bottom right",
    )

    rsi_fig.update_layout(
        title="Relative Strength Index (RSI)",
        xaxis_title="Date",
        yaxis_title="RSI",
        yaxis_range=[0, 100],
        template="plotly_white",
    )
    st.plotly_chart(rsi_fig)

    # Display information about each plot
    st.write("### Description of Each Plot:")
    st.write(
        "1. **Price Visualization:** Displays the Open, High, Low, and Close prices over time."
    )
    st.write(
        "2. **Volume Visualization:** Shows the trading volume over time as a bar chart."
    )
    st.write(
        "3. **Moving Average Visualization:** Illustrates the 20-day moving average alongside the closing price to smooth out price fluctuations."
    )
    st.write(
        "4. **RSI Visualization:** The RSI is calculated to identify overbought (>70) and oversold (<30) conditions in the stock."
    )


# Function to Display Model Performance
def display_numerical_model_performance():
    # HTML content
    html_content = """
    <h5>Regression Model Performance Overview</h5>
    <p class="description">This table presents the performance of various regression models for different companies. We have utilized an ensemble model approach to enhance prediction accuracy.</p>

    <table>
        <tr>
            <th>Company</th>
            <th>Linear Regression</th>
            <th>Ridge Regression</th>
            <th>Lasso Regression</th>
            <th>Elastic Net Regression</th>
        </tr>
        <tr>
            <td>Apple (AAPL)</td>
            <td>0.9998629224782566</td>
            <td>0.9998630076573156</td>
            <td>0.9993577928176817</td>
            <td>0.9996487306800625</td>
        </tr>
        <tr>
            <td>Amazon (AMZN)</td>
            <td>0.999084553005321</td>
            <td>0.9961820949085249</td>
            <td>0.9961820949085249</td>
            <td>0.9965084504390407</td>
        </tr>
        <tr>
            <td>Google (GOOG)</td>
            <td>0.9992315300913325</td>
            <td>0.9992317269769614</td>
            <td>0.9973035403402394</td>
            <td>0.9973876081990091</td>
        </tr>
        <tr>
            <td>Microsoft (MSFT)</td>
            <td>0.9992315300913325</td>
            <td>0.9998440164467663</td>
            <td>0.9993642265769165</td>
            <td>0.9994838523467628</td>
        </tr>
        <tr>
            <td>Meta (META)</td>
            <td>0.9992315300913325</td>
            <td>0.9992317269769614</td>
            <td>0.9973035403402394</td>
            <td>0.9973876081990091</td>
        </tr>
        <tr>
            <td>Netflix (NFLX)</td>
            <td>0.9992198305734726</td>
            <td>0.9992198288782033</td>
            <td>0.9971600744221598</td>
            <td>0.9971700356054888</td>
        </tr>
        <tr>
            <td>NVIDIA (NVDA)</td>
            <td>0.9971063606802831</td>
            <td>0.998365397592374</td>
            <td>0.9940339650281499</td>
            <td>0.9972701576306695</td>
        </tr>
        <tr>
            <td>Tata Consultancy Services (TCS)</td>
            <td>0.9979612118835919</td>
            <td>0.9979612934362246</td>
            <td>0.9890586523727406</td>
            <td>0.9891227853737217</td>
        </tr>
    </table>
    """

    # Display the HTML content
    st.markdown(html_content, unsafe_allow_html=True)


# Function to display visualizations for the selected ticker, including actual vs. predicted prices
def display_numerical_model_visualization(ticker):
    # Define the dataset and model paths
    dataset_path = os.path.join(DATASET_DIR, f"Preprocessed_{ticker}_Dataset.csv")
    model_path = os.path.join(
        DATASET_DIR_1, "Models", "pkl_models", f"{ticker}_Ensemble_Model.pkl"
    )

    # Check if the dataset file exists
    if not os.path.isfile(dataset_path):
        st.error(f"No dataset found for ticker symbol: {ticker}")
        return

    # Load the dataset
    df = pd.read_csv(dataset_path, index_col="date", parse_dates=True)

    # Load the model if available
    if not os.path.isfile(model_path):
        st.error(f"No model found for ticker symbol: {ticker}")
        return

    with open(model_path, "rb") as file:
        model = pickle.load(file)

    # Predict the closing prices
    df["Predicted Close"] = model.predict(
        df.drop(columns=["close"])
    )  # Relevant features are present

    # Calculate Moving Average
    df["Moving Average"] = df["Predicted Close"].rolling(window=20).mean()

    # Calculate RSI
    delta = df["Predicted Close"].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df["RSI"] = 100 - (100 / (1 + rs))

    # Create the line graph for Actual and Predicted Prices
    st.subheader(f"{ticker} Price Visualization")
    price_fig = go.Figure()

    price_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Predicted Close"],
            mode="lines",
            name="Predicted Close",
            line=dict(color="green", width=2, dash="dash"),
        )
    )
    price_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["open"],
            mode="lines",
            name="Open",
            line=dict(color="#fade2a", width=2, dash="dash"),
        )
    )
    price_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["high"],
            mode="lines",
            name="High",
            line=dict(color="#f2495c", width=2, dash="dash"),
        )
    )
    price_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["low"],
            mode="lines",
            name="Low",
            line=dict(color="#5794f2", width=2, dash="dash"),
        )
    )
    price_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["close"],
            mode="lines",
            name="Actual Close",
            line=dict(color="#B877D9", width=4),
            opacity=0.5,
        )
    )

    price_fig.update_layout(
        title="Stock Price Visualization",
        xaxis_title="Date",
        yaxis_title="Price in USD ($)",
        template="plotly_white",
    )
    st.plotly_chart(price_fig)

    # Predicted vs. Actual Price Plot
    st.subheader(f"{ticker} Actual vs Predicted Price Visualization")
    prediction_fig = go.Figure()

    prediction_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["close"],
            mode="lines",
            name="Actual Close",
            line=dict(color="green", width=2),
        )
    )
    prediction_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Predicted Close"],
            mode="lines",
            name="Predicted Close",
            line=dict(color="red", width=2, dash="dash"),
        )
    )

    prediction_fig.update_layout(
        title="Actual vs Predicted Closing Price",
        xaxis_title="Date",
        yaxis_title="Price in USD ($)",
        template="plotly_white",
    )
    st.plotly_chart(prediction_fig)

    # Bar chart for Volume
    st.subheader(f"{ticker} Volume Visualization")

    volume_fig = go.Figure()
    volume_fig.add_trace(
        go.Bar(
            x=df.index,
            y=df["volume"],
            marker=dict(
                color="teal",  # Set bar color
                line=dict(color="teal", width=1),  # Outline color
            ),
            opacity=1,
        )
    )

    volume_fig.update_layout(
        title="Volume Bar Chart",
        xaxis_title="Date",
        yaxis_title="Volume",
        template="plotly_white",
    )

    st.plotly_chart(volume_fig)

    # Moving Average Plot
    st.subheader(f"{ticker} Moving Average Visualization")
    ma_fig = go.Figure()

    ma_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Predicted Close"],
            mode="lines",
            name="Predicted Close",
            line=dict(color="#ff7f50", width=2),
        )
    )
    ma_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Moving Average"],
            mode="lines",
            name="20-Day Moving Average",
            line=dict(color="#008080", width=2, dash="dash"),
        )
    )

    ma_fig.update_layout(
        title="Moving Average of Closing Price",
        xaxis_title="Date",
        yaxis_title="Price in USD ($)",
        template="plotly_white",
    )
    st.plotly_chart(ma_fig)

    # RSI Plot
    st.subheader(f"{ticker} RSI Visualization")
    rsi_fig = go.Figure()

    rsi_fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["RSI"],
            mode="lines",
            name="RSI",
            line=dict(color="#C71585", width=2),
        )
    )
    rsi_fig.add_hline(
        y=70,
        line_dash="dash",
        line_color="#39FF14",
        annotation_text="Overbought (70)",
        annotation_position="top right",
    )
    rsi_fig.add_hline(
        y=30,
        line_dash="dash",
        line_color="yellow",
        annotation_text="Oversold (30)",
        annotation_position="bottom right",
    )

    rsi_fig.update_layout(
        title="Relative Strength Index (RSI)",
        xaxis_title="Date",
        yaxis_title="RSI",
        yaxis_range=[0, 100],
        template="plotly_white",
    )
    st.plotly_chart(rsi_fig)

    # Display information about each plot
    st.write("### Description of Each Plot:")
    st.write(
        "1. **Price Visualization:** Displays the Open, High, Low, and Actual vs. Predicted Close prices over time."
    )
    st.write(
        "2. **Actual vs Predicted Price Visualization:** Compares the model's predicted closing prices with the actual closing prices."
    )
    st.write(
        "3. **Volume Visualization:** Shows the trading volume over time as a bar chart."
    )
    st.write(
        "4. **Moving Average Visualization:** Illustrates the 20-day moving average alongside the closing price to smooth out price fluctuations."
    )
    st.write(
        "5. **RSI Visualization:** The RSI is calculated to identify overbought (>70) and oversold (<30) conditions in the stock."
    )


# Directory containing the preprocessed datasets
DATASET_DIR_1 = "Codes/Historical_Data_Analysis"


# Define the function for displaying the model prediction
def display_numerical_model_predicted(ticker, open_price, high, low, volume):
    # Define dataset and model paths
    dataset_path = os.path.join(DATASET_DIR, f"Preprocessed_{ticker}_Dataset.csv")
    model_path = os.path.join(
        DATASET_DIR_1, "Models", "pkl_models", f"{ticker}_Ensemble_Model.pkl"
    )

    # Check if the dataset file exists
    if not os.path.isfile(dataset_path):
        st.error(f"No dataset found for ticker symbol: {ticker}")
        return

    # Load the dataset
    df = pd.read_csv(dataset_path, index_col="date", parse_dates=True)

    # Check if the model file exists
    if not os.path.isfile(model_path):
        st.error(f"No model found for ticker symbol: {ticker}")
        return

    # Load the model
    with open(model_path, "rb") as file:
        model = pickle.load(file)

    # Create a new DataFrame for the input values to predict
    input_data = pd.DataFrame(
        {"open": [open_price], "high": [high], "low": [low], "volume": [volume]}
    )

    # Predict the closing price for the given input values
    predicted_close = model.predict(input_data)[
        0
    ]  # Take the first (and only) prediction

    # Display the prediction
    st.write(f"### Predicted Closing Price for {ticker}: ${predicted_close:.2f}")


# Function to Display Model Performance
def display_text_model_performance():
    # Basic HTML table without additional styling
    html_content = """
    <h5>Regression Model Performance Overview</h5>
    <p>This table presents the performance of various regression models for different companies.</p>

    <table border="1">
    <thead>
        <tr>
        <th>Metric</th>
        <th>Logistic Regression</th>
        <th>Naive Bayes</th>
        <th>Random Forest</th>
        </tr>
    </thead>
    <tbody>
        <td>Accuracy</td>
        <td>0.6516</td>
        <td>0.6672</td>
        <td>0.9900</td>
        </tr>
        <!-- Class 0 -->
        <tr>
        <td>Class 0 Precision</td>
        <td>0.62</td>
        <td>0.65</td>
        <td>0.99</td>
        </tr>
        <tr>
        <td>Class 0 Recall</td>
        <td>0.82</td>
        <td>0.77</td>
        <td>1.00</td>
        </tr>
        <tr>
        <td>Class 0 F1-Score</td>
        <td>0.71</td>
        <td>0.70</td>
        <td>0.99</td>
        </tr>
        <tr>
        <td>Class 0 Support</td>
        <td>2395</td>
        <td>2395</td>
        <td>2395</td>
        </tr>
        <!-- Class 1 -->
        <tr>
        <td>Class 1 Precision</td>
        <td>0.72</td>
        <td>0.70</td>
        <td>1.00</td>
        </tr>
        <tr>
        <td>Class 1 Recall</td>
        <td>0.48</td>
        <td>0.56</td>
        <td>0.98</td>
        </tr>
        <tr>
        <td>Class 1 F1-Score</td>
        <td>0.57</td>
        <td>0.62</td>
        <td>0.99</td>
        </tr>
        <tr>
        <td>Class 1 Support</td>
        <td>2304</td>
        <td>2304</td>
        <td>2304</td>
        </tr>
        <!-- Overall Metrics -->
        <tr>
        <td>Macro Avg Precision</td>
        <td>0.67</td>
        <td>0.67</td>
        <td>0.99</td>
        </tr>
        <tr>
        <td>Macro Avg Recall</td>
        <td>0.65</td>
        <td>0.67</td>
        <td>0.99</td>
        </tr>
        <tr>
        <td>Macro Avg F1-Score</td>
        <td>0.64</td>
        <td>0.66</td>
        <td>0.99</td>
        </tr>
        <tr>
        <td>Weighted Avg Precision</td>
        <td>0.67</td>
        <td>0.67</td>
        <td>0.99</td>
        </tr>
        <tr>
        <td>Weighted Avg Recall</td>
        <td>0.65</td>
        <td>0.67</td>
        <td>0.99</td>
        </tr>
        <tr>
        <td>Weighted Avg F1-Score</td>
        <td>0.64</td>
        <td>0.66</td>
        <td>0.99</td>
        </tr>
        <tr>
        <td>Total Support</td>
        <td>4699</td>
        <td>4699</td>
        <td>4699</td>
        </tr>
    </tbody>
    </table>

    """

    # Display the HTML content
    st.markdown(html_content, unsafe_allow_html=True)


# Function to display the Text Model Visualization section
def display_text_model_visualization():
    st.markdown(
        """
        <h3 style="text-align:center;">Text Model Visualization Overview</h3>
        <div style="font-size:18px; text-align:center;">
            Our text model visualization highlights the detailed outputs and predictions using interactive charts and plots.
        </div>
        <br>
        <h4 style="text-align:center;">Functionality of the Text Model Visualization</h4>
        <div style="font-size:16px; text-align:justify;">
            The section demonstrates how text-based prediction models, such as those for sentiment analysis or topic classification, visualize 
            their results. Users can select different models to visualize text data, analyze results, and explore comparative insights through 
            various interactive plots and metrics.
            <br><br>
            Below is a conceptual visualization of how the text model operates and displays outputs.
        </div>
        <br>
        
        <h4 style="text-align:center;">Snapshots from the Model Visualization</h4>
        
        <!-- Image 1 -->
        <div style="text-align:center;">
            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis\Textual_Analysis\Transparent_Plots\Most_Frequent_Words_in_News_Articles.png" width="100%" alt="Model Visualization Snapshot 1" title="Model Visualization Snapshot 1" />
            <br><br>
        </div>

        <!-- Image 2 -->
        <div style="text-align:center;">
            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis\Textual_Analysis\Plots\Target_Variable_Distribution.png" width="100%" alt="Model Visualization Snapshot 2" title="Model Visualization Snapshot 2" />
            <br><br>
        </div>
        
        <!-- Image 3 -->
        <div style="text-align:center;">
            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis\Textual_Analysis\Plots\Pie_Chart_Target_Variable_Distribution.png" width="100%" alt="Model Visualization Snapshot 2" title="Model Visualization Snapshot 2" />
            <br><br>
        </div>

        <!-- Image 4 -->
        <div style="text-align:center;">
            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis\Textual_Analysis\Plots\Top_20_Important_Features_(TF-IDF_Terms).png" width="100%" alt="Model Visualization Snapshot 3" title="Model Visualization Snapshot 3" />
            <br><br>
        </div>
        
        """,
        unsafe_allow_html=True,
    )


# Function to predict and display the text model prediction
def display_text_model_prediction():
    # File paths for the dataset and model
    csv_path = os.path.join(
        "Codes",
        "Historical_Data_Analysis",
        "Textual_Analysis",
        "Dataset",
        "Preprocessed_Text_Dataset.csv",
    )
    model_path = os.path.join(
        "Codes",
        "Historical_Data_Analysis",
        "Textual_Analysis",
        "Models",
        "Classification",
        "pkl_models",
        "Random_Forest_Best_Model.pkl",
    )

    # Step 1: Load the preprocessed dataset
    try:
        data = pd.read_csv(csv_path)
        st.write("Dataset loaded successfully.")
    except FileNotFoundError:
        st.error("Dataset file not found at the specified path.")
        return

    # Step 2: Load the pre-trained model
    try:
        with open(model_path, "rb") as file:
            model = pickle.load(file)
        # st.write("Model loaded successfully.")
    except FileNotFoundError:
        # st.error("Model file not found at the specified path.")
        return

    # Step 3: Vectorize the cleaned text data using TF-IDF

    vectorizer = TfidfVectorizer(max_features=5000)
    X_transformed = vectorizer.fit_transform(data["cleaned_text"]).toarray()

    # Step 4: Streamlit input for user text
    user_input = st.text_input(
        "Enter the text to predict the stock movement (0: Down, 1: Up):"
    )

    if user_input:
        # Step 5: Transform user input using the same vectorizer
        user_input_transformed = vectorizer.transform([user_input]).toarray()

        # Step 6: Use the model to predict the user input
        prediction = model.predict(user_input_transformed)

        # Step 7: Display prediction
        if prediction[0] == 1:
            st.success("The model predicts: Up (1)")
        else:
            st.error(
                "The model predicts: Down (0)"
            )  # Use st.warning() for a yellow background


# Function to Display Model Performance
def display_hybrid_model_performance():
    # Basic HTML table without additional styling
    html_content = """
    <h5>Regression Model Performance Overview</h5>
    <p>This table presents the performance of various regression models for different companies.</p>

    <table border="1">
    <thead>
        <tr>
        <th>Model</th>
        <th>MAE</th>
        <th>MSE</th>
        <th>RMSE</th>
        <th>R² Score</th>
        <th>Accuracy (%)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
        <td>MLP</td>
        <td>4.631412</td>
        <td>30.276025</td>
        <td>5.502365</td>
        <td>0.583915</td>
        <td>99.863574</td>
        </tr>
        <tr>
        <td>Linear Regression</td>
        <td>5.725293</td>
        <td>39.196283</td>
        <td>6.260694</td>
        <td>0.461323</td>
        <td>100.000000</td>
        </tr>
        <tr>
        <td>K-Nearest Neighbors (KNN)</td>
        <td>5.575181</td>
        <td>41.867105</td>
        <td>6.470479</td>
        <td>0.424618</td>
        <td>100.000000</td>
        </tr>
        <tr>
        <td>SVM</td>
        <td>5.771079</td>
        <td>47.432490</td>
        <td>6.887125</td>
        <td>0.348132</td>
        <td>99.454297</td>
        </tr>
        <tr>
        <td>Gradient Boosting</td>
        <td>6.189361</td>
        <td>52.197185</td>
        <td>7.224762</td>
        <td>0.282651</td>
        <td>100.000000</td>
        </tr>
        <tr>
        <td>Random Forest</td>
        <td>6.378920</td>
        <td>60.091005</td>
        <td>7.751839</td>
        <td>0.174165</td>
        <td>100.000000</td>
        </tr>
        <tr>
        <td>Decision Tree</td>
        <td>6.405307</td>
        <td>61.140660</td>
        <td>7.819249</td>
        <td>0.159740</td>
        <td>100.000000</td>
        </tr>
        <tr>
        <td>AdaBoost</td>
        <td>7.360769</td>
        <td>77.328544</td>
        <td>8.793665</td>
        <td>-0.062731</td>
        <td>100.000000</td>
        </tr>
    </tbody>
    </table>

    """

    # Display the HTML content
    st.markdown(html_content, unsafe_allow_html=True)


# Function to display the Text Model Visualization section
def display_hybrid_model_visualization():
    st.markdown(
        """
        <h3 style="text-align:center;">Text Model Visualization Overview</h3>
        <div style="font-size:18px; text-align:center;">
            Our hybrid model visualization highlights the detailed outputs and predictions using interactive charts and plots.
        </div>
        <br>
        <h4 style="text-align:center;">Functionality of the Text Model Visualization</h4>
        <div style="font-size:16px; text-align:justify;">
            The section demonstrates how text-based prediction models, such as those for sentiment analysis or topic classification, visualize 
            their results. Users can select different models to visualize text data, analyze results, and explore comparative insights through 
            various interactive plots and metrics.
            <br><br>
            Below is a conceptual visualization of how the text model operates and displays outputs.
        </div>
        <br>
        
        <h4 style="text-align:center;">Snapshots from the Model Visualization</h4>
        
        <!-- Image 1 -->
        <div style="text-align:center;">
            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis\Hybrid_Model\Plots\Comparison_Linear_Regression.png" width="100%" alt="Model Visualization Snapshot 1" title="Model Visualization Snapshot 1" />
            <br><br>
        </div>

        <!-- Image 2 -->
        <div style="text-align:center;">
            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis\Hybrid_Model\Plots\Comparison_of_Model_Accuracy.png" width="100%" alt="Model Visualization Snapshot 2" title="Model Visualization Snapshot 2" />
            <br><br>
        </div>
        
        <!-- Image 3 -->
        <div style="text-align:center;">
            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis\Hybrid_Model\Plots\Comparison_of_Regression_Models_MAE_R2_filtered.png" width="100%" alt="Model Visualization Snapshot 2" title="Model Visualization Snapshot 2" />
            <br><br>
        </div>
        
        """,
        unsafe_allow_html=True,
    )


# Function to predict and display the stock price based on user input
def display_hybrid_model_prediction():
    # File path for the pre-trained model
    model_path = os.path.join(
        "Codes",
        "Historical_Data_Analysis",
        "Hybrid_Model",
        "Models",
        "Combined",
        "pkl_models",
        "MLP_Model.pkl",
    )

    # Step 1: Load the pre-trained model
    try:
        with open(model_path, "rb") as file:
            model = pickle.load(file)
        st.write("Model loaded successfully.")
    except FileNotFoundError:
        st.error("Model file not found at the specified path.")
        return

    # Step 2: Streamlit inputs for user data
    dia_close = st.number_input(
        "Enter the DIA close value:", min_value=0.0, format="%.2f"
    )
    qqq_close = st.number_input(
        "Enter the QQQ close value:", min_value=0.0, format="%.2f"
    )
    user_input_text = st.text_input(
        "Enter the news text to calculate sentiment and predict stock price:"
    )

    if user_input_text:
        # Step 3: Calculate sentiment score of the input text
        sentiment_score = TextBlob(user_input_text).sentiment.polarity
        st.write(f"Calculated sentiment score: {sentiment_score:.2f}")

        # Step 4: Combine all inputs into a single DataFrame for model prediction
        final_input = pd.DataFrame(
            {
                "DIA_Close": [dia_close],
                "QQQ_Close": [qqq_close],
                "Sentiment_Score": [sentiment_score],
            }
        )

        # Step 5: Predict using the model
        predicted_price = model.predict(final_input)[0]

        # Step 6: Display prediction with $ symbol
        st.success(f"The model predicts the stock price: ${predicted_price:.2f}")


# Function to display the InfluxDB Database section
def display_project_database():
    st.markdown(
        """
        <h3 style="text-align:center;">Project Database Overview</h3>
        <div style="font-size:18px; text-align:center;">
            We are using InfluxDB Database for efficient data storage and management.
        </div>
        <br>
        <h4 style="text-align:center;">InfluxDB Database</h4>
        <div style="font-size:16px; text-align:justify;">
            InfluxDB is a powerful time-series database optimized for storing and querying both historical and real-time data, 
            particularly in high-volume environments. It offers exceptional performance for managing time-stamped data, making it 
            an ideal choice for our project.
            <br><br>
        </div>
        <div style="text-align:center;">
            <img src="https://dashboard.snapcraft.io/site_media/appmedia/2020/07/influxdata-logo--symbol--pool-alpha-small_eSQhzYC.png"
                width="150" title = "InfluxDB Logo" alt="InfluxDB Logo" />
            <br><br>
        </div>
        <h4 style="text-align:center;">InfluxDB Architecture</h4>
        <div style="font-size:16px; text-align:justify;">
            The InfluxDB architecture utilizes a bucket system, which is pivotal for organizing data. In our project, we have a 
            primary bucket named <b>Stock Price</b>. Within this bucket, measurements help categorize and store data efficiently. 
            The first measurement is <b>stock_price</b>, which includes data points such as open, high, low, close, RSI (Relative 
            Strength Index), volume, and moving average, all indexed by time.
            <br><br>
            Another key measurement is <b>model_prediction</b>, containing values such as predicted high, low, open, volume, 
            predicted close, predicted moving average, and predicted RSI.
            <br><br>
            Both measurements include a <b>Ticker</b> column that holds the company ticker symbol, covering a total of eight 
            companies: AAPL, AMZN, MSFT, NVDA, NFLX, META, TCS, and GOOG.
            <br><br>
            Initially, data is stored in InfluxDB, then queried and visualized using Grafana. The dashboard in Grafana is built on 
            top of this architecture, allowing dynamic data visualization. The diagram below depicts the general architecture of 
            InfluxDB.
            <br><br>
        </div>
        
        <div style="text-align:center;">
            <img src="https://wiki.onosproject.org/download/attachments/8423670/influxdb_arch.png?version=1&modificationDate=1459547041415&api=v2"
                width="400" title="InfluxDB Architecture" alt="InfluxDB Architecture" />
        </div>
        <br><br>
        
        <div style="text-align:center;">
            <h4> Database Overview</h4>
            <p> This section displays database snapshots from the project, organized by categories.</p>
        </div>
        <br>

        <!-- Section 1: Numerical Analysis -->
        <h5 style="text-align:center;">1. Numerical Analysis</h5>
        <div style="font-size:16px; text-align:justify;">
            This section displays numerical data from the stock market, including graphs for open, high, low, and close prices. It also features volume bar plots, RSI, and moving averages.
            <br><br>
        </div>
        <div style="text-align:center;">
            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/InfluxDB_Database/Numerical_Analysis_1.png" width="100%" alt="Numerical Analysis Snapshot" title="Numerical Analysis Snapshot" />
            <br><br>
        </div>

        <!-- Section 2: Model Prediction -->
        <h5 style="text-align:center;">2. Model Prediction</h5>
        <div style="font-size:16px; text-align:justify;">
            This section displays the model predictions, comparing predicted and actual values for stock prices, RSI, and moving averages.
            <br><br>
        </div>
        <div style="text-align:center;">
            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/InfluxDB_Database/Model_Prediction_1.png" width="100%" alt="Model Prediction Snapshot" title="Model Prediction Snapshot" />
            <br><br>
        </div>

        <!-- Section 3: Textual Analysis -->
        <h5 style="text-align:center;">3. Textual Analysis</h5>
        <div style="font-size:16px; text-align:justify;">
            This section visualizes sentiment analysis from news headlines, including positive, negative, and neutral sentiment scores.
            <br><br>
        </div>
        <div style="text-align:center;">
            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/InfluxDB_Database/Textual_Analysis_1.png" width="100%" alt="Textual Analysis Snapshot" title="Textual Analysis Snapshot" />
            <br><br>
        </div>

        <!-- Section 4: Hybrid Model -->
        <h5 style="text-align:center;">4. Hybrid Model</h5>
        <div style="font-size:16px; text-align:justify;">
            The hybrid model combines numerical and textual data to provide a more comprehensive analysis of stock prices.
            <br><br>
        </div>
        <div style="text-align:center;">
            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/InfluxDB_Database/Hybrid_Model_1.png" width="100%" alt="Hybrid Model Snapshot" title="Hybrid Model Snapshot" />
        </div>


        """,
        unsafe_allow_html=True,
    )


# Function to display the Grafana Dashboard sections
def display_project_dashboard():

    st.markdown(
        """
        <h3 style="text-align:center;">Project Dashboard Overview</h3>
        <div style="font-size:18px; text-align:center;">
            We are using Grafana for efficient data querying and visualization.
        </div>
        <br>
        <div style="text-align:center;">
        <h4>Grafana Dashboard</h4>
        <p>The Grafana dashboard provides an interactive and dynamic interface for real-time data visualization and analysis.</p>
          <img src="https://creazilla-store.fra1.digitaloceanspaces.com/icons/3253859/grafana-icon-md.png" width="150" title = "Grafana Logo" alt="Grafana Logo" />
         <h4>Dashboard Overview</h4>
         <p> This section displays dashboard snapshots from the project, organized by categories.</p>
         <br>
         <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Overview/Dashboard_1.png" width="100%" alt="Stock Market Overview Snapshot 1" title="Stock Market Overview Snapshot 1" />
        <br><br>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Section 1: Stock Market and Project Dashboard Overview
    st.markdown(
        """
        <h5 style = "text-align:center">1. Stock Market and Project Dashboard Overview</h5>
        <p>
        This section provides an overview of the stock market, project details, and descriptions of the companies used in the project, 
        including MAANG, Nvidia, Microsoft, and TCS.
        </p>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Stock_Market_and_Project_Dashboard_Overview/Dashboard_1.png" width="100%" alt="Stock Market Overview Snapshot 1" title="Stock Market Overview Snapshot 1" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Stock_Market_and_Project_Dashboard_Overview/Dashboard_Panel_Dashboard_Description_and_Datasets_Information_View_1.png" width="100%" alt="Stock Market Overview Snapshot 2" title="Stock Market Overview Snapshot 2" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Stock_Market_and_Project_Dashboard_Overview/Dashboard_Panel_Dashboard_Description_and_Datasets_Information_View_2.png" width="100%" alt="Stock Market Overview Snapshot 3" title="Stock Market Overview Snapshot 3" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Stock_Market_and_Project_Dashboard_Overview/Dashboard_Panel_Stock_Market_View_1.png" width="100%" alt="Stock Market Overview Snapshot 4" title="Stock Market Overview Snapshot 4" />
        <br><br>
        """,
        unsafe_allow_html=True,
    )

    # Section 2: Numerical Analysis
    st.markdown(
        """
        <h5 style = "text-align:center">2. Numerical Analysis</h5>
        <p>
        This section displays numerical data of the stock market, featuring graphs of open, high, low, and close prices 
        along with volume bar plots, RSI, and moving averages.
        </p>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Numerical_Analysis/Dashboard_1.png" width="100%" alt="Numerical Analysis Snapshot 1" title="Numerical Analysis Snapshot 1" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Numerical_Analysis/Dashboard_2.png" width="100%" alt="Numerical Analysis Snapshot 2" title="Numerical Analysis Snapshot 2" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Numerical_Analysis/Dashboard_3.png" width="100%" alt="Numerical Analysis Snapshot 3" title="Numerical Analysis Snapshot 3" />
        <br><br>
        """,
        unsafe_allow_html=True,
    )

    # Section 3: Model Prediction
    st.markdown(
        """
        <h5 style = "text-align:center">3. Model Prediction</h5>
        <p>
        This section highlights model predictions, including individual and comparative graphs of predicted and actual values 
        for stock prices, as well as predicted RSI and moving averages.
        </p>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Model_Prediction/Dashboard_1.png" width="100%" alt="Model Prediction Snapshot 1" title="Model Prediction Snapshot 1" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Model_Prediction/Dashboard_2.png" width="100%" alt="Model Prediction Snapshot 2" title="Model Prediction Snapshot 2" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Model_Prediction/Dashboard_Panel_Model_Evaluation_View.png" width="100%" alt="Model Prediction Snapshot 3" title="Model Prediction Snapshot 3" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Model_Prediction/Dashboard_3.png" width="100%" alt="Model Prediction Snapshot 3" title="Model Prediction Snapshot 3" />
        <br><br>
        """,
        unsafe_allow_html=True,
    )

    # Section 4: Textual Analysis
    st.markdown(
        """
        <h5 style = "text-align:center">4. Textual Analysis</h5>
        <p>
        This section visualizes sentiment analysis from news headlines, showcasing positive, negative, and neutral sentiment scores.
        </p>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Textual_Analysis/Dashboard_1.png" width="100%" alt="Textual Analysis Snapshot 1" title="Textual Analysis Snapshot 1" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Textual_Analysis/Dashboard_2.png" width="100%" alt="Textual Analysis Snapshot 2" title="Textual Analysis Snapshot 2" />
        <br><br>
        """,
        unsafe_allow_html=True,
    )

    # Section 5: Hybrid Model
    st.markdown(
        """
        <h5 style = "text-align:center">5. Hybrid Model</h5>
        <p>
        The hybrid model combines numerical and textual data for a comprehensive analysis.
        </p>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Hybrid_Model/Dashboard_1.png" width="100%" alt="Hybrid Model Snapshot 1" title="Hybrid Model Snapshot 1" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Hybrid_Model/Dashboard_2.png" width="100%" alt="Hybrid Model Snapshot 2" title="Hybrid Model Snapshot 2" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Hybrid_Model/Dashboard_3.png" width="100%" alt="Hybrid Model Snapshot 3" title="Hybrid Model Snapshot 3" />
        <br><br>
        <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Hybrid_Model/Dashboard_4.png" width="100%" alt="Hybrid Model Snapshot 4" title="Hybrid Model Snapshot 4" />
        <br><br>
        """,
        unsafe_allow_html=True,
    )


# Function to display the Flask App section
def display_project_flask_app():
    st.markdown(
        """
        <h3 style="text-align:center;">Flask App Overview</h3>
        <div style="font-size:18px; text-align:center;">
            Our Flask app is designed with a pastel lavender pink theme for a visually soothing user interface.
        </div>
        <br>
        <h4 style="text-align:center;">Flask App Functionality</h4>
        <div style="font-size:16px; text-align:justify;">
            The Flask application loads pre-trained models for each company, with separate models created to forecast stock prices. 
            Users can select a company from a dropdown menu, and the app fetches the appropriate model for predictions. The app 
            takes input data for open, high, low, and volume prices and displays the predicted close value.
            <br><br>
            Below is a visual representation of the Flask app's architecture.
        </div>
        <br>
        
        <!-- Image for Flask App Logo -->
        <div style="text-align:center;">
            <img src="https://www.seekpng.com/png/full/875-8753366_flask-png.png" width="150" title="Flask Logo" alt="Flask Logo" />
            <br><br>
        </div>
        
        <!-- Image for Flask App Architecture -->
        <div style="text-align:center;">
            <img src="https://th.bing.com/th/id/OIP.zUyMlO4bXyV_GNy3XcFubgHaEC?rs=1&pid=ImgDetMain" width="400" title="Flask App Architecture" alt="Flask App Architecture" />
            <br><br>
        </div>
        
        <h4 style="text-align:center;">Snapshots from the Flask App</h4>
        
        <!-- Image 1 -->
        <div style="text-align:center;">
            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/App_Snapshots/Flask_App/App_View_1.png" width="100%" alt="Flask App Snapshot 1" title="Flask App Snapshot 1" />
            <br><br>
        </div>

        <!-- Image 2 -->
        <div style="text-align:center;">
            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/App_Snapshots/Flask_App/App_View_2.png" width="100%" alt="Flask App Snapshot 2" title="Flask App Snapshot 2" />
            <br><br>
        </div>

        <!-- Image 3 -->
        <div style="text-align:center;">
            <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/App_Snapshots/Flask_App/App_View_3.png" width="100%" alt="Flask App Snapshot 3" title="Flask App Snapshot 3" />
            <br><br>
        </div>
        
        """,
        unsafe_allow_html=True,
    )


# Function to display team members' contact information in a column-wise format
def display_contact_information():

    # Define team member information as separate rows with transposed details
    team_members = [
        {
            "Name": "Madhurima Rawat",
            "Role": "Project Planner & Developer",
            "Responsibilities": "Project planning, managing GitHub repository, code documentation, setting up InfluxDB database, Grafana dashboard design, Streamlit deployment, Flask backend, styling and layout, data visualization and preprocessing of numerical data.",
            "Tools": "GitHub, InfluxDB, Grafana, Streamlit, Python, Flask, Pandas, Matplotlib, Plotly",
            "GitHub": '<a href="https://github.com/madhurimarawat" target="_blank">GitHub</a>',
            "LinkedIn": '<a href="https://www.linkedin.com/in/madhurima-rawat/" target="_blank">LinkedIn</a>',
            "Email": '<a href="mailto:rawtamadhurima@gmail.com" target="_blank">Email</a>',
        },
        {
            "Name": "Geetanshu Dev Meshram",
            "Role": "Data Analyst & Backend Developer",
            "Responsibilities": "Model building for numerical data, basic Flask app design.",
            "Tools": "Python, Flask, Machine Learning libraries",
            "GitHub": '<a href="https://github.com/geetanshudev" target="_blank">GitHub</a>',
            "LinkedIn": '<a href="https://www.linkedin.com/in/geetanshu-dev-meshram-2b3b61240/" target="_blank">LinkedIn</a>',
            "Email": '<a href="mailto:meshramgeetanshudev@gmail.com" target="_blank">Email</a>',
        },
        {
            "Name": "Sneha Jha",
            "Role": "Data Analyst",
            "Responsibilities": "Processing text data, model building, and hybrid model building.",
            "Tools": "NLP libraries, Machine Learning libraries, Hybrid Model Building",
            "GitHub": '<a href="https://github.com/Sneha100802" target="_blank">GitHub</a>',
            "LinkedIn": '<a href="https://www.linkedin.com/in/sneha-jha-808796261/" target="_blank">LinkedIn</a>',
            "Email": '<a href="mailto:jhasneha344@gmail.com" target="_blank">Email</a>',
        },
    ]

    # Display a brief summary of the team with names, LinkedIn profiles, and a description
    st.markdown("### Team Overview")
    st.markdown(
        "Our team consists of three passionate individuals who bring diverse skills to the table. "
        "We are focused on developing cutting-edge solutions in data analytics, backend development, and project management. "
        "Each team member plays a critical role in the success of the project, and we are excited to share our expertise and dedication."
    )

    # Explicitly written details for each team member with LinkedIn links
    st.markdown(
        "[Madhurima Rawat](https://www.linkedin.com/in/madhurima-rawat/) : &nbsp; Project Planner & Developer specialized in Project planning, managing GitHub repository, setting up InfluxDB database, Grafana dashboard design, Streamlit deployment, Flask styling and layout, data visualization and preprocessing of numerical data. Tools: GitHub, InfluxDB, Grafana, Streamlit, Python, Flask, Pandas, Matplotlib, Plotly"
    )
    st.markdown(
        "[Geetanshu Dev Meshram](https://www.linkedin.com/in/geetanshu-dev-meshram-2b3b61240/) :  &nbsp; Data Analyst & Backend Developer specialized in Model building for numerical data, basic Flask app design. Tools: Python, Flask, Machine Learning libraries"
    )
    st.markdown(
        "[Sneha Jha](https://www.linkedin.com/in/sneha-jha-808796261/) :  &nbsp; Data Analyst specialized in Processing text data, model building, and hybrid model building. Tools: NLP libraries, Hybrid Model Building"
    )

    st.markdown("---")

    # HTML Table with centered content and reduced width
    html_table = f"""
    <table style="width: 80%; border: 1px solid black; border-collapse: collapse; margin-left: auto; margin-right: auto;">
        <tr>
            <th style="padding: 8px; text-align: center;"><i class="fas fa-id-card"></i> &nbsp; Name</th>
            <th style="padding: 8px; text-align: center;">Madhurima Rawat</th>
            <th style="padding: 8px; text-align: center;">Geetanshu Dev Meshram</th>
            <th style="padding: 8px; text-align: center;">Sneha Jha</th>
        </tr>
        <tr>
            <td style="padding: 8px; text-align: center;"><i class="fas fa-user-tie"></i> &nbsp; <strong>Role</strong></td>
            <td style="padding: 8px; text-align: center;">{team_members[0]['Role']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[1]['Role']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[2]['Role']}</td>
        </tr>
        <tr>
            <td style="padding: 8px; text-align: center;"><i class="fas fa-tasks"></i> &nbsp; <strong>Responsibilities</strong></td>
            <td style="padding: 8px; text-align: center;">{team_members[0]['Responsibilities']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[1]['Responsibilities']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[2]['Responsibilities']}</td>
        </tr>
        <tr>
            <td style="padding: 8px; text-align: center;"><i class="fas fa-tools"></i> &nbsp; <strong>Tools</strong></td>
            <td style="padding: 8px; text-align: center;">{team_members[0]['Tools']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[1]['Tools']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[2]['Tools']}</td>
        </tr>
        <tr>
            <td style="padding: 8px; text-align: center;"><i class="fab fa-github"></i> &nbsp;<strong>GitHub</strong></td>
            <td style="padding: 8px; text-align: center;">{team_members[0]['GitHub']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[1]['GitHub']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[2]['GitHub']}</td>
        </tr>
        <tr>
            <td style="padding: 8px; text-align: center;"><i class="fab fa-linkedin"></i> &nbsp;<strong>LinkedIn</strong></td>
            <td style="padding: 8px; text-align: center;">{team_members[0]['LinkedIn']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[1]['LinkedIn']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[2]['LinkedIn']}</td>
        </tr>
        <tr>
            <td style="padding: 8px; text-align: center;"><i class="fas fa-envelope"></i> &nbsp;<strong>Email</strong></td>
            <td style="padding: 8px; text-align: center;">{team_members[0]['Email']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[1]['Email']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[2]['Email']}</td>
        </tr>
    </table>
    """

    # Render the table
    st.markdown(html_table, unsafe_allow_html=True)


# Function to display resources information
def display_resources_information():
    st.markdown("### Resources and Links")

    # Partial stock prices section
    st.markdown(
        """
        **Partial Stock Prices YAHOO Link:**
        - [Yahoo Finance](https://finance.yahoo.com/)

        **Textual and Hybrid Data:**
        - [Kaggle Dataset - News & Stock Prices](https://www.kaggle.com/datasets/kianso/news-stock-price)
        
        **Complete Stock Price Histories:**
        - [Alphabet/GOOG Stock](https://www.macrotrends.net/stocks/charts/GOOG/google/stock-price-history)
        - [AAPL Stock](https://www.macrotrends.net/stocks/charts/AAPL/apple/stock-price-history)
        - [AMZN Stock](https://www.macrotrends.net/stocks/charts/TCS/container-store/stock-price-history)
        - [META Stock](https://www.macrotrends.net/stocks/charts/META/meta-platforms/stock-price-history)
        - [MSFT Stock](https://www.macrotrends.net/stocks/charts/MSFT/microsoft/stock-price-history)
        - [NFLX Stock](https://www.macrotrends.net/stocks/charts/NFLX/netflix/stock-price-history)
        - [NVDA Stock](https://www.macrotrends.net/stocks/charts/NVDA/nvidia/stock-price-history)
        - [TCS Stock](https://www.macrotrends.net/stocks/charts/TCS/container-store/stock-price-history)

         **Illustration Links:**
        - [Project Resources (Illustration 1)](https://img.freepik.com/premium-vector/flat-design-stock-market-analysis_23-2148590818.jpg)
        - [Streamlit App Background Image (Illustration 2)](https://vectormine.b-cdn.net/wp-content/uploads/Stock_Market.jpg)
        """
    )


# Function to include background image and opacity
def display_background_image(url, opacity):
    """
    Displays a background image with a specified opacity on the web app using CSS.

    Args:
    - url (str): URL of the background image.
    - opacity (float): Opacity level of the background image.
    """
    # Set background image using HTML and CSS
    st.markdown(
        f"""
        <style>
            body {{
                background: url('{url}') no-repeat center center fixed;
                background-size: cover;
                opacity: {opacity};
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )


# Main function to handle the selection and display of sections
def main():
    """
    Main function that sets up the app's navigation, displays sections based on user selection,
    and includes links to the GitHub repository.
    """
    st.title("Stock Market Prediction")

    # Sidebar navigation for different sections
    st.sidebar.title("Explore")
    selected_section = st.sidebar.radio(
        "Go to",
        [
            "Stock Market Description",
            "Project Description",
            "Companies",
            "Numerical Dataset Information",
            "Numerical Dataset Visualization",
            "Numerical Model Evaluation",
            "Numerical Model Visualization",
            "Numerical Model Prediction",
            "Text Model Evaluation",
            "Text Model Visualization",
            "Text Model Prediction",
            "Hybrid Model Evaluation",
            "Hybrid Model Visualization",
            "Hybrid Model Prediction",
            "InfluxDB Database",
            "Grafana Dashboard",
            "Flask App",
            "Meet the Team",
            "Resources",
        ],
    )

    # Include Font Awesome CSS for icons
    st.sidebar.markdown(
        """
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
        <div class="sidebar-content">
            <h1><a href="https://github.com/madhurimarawat/Stock-Market-Prediction" target="_blank">
                    <i class="fab fa-github"></i> &nbsp; Visit Repository
                </a></h1>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Call respective functions based on the selected section
    if selected_section == "Stock Market Description":
        """
        Provides an introduction and overview of the stock market,
        covering key concepts and market behaviors.
        """
        display_stock_market_description()

    elif selected_section == "Project Description":
        """
        Gives a concise description of the project objectives,
        methodology, and expected outcomes.
        """
        display_project_description()

    elif selected_section == "Companies":
        """
        Displays a table containing company data, such as stock prices and financial metrics,
        allowing users to compare different companies.
        """
        display_company_data_table()

    elif selected_section == "Numerical Dataset Information":
        """
        Displays detailed dataset information for the selected ticker symbol.
        Users can explore the dataset using a sidebar dropdown.
        """
        ticker_symbol = st.sidebar.selectbox(
            "Select Dataset (Ticker Symbol)",
            ["AAPL", "GOOG", "AMZN", "META", "MSFT", "NFLX", "NVDA", "TCS"],
        )
        display_numerical_dataset_info(ticker_symbol)

    elif selected_section == "Numerical Dataset Visualization":
        """
        Shows visual representations of stock data, such as price trends
        and volume analysis for the selected ticker symbol.
        """
        ticker_symbol = st.sidebar.selectbox(
            "Select Dataset (Ticker Symbol)",
            ["AAPL", "GOOG", "AMZN", "META", "MSFT", "NFLX", "NVDA", "TCS"],
        )
        display_numerical_data_visualizations(ticker_symbol)

    elif selected_section == "Numerical Model Evaluation":
        """
        Displays performance statistics for numerical models,
        including accuracy, RMSE, and other metrics.
        """
        display_numerical_model_performance()

    elif selected_section == "Numerical Model Visualization":
        """
        Provides visualizations of numerical model predictions and actual results
        to help users understand model performance.
        """
        ticker_symbol = st.sidebar.selectbox(
            "Select Dataset (Ticker Symbol)",
            ["AAPL", "GOOG", "AMZN", "META", "MSFT", "NFLX", "NVDA", "TCS"],
        )
        display_numerical_model_visualization(ticker_symbol)

    elif selected_section == "Numerical Model Prediction":
        """
        Offers a prediction feature where users can input values manually
        or select data from a dataset to predict stock closing prices.
        """
        ticker_symbol = st.sidebar.selectbox(
            "Select Dataset (Ticker Symbol)",
            ["AAPL", "GOOG", "AMZN", "META", "MSFT", "NFLX", "NVDA", "TCS"],
        )

        input_method = st.radio(
            "Select Input Method", ("Manual Input", "Select from Dataset")
        )

        if input_method == "Manual Input":
            open_price = st.number_input(
                "Enter Open Price ($)", min_value=0.0, format="%.2f"
            )
            high = st.number_input("Enter High Price ($)", min_value=0.0, format="%.2f")
            low = st.number_input("Enter Low Price ($)", min_value=0.0, format="%.2f")
            volume = st.number_input("Enter Volume", min_value=0, format="%d")

            if st.button("Predict Closing Price"):
                display_numerical_model_predicted(
                    ticker_symbol, open_price, high, low, volume
                )

        else:
            df = pd.read_csv(
                os.path.join(DATASET_DIR, f"Preprocessed_{ticker_symbol}_Dataset.csv"),
                index_col="date",
                parse_dates=True,
            )
            date_options = df.index.strftime("%Y-%m-%d").tolist()
            selected_date = st.selectbox("Select Date", date_options)
            selected_row = df.loc[selected_date]

            open_price = selected_row["open"]
            high = selected_row["high"]
            low = selected_row["low"]
            volume = selected_row["volume"]
            close = selected_row["close"]

            st.write(f"### Using values for {selected_date}:")
            st.write(
                f"<p>Open Price: <strong>${open_price:.2f}</strong> &nbsp;&nbsp; "
                f"High: <strong>${high:.2f}</strong> &nbsp;&nbsp; "
                f"Low: <strong>${low:.2f}</strong> &nbsp;&nbsp; "
                f"Volume: <strong>{volume}</strong></p> "
                f"Close: <strong>${close:.2f}</strong></p>",
                unsafe_allow_html=True,
            )

            if st.button("Predict Closing Price"):
                display_numerical_model_predicted(
                    ticker_symbol, open_price, high, low, volume
                )

    elif selected_section == "Text Model Evaluation":
        """
        Displays performance metrics of the text-based model,
        including precision, recall, and F1-score.
        """
        display_text_model_performance()

    elif selected_section == "Text Model Visualization":
        """
        Shows visualizations related to the output of the text-based model,
        such as word clouds and sentiment analysis charts.
        """
        display_text_model_visualization()

    elif selected_section == "Text Model Prediction":
        """
        Provides a text-based prediction tool that analyzes sentiment
        and correlates it with stock price trends.
        """
        display_text_model_prediction()

    elif selected_section == "Hybrid Model Evaluation":
        """
        Evaluates the combined performance of numerical and text-based models,
        showing how well the hybrid approach works.
        """
        display_hybrid_model_performance()

    elif selected_section == "Hybrid Model Visualization":
        """
        Displays visual outputs of the hybrid model, highlighting predictions
        and actual stock price trends.
        """
        display_hybrid_model_visualization()

    elif selected_section == "Hybrid Model Prediction":
        """
        Predicts stock prices using a hybrid model that integrates numerical
        and text-based data for better accuracy.
        """
        display_hybrid_model_prediction()

    elif selected_section == "InfluxDB Database":
        """
        Provides an overview of the InfluxDB database setup used for storing
        and querying time-series data.
        """
        display_project_database()

    elif selected_section == "Grafana Dashboard":
        """
        Displays a link or an embedded Grafana dashboard that visualizes real-time
        data monitoring for stock analysis.
        """
        display_project_dashboard()

    elif selected_section == "Flask App":
        """
        Links or embeds the Flask app, enabling users to access prediction features
        through a separate web service.
        """
        display_project_flask_app()

    elif selected_section == "Meet the Team":
        """
        Introduces the team members working on the project and provides
        their contact information.
        """
        display_contact_information()

    elif selected_section == "Resources":
        """
        Lists resources and links relevant to the project, including stock data
        sources and illustrations.
        """
        display_resources_information()


# Running the main function
if __name__ == "__main__":

    # Call function to display the background image with opacity
    display_background_image(
        "https://vectormine.b-cdn.net/wp-content/uploads/Stock_Market.jpg", 0.8
    )

    # Call main function to run the app
    main()
