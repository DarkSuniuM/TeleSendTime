"""SendTime Module Utility Functions."""


def load_template(file_path):
    """Load template from file."""
    with open(file_path, 'rb') as file:
        return file.read().decode('UTF-8')
