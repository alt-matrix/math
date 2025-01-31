import numpy as np
import matplotlib.pyplot as plt

def generate_matrix_art():
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_frame_on(False)
    
    # Create a random transformation matrix
    matrix = np.random.rand(2, 2) - 0.5
    
    # Generate a grid of points
    x, y = np.meshgrid(np.linspace(-1, 1, 10), np.linspace(-1, 1, 10))
    points = np.vstack([x.ravel(), y.ravel()])
    
    # Apply transformation
    transformed_points = matrix @ points
    
    # Draw original and transformed points
    ax.scatter(points[0], points[1], color='blue', alpha=0.5, label='Original')
    ax.scatter(transformed_points[0], transformed_points[1], color='red', alpha=0.5, label='Transformed')
    
    # Draw connecting lines (representing neural network connections)
    for i in range(points.shape[1]):
        ax.plot([points[0, i], transformed_points[0, i]], 
                [points[1, i], transformed_points[1, i]], 
                color='black', alpha=0.3)
    
    plt.legend()
    plt.show()

# Generate the artwork
if __name__ == '__main__':
    generate_matrix_art()
