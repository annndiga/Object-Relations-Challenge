import sys
import os
# Adjust the path to the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from lib.author import Author
from lib.magazine import Magazine
from lib.article import Article

# Create authors
author1 = Author("Brandy Makena")
author2 = Author("Kyle Njuki")

# Create magazines
magazine1 = Magazine("Tech At the Moment", "Technology")
magazine2 = Magazine("Gen Z on Health", "Health")

# Authors write articles
author1.write_article("Python Basics", magazine1)
author2.write_article("Machine Learning", magazine1)
author2.write_article("Healthy Habits", magazine2)

# Authors create magazines
author1.write_magazine("Tech Today", "Technology")
author2.write_magazine("Health Weekly", "Health")

# Test methods
print(author1)
print(author2)
print(magazine1)
print(magazine2)
print([author.name for author in magazine1.contributing_authors()])
