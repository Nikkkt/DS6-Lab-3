import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def affine_rotation(points, pivot, alpha):
    radians = np.radians(alpha)
    cos_a = np.cos(radians)
    sin_a = np.sin(radians)

    rotation_matrix = np.array([
        [cos_a, -sin_a],
        [sin_a, cos_a]
    ])

    translated_points = points - pivot
    rotated_points = np.dot(translated_points, rotation_matrix.T)
    result_points = rotated_points + pivot

    return result_points

def read_dataset(file_path):
    with open(file_path, 'r') as file:
        data = [list(map(int, line.split())) for line in file]

    return np.array(data)

def main(input_file, output_image_file):
    dataset = read_dataset(input_file)
    pivot = np.array([480, 480])
    alpha = 70
    transformed_dataset = affine_rotation(dataset, pivot, alpha)

    canvas_size = (960, 960)

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim(0, canvas_size[0])
    ax.set_ylim(0, canvas_size[1])

    ax.scatter(transformed_dataset[:, 0], transformed_dataset[:, 1], color='blue', s=10)

    ax.set_aspect('equal', adjustable='box')

    plt.savefig(output_image_file, format='png')
    plt.close()

if __name__ == "__main__":
    input_file = "DS6.txt"
    output_image_file = "result.png"

    main(input_file, output_image_file)
