## Object Relations Articles Project

This project is a simple demonstration of object-oriented programming and the relationships between authors, articles, and magazines.

## Project Structure

The project is organized into the following structure:

- magazine/: Contains the main classes and logic for authors, articles, and magazines.
- author.py: Defines the Author class.
- article.py: Defines the Article class.
- magazine.py: Defines the Magazine class.
- test/: Contains unit tests for the classes in the lib directory.
- test_author.py: Tests for the Author class.
- test_main.py: Tests for the main logic of the project.
- main.py: The main script that demonstrates the usage of the classes.

## Getting Started

1. Clone the repository to your local machine:
- Copy code
           ` git clone git@github.com:annndiga/Object-Relations-Challenge.git`

2. cd  to the right directory for instance in this case;
          
           "/Object-Relations-Articles/lib'

3. Install the required dependencies:
- Copy code
            `pipenv install`
            `pipenv shell`

4. Run the main script to see a demonstration of the classes in action:
- Copy code
            `python main.py`

5. Running Tests
- To run the unit tests, navigate to the test directory and use the following command:
Copy code
            `sudo apt install python3-pip` 
            `pip3 install pytest`
            `pytest -x` or `pytest` 

## Project Overview

- The project showcases the relationships between authors, articles, and magazines. Authors can write articles and create magazines. Articles belong to an author and a magazine.

Author Class
- The Author class represents an author who can write articles and create magazines. Authors have a list of articles they've written and a list of magazines they've created.

- Article Class
The Article class represents an article written by an author. Articles belong to an author and a magazine.

- Magazine Class
The Magazine class represents a magazine that can contain multiple articles. Magazines have a list of articles and contributing authors.

## Contributing

If you'd like to contribute to this project, feel free to submit pull requests or issues on the GitHub repository.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
This project was created as a demonstration of object-oriented programming concepts.

