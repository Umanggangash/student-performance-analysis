import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("students_data.xlsx")

# Average marks
data["Average"] = (data["Math"] + data["Science"] + data["English"]) / 3

# Top students
top_students = data.sort_values(by="Average", ascending=False).head()

print("Top Students:")
print(top_students[["Name","Average"]])

# Plot marks distribution
plt.bar(data["Name"], data["Average"])
plt.xticks(rotation=45)
plt.title("Student Average Marks")
plt.ylabel("Average Score")
plt.tight_layout()

plt.savefig("dashboard.png")
plt.show()