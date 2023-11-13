import nbformat

# Load the JSON file
with open('input.json', 'r') as f:
    notebook_data = nbformat.read(f, as_version=4)

# Save the notebook data as an IPython Notebook
with open('convolutions.ipynb', 'w') as f:
    nbformat.write(notebook_data, f)
