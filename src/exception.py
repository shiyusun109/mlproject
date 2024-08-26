import sys
import logging

def error_message_detail(error,error_detail:sys): #sys module to traceback information. error_detail should be of type sys.
    _,_,exc_tb = error_detail.exc_info()         #exc_tb: trackback object
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message


class CustomException(Exception): #inheriting parent message exception
    def __init__(self,error_message,error_detail:sys):   # Initialize the base class with the error_message
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    
