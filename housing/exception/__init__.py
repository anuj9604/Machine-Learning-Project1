import os
import sys

class HousingException(Exception):

    def __init__(self, err_msg:Exception, err_details:sys):
        super().__init__(err_msg)
        self.err_msg=HousingException.get_detailed_err_msg(err_msg=err_msg, err_details=err_details)

    @staticmethod
    def get_detailed_err_msg(err_msg:Exception, err_details:sys)->str:
        """err_msg: Exception class object
        err_details: object of sys module"""
        _, _, exec_tb=err_details.exc_info()
        line_number=exec_tb.tb_frame.f_lineno
        file_name=exec_tb.tb_frame.f_code.co_filename
        err_msg=f"Error occured in script: [{file_name}] at line number: [{line_number}] error messge: [{err_msg}]"
        return err_msg

    def __str_(self):
        return self.err_msg

    def __repr__(self)->str:
        return HousingException.__name__.str()


