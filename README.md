# EDA on US Visa Applications Dataset

This project performs exploratory data analysis on the US visa applications dataset. The analysis includes data cleaning, visualization, and insights generation.

## Dataset

The dataset contains various attributes related to US visa applications, including:
- Case Number
- Case Status
- Decision Date
- Employer City
- Job Title
- Country of Citizenship
- Application Type
- Education Level

## Libraries Used

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

## Data Preprocessing

- Loaded the dataset
- Dropped unnecessary columns
- Handled missing values
- Dropped rows with 'Withdrawn' status
- Normalized case statuses

## Exploratory Data Analysis (EDA)

- Distribution of case statuses
- Year-wise visa status analysis
- Analysis of top employer cities
- Analysis of top job titles
- Analysis of countries of citizenship
- Analysis of application types
- Analysis of education levels

## Visualizations

- Bar plots and count plots for various attributes
- Year-wise analysis of visa status
- Top employer cities and job titles
- Analysis of countries of citizenship, application types, and education levels

## How to Run

1. Install the necessary libraries:
    ```shell
    pip install pandas numpy matplotlib seaborn scikit-learn
    ```
2. Ensure you have the dataset file named `us_perm_visas.csv` in the same directory.
3. Run the script:
    ```shell
    python eda_us_visas.py
    ```

