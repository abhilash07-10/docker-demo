import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David'],
    'Math': [85, 78, 92, 88],
    'Science': [90, 82, 95, 85]
}

df = pd.DataFrame(data)
df['Average'] = np.mean(df[['Math', 'Science']], axis=1)

plt.bar(df['Student'], df['Average'], color='skyblue')
plt.title('Average Scores of Students')
plt.xlabel('Student')
plt.ylabel('Average Score')
plt.ylim(0, 100)
plt.grid(axis='y')
plt.show()
