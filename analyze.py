import pandas as pd

# Load the dataset
df = pd.read_json("hf://datasets/ArtifactAI/arxiv-physics-instruct-tune-30k/arxiv_physics_instruct_30k.jsonl", lines=True)

print(df.head())
# Calculate the length of each sentence
df['Qsentence_length'] = df['question'].apply(lambda x: len(x.split()))

import matplotlib.pyplot as plt

# Print the distribution of sentence lengths
print(df['Qsentence_length'].describe())

# Create a histogram of sentence lengths
plt.hist(df['Qsentence_length'], bins=30)
plt.xlabel('Question Length')
plt.ylabel('Frequency')
plt.title('Distribution of Question Lengths')
plt.show()


# Calculate the length of each sentence
df['Asentence_length'] = df['answer'].apply(lambda x: len(x.split()))


# Print the distribution of sentence lengths
print(df['Asentence_length'].describe())

# Create a histogram of sentence lengths
plt.hist(df['Asentence_length'], bins=30)  # Increase the number of bins for finer spacing
plt.xlabel('Answer Length')
plt.ylabel('Frequency')
plt.title('Distribution of Answer Lengths')
plt.show()