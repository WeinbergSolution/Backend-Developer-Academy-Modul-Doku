from dotenv import load_dotenv      # importiert die Libary from dotenv 
                                    # load_dotenv
import os                           # Das Operating System

load_dotenv()                       # läd die Dotenv

secretkey = os.getenv("SECRET_KEY") # läd den SECRET_KEY aud der .env
                                    # und speichert ihn in "secretkey"

print(secretkey)                    # gibt den secretkey auf der console aus.
                                    # nur Demo, macht man so nicht.
                                    

username = os.getenv("USER_NAME")   # Läd den USER_NAME aus der .env
                                    # und speichert diesen in "username"

print(username)                     # gibt den username aus 