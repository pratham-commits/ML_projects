import sys
from src.logger import logging

#any exception is being generated sys will be able to handle it

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    line_number=exc_tb.tb_lineno
    error_msg=str(error)

    #exc_tb will contain all the error info where the error has occurred , on which line error has occurred
    error_message="Error occurred in python script [{0}] \n Line number [{1}] \n error message [{2}]".format(
        file_name,
        line_number,
        error_msg
    )
    logging.info('Error occurred:',error_message)
    return error_message

#this function needs to be called when an exception is to be raised
#so for that we are creating a class below

class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    


        

