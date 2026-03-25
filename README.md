# There And Back Again

A complete end-to-end data science project spanning the full lifecycle — from raw data ingestion and NLP analysis, through machine learning modeling and high performance computing, to a live deployed web application. Built to be industry agnostic and applicable across finance, tech, healthcare, consulting, and beyond.

## Data Sources

- Financial Phrase Bank — financial news sentences from Kaggle
  (not included in repo due to licensing)
- Teldo Customer Churn — customer records from Kaggle
  (not included in repo due to file size)
- All data placed in data/ folder before running notebooks

## Motivation

Most data science projects demonstrate one skill in isolation — a model here, a visualization there. There And Back Again was built to show the complete journey: raw data becomes insight, insight becomes a model, and the model becomes a tool anyone can use. Built to develop hands-on experience across the full data science stack using Python, SQL, Power BI, C++, and MATLAB.

## Project Structurev

there-and-back-again/
- data
- notebooks/
    - 01_sentiment_analysis.ipynb
    - 02_customer_churn_prediction.ipynb
    - 03_performance_benchmark.ipynb
- outputs/
- sql/
- cpp/
    - matrix__multiply.cpp
- matlab/
    - monte_carlo_simulation.m
- app.py
- train_model.py
- requirements.txt
- sentiment_dashboard.pbix

## Modules

### 1. Financial News Sentiment Pipeline
Built an NLP pipeline analyzing 4,846 real financial news sentences using Python and SQL. Classified sentiment as positive, negative, or neutral using TextBlob achieving 54.73% accuracy. Identified that financial language requires domain specific NLP models due to specialized vocabulary. 

### 2. Customer Churn Prediction
Built and compared three supervised ML models — Logistic Regression, Random Forest, and XGBoost — on 7,032 telecom customer records. Random Forest achieved 79.25% accuracy. SHAP analysis revealed contract type as the strongest churn predictor. 

### 3. Performance & Visualization
Three components — a Power BI dashboard connected to the SQL sentiment database with KPI cards, donut chart, and color coded conditional formatting. A C++ matrix multiplication benchmark showing 44.5x speedup over Python loops. A MATLAB Monte Carlo simulation of 10,000 stock price paths showing 38% probability of loss over one year.

### 4. Deployed Web App
Deployed the Random Forest churn prediction model as a live interactive Streamlit web application. Users input customer details and recieve an instant churn probability prediction.

## Key Results

**Financial News Sentiment Analysis**
- Dataset: 4,846 real financial news sentences
- TextBlob accuracy: 54.73%
- Top finding: Financial text requires domain specific NLP

**Customer Churn Prediction**
- Dataset: 7,032 telecom customer records
- Random Forest accuracy: 79.25% 
- Top churn predictor: Contract type (SHAP analysis)

**Performance Benchmark**
- C++ vs Python loops: 44.5x faster
- NumPy vs Python loops: 6,725x faster
- Key insight: Optimization matters more than language choice

**MATLAB Monte Carlo**
- Simulations: 10,000 stock prices paths
- Mean final price: $108.36
- Probability of loss: 38.06%

**Deployed Web App**
- Live URL: https://matthewburns1-project-3-app-3aexhf.streamlit.app/ 
- Model: Random Forest churn predictor
- Access: Public — no code required

## Tools Used 

**Languages** 
- Python
- SQL
- C++
- MATLAB

**Libraries**
- pandas
- numpy
- matplotlib
- scikit-learn
- xgboost
- shap
- textblob
- nltk
- folium
- sqlalchemy 
- streamlit

**Visualization**
- Power BI Desktop

**Environment**
- Jupyter Notebook
- VS Code
- Anaconda
- Git

## How to Run

1. Clone the repository
2. Open notebooks in VS Code with Jupyter extension
3. Run the notebooks in order:
   - 01_sentiment_analysis.ipynb
   - 02_customer_churn_prediction.ipynb
   - 03_performance_benchmark.ipynb
4. Open sentiment_dashboard.pbic in Power BI Desktop
5. Run the C++ benchmark:
   - g++ -o cpp/matrix_multiply cpp/matrix_multiply.cpp
   - cpp/matrix_multiply
6. Run the MATLAB simulation in MATLAB Desktop
7. Train the model: python train_model.py
8. Run the web app: streamlit run app.py

**Requirements**
- Anaconda
- VS Code
- Power BI Desktop
- MATLAB
- MinGW C++ compiler
- Run: pip install -r requirements.txt

**Live App**
- https://matthewburns1-project-3-app-3aexhf.streamlit.app/

**Data**
- Download Financial Phrase Bank from Kaggle
- Download Telco Customer Churn from Kaggle
- Place both CSV files in the data/ folder