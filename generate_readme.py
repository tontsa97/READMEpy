import os

def generate_readme(project_name, description):
    readme_content = f"""# {project_name}

{description}

## Installation

1. **Clone this repository:**

    ```sh
    git clone https://github.com/user/{project_name}.git
    ```

2. **Navigate to the project directory:**

    ```sh
    cd {project_name}
    ```

3. **Open the `index.html` file in your browser:**

    You can open the file directly in your browser by double-clicking on it or using your preferred browser.

## Files

- `index.html`: Main page containing the HTML structure.
- `styles.css`: Style sheet defining the page layout.
- `script.js`: JavaScript file generating random poems.
- `README.md`: This file containing instructions and information about the project.

## Usage

1. Open `index.html` in your browser.
2. You will see a random poem with a nighttime theme.
3. Press the "Generate New Poem" button to create a new poem.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
"""
    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)

if __name__ == "__main__":
    project_name = input("Enter the project name: ")
    description = input("Enter a brief description of the project: ")
    generate_readme(project_name, description)
    print("README.md has been successfully created.")
