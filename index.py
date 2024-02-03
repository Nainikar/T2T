import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Define the Problem
# We'll create a simple example with locations and distances.
locations = {
    'A': (0, 0),
    'B': (1, 2),
    'C': (3, 1),
    'D': (5, 3),
    'E': (6, 0)
}

distances = {
    ('A', 'B'): 3,
    ('A', 'C'): 4,
    ('B', 'C'): 2,
    ('B', 'D'): 5,
    ('C', 'D'): 1,
    ('C', 'E'): 6,
    ('D', 'E'): 3
}

# Step 2: Prepare Data for Machine Learning
# Create a DataFrame with features (distances) and target (optimized time)
data = {'start': [], 'end': [], 'distance': [], 'time': []}

for (start, end), distance in distances.items():
    data['start'].append(start)
    data['end'].append(end)
    data['distance'].append(distance)
    data['time'].append(distance * 2)  # Simulated time (linear relation)

df = pd.DataFrame(data)

# Step 3: Split Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(df[['distance']], df['time'], test_size=0.2, random_state=42)

# Step 4: Train a Machine Learning Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Make Predictions
df['predicted_time'] = model.predict(df[['distance']])

# Step 6: Create a Graph
G = nx.Graph()
G.add_nodes_from(locations.keys())
G.add_edges_from(distances.keys())

# Step 7: Visualize the Graph and Predictions
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold')

# Display the edges with predicted times as labels
edge_labels = {(i, j): f"{distances[(i, j)]}\n{model.predict([[distances[(i, j)]]])[0]:.2f} mins" for i, j in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

plt.title("Route Optimization with Machine Learning")
plt.show()
