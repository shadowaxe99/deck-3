```python
import numpy as np
from scipy.spatial import ConvexHull
from skimage import measure
from stl import mesh

def generate_hologram_mesh(model_data):
    """
    Generate a 3D mesh for the hologram from the model data.
    """
    vertices, faces = measure.marching_cubes(model_data)
    return mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))

def create_hologram(model_data, color=(0, 255, 0), opacity=0.5):
    """
    Create a hologram from the model data.
    """
    hologram_mesh = generate_hologram_mesh(model_data)
    hologram_mesh.vectors = vertices[faces]
    hologram_mesh.update_normals()

    return {
        'mesh': hologram_mesh,
        'color': color,
        'opacity': opacity
    }

def display_hologram(hologram, position=(0, 0, 0), rotation=(0, 0, 0)):
    """
    Display the hologram at the specified position and rotation.
    """
    hologram_mesh = hologram['mesh']
    hologram_mesh.translate(position)
    hologram_mesh.rotate(rotation)

    # Display the hologram using a hologram display library
    # This is a placeholder and should be replaced with actual code to display the hologram
    display_hologram_mesh(hologram_mesh, hologram['color'], hologram['opacity'])
```