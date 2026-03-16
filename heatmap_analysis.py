import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Heatmap_project\StudentsPerformance.csv.csv")

numeric_data = data[['math score','reading score','writing score']]

corr = numeric_data.corr()

sns.heatmap(corr, annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap of Student Scores")
plt.show()
