from entities.user import User
import re
import sys, pdb

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        pdb.Pdb(stdout=sys.__stdout__).set_trace()
        
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")
        
        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa

        #####################################################
        # tarkistetaan ensin käyttäjätunnuksen oikeellisuus #
        #####################################################

        
        if len(username) < 3:
            raise UserInputError("Username is too short!")

        
        match = re.match("^[a-z]+$", username)
        #print(match)
        if match == None:
            raise UserInputError("Username is not valid!")
        
            

        _user = self._user_repository.find_by_username(username)
        
        if _user != None:
            raise UserInputError("Username is already exists!")
        
        #####################################################
        # tarkistetaan sitten salasanan oikeellisuus        #
        #####################################################

        if len(password) < 8:
            raise UserInputError("Password is too short!")

        match1 = re.search("[0|1|2|3|4|5|6|7|8|9]", password)
        match2 = re.search("[a-z]", password)

        if match1 == None or match2 == None:
            raise UserInputError("Password is not valid!")
        

