import sys
import logging

def error_message_detail(error:Exception,error_detail:sys) ->str:
	"""
	Extracts detailed error information including file name, line number and the error message
	Params:
		error_details: The sys module to access traceback details
		error: The exception that occured
	Return:
		A formatted error message string
	"""
	_,_,exc_tb=error_detail.exc_info()
	file_name=exc_tb.tb_frame.f_code.co_filename
	line_number=exc_tb.tb_lineno
	error_message=f"Error occured in python script: [{file_name}] at line number [{line_number}]: {str(error)}"
	logging.error(error_message)
	return error_message

class MyException(Exception):
	"""
	Custom exception class for handling errors in the Vehicle insurance prediction
	"""
	def __init__(self,error_message:str,error_detail:sys):
		"""
		Initializes the Vehicle insurance prediction exception with a detailed error
		Params:
			error_message: A string describing the error.
			error_details: The sys module to access traceback details
		"""

		super().__init__(error_message)
		self.error_message=error_message_detail(error_message,error_detail)

	def __str__(self) -> str:
		"""
		Returns the string representation of the error message.
		"""
		return self.error_message