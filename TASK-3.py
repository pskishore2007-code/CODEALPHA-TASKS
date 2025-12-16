CODE:
import seaborn as sns
import matplotlib.pyplot as plt

sns.pairplot(df)   # relationships between variables
sns.heatmap(df.corr(), annot=True)  # correlation matrix



QUESTIONS TO BE ASKEDBEFORE analysis
- What factors influence the target variable?
- Are there seasonal or time-based effects?
- Are there outliers that could skew results?
- What decisions will this analysis support? (business, academic, technical).
