import matplotlib.pyplot as plt
import seaborn as sns
df=sns.load_dataset("titanic")
sns.histplot(df['age'],bins=20,kde=True)
plt.title("Age distribution")
plt.show()
df=sns.load_dataset("titanic")
df=sns.histplot(df['size'],bins=10,kde=True)
plt.title("Age distribution")
plt.show()
