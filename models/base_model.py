#!/usr/bin/python3
"""
BaseModel module
"""
import uuid
from datetime import datetime

class BaseModel:
	"""
		BaseModel class: defines all common
				 attributes/methods for other classes
	"""
	def __init__(self):
		"""init a new instance of class"""
		self.id = str(uuid.uuid4())
		self.created_at = datetime.now()
		self.updated_at = self.created_at

	def __str__(self):
		"""Return a string rep. of the instance"""
		return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

	def save(self):
		"""Update the updated_at with the current time and date"""
		self.updated_at = datetime.now()

	def to_dict(self):
		"""Return  a dict rep. of the instance"""
		result = self.__dict__.copy()
		result["__class__"] = self.__class__.__name__
		result["created_at"] = self.created_at.isoformat()
		result["updated_at"] = self.updated_at.isoformat()
		return result

