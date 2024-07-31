# College Majors and Salaries Analysis

This project analyzes college majors and their starting and mid-career salaries using Pandas, a popular data manipulation library in Python. 
The dataset includes various majors, their starting median salaries, and mid-career median salaries, among other data points.


## Installation

To run this project, you need to have Python installed. You can download it from the official [Python website](https://www.python.org/).

1. Clone the repository:


2. Navigate to the project directory:
   ```bash
   cd college-majors-salaries-analysis
   ```

3. Install the required packages:
   ```bash
   pip install pandas
   ```

## Usage
You can run this project locally or on Google Colab.
1. Ensure you have the dataset CSV file in the project directory. Update the file path in the script if necessary.
2. Run the analysis script:
   ```bash
   python analysis.py
   ```
Running on Google Colab
Open Google Colab.
Upload your dataset CSV file to the Colab environment.
Copy and paste the code from analysis.py into a new Colab notebook cell.
Run the cell to execute the analysis.


## Data

The dataset used in this project is a CSV file containing the following columns:
- `Undergraduate Major`: The name of the major.
- `Starting Median Salary`: The median salary of graduates with this major at the beginning of their careers.
- `Mid-Career Median Salary`: The median salary of graduates with this major in the middle of their careers (10+ years of experience).
- `Mid-Career 10th Percentile Salary`: The 10th percentile salary for mid-career professionals.
- `Mid-Career 90th Percentile Salary`: The 90th percentile salary for mid-career professionals.
- `Group`: The category of the major (e.g., STEM, HASS, Business).

## Analysis

The analysis script performs the following tasks:

1. **Load the Data**: Reads the CSV file into a Pandas DataFrame.
2. **Identify Highest and Lowest Salaries**:
   - Finds the major with the highest starting median salary.
   - Finds the major with the highest mid-career median salary.
   - Finds the major with the lowest starting median salary.
   - Finds the major with the lowest mid-career median salary.
3. **Calculate Salary Spread**:
   - Calculates the difference between the 90th and 10th percentile mid-career salaries to identify low-risk majors.
   - Sorts and displays majors with the smallest and largest salary spreads.
4. **Group Analysis**:
   - Groups majors by their category (STEM, HASS, Business).
   - Calculates the average starting and mid-career salaries for each category.
   - 
   ![pythondata](https://github.com/user-attachments/assets/a1dd729b-bb1b-4922-a67c-f8dec325b08d)
![Python2](https://github.com/user-attachments/assets/46583d6a-e161-4d9c-aebd-144d0e81cc7f)
![Python3](https://github.com/user-attachments/assets/e5272433-64da-4cd5-99ff-cf0e04a61a4c)
![python4](https://github.com/user-attachments/assets/fdf3b441-303c-4699-b9ce-379a760f80a6)
![Python5](https://github.com/user-attachments/assets/1a58cc9a-bf6e-4044-a0ca-e09d6296da4f)
![Python6](https://github.com/user-attachments/assets/fe763ec6-4bd0-4527-b033-469ecfb8e81b)


