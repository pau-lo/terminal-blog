# importing our database class
from database import Database
# from models.post import Post
# from models.blog import Blog
from menu import Menu

Database.initialize()

menu = Menu()

menu.run_menu()
