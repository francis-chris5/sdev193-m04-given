# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 10:33:29 2023

@author: c.s.francis


@summary: A simple test class to run configuration checks with.
"""



class Greet():
    def __init__(self):
        """
        the constructor instantiates an object with a blank message
        

        Returns
        -------
        None.

        """
        self.__message = ""
        
        
    def getMessage(self):
        """
        standard accessor to grab the message from its mangled data field

        Returns
        -------
        STR
            the message set by the user.

        """
        return self.__message
    
    
    def setMessage(self, message):
        """
        

        Parameters
        ----------
        message : STR
            the new message for the object to output.

        Returns
        -------
        None.

        """
        self.__message = message
        
    
    def simpleMessage(self):
        """
        the standard configuration check message

        Returns
        -------
        None.

        """
        self.__message = "Hello World!!!"
        
        
    def bugsMessage(self):
        """
        an all american classic greeting

        Returns
        -------
        None.

        """
        self.__message = "Nah... What's up doc?"
    
    
    def newYorkMessage(self):
        """
        a movie "blooper" that nearly killed the actor got left in the final cut and became among the most popular things for tourists to say when visiting New York City

        Returns
        -------
        None.

        """
        self.__message = "Hey! I'm walking here!"


    def __repr__(self):
        """
        the default output for the objects created from this class

        Returns
        -------
        STR
            a message --probably a greeting-- set by the user.

        """
        return self.__message
        


if __name__=="__main__":
    g1 = Greet()
    g1.newYorkMessage()
    print(g1)