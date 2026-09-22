import seaborn as sns
tip=sns.load_dataset("tips")
print(tip.head())
objective="classification: Survived (Yes/No)"
success_criteria="Accuracy > 80%"
constraints="Limited features, missing vals, imbalenced classes"
print("Objective:",objective)
print("Success: ",success_criteria)
print("Constraints:",constraints)