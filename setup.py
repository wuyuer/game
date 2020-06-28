from setuptools import setup, find_packages  

files = ["*", "images/*"]

setup(  
    name = "game",  
    version = "1.0",  
    keywords = ("game", "xxx"),  
    description = "game",  
    license = "MIT Licence",  
    url = "whatever",
  
    author = "test",  
    author_email = "test@gmail.com",  
  
    packages = ['src'],
    package_data = {'src': files}
    #include_package_data = True,  
    #platforms = "any",  
    #requires = ['pygame'],  
  
    #scripts = [],  
    #entry_points = {  
    #    'console_scripts': [  
    #        'test = test.help:main'  
    #    ]  
    #}  
)
