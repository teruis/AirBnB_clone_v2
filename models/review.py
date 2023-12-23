#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
	    """ Review classto store review information """
	    
	    place_id = ""
	    user_id = ""
	    text = ""
