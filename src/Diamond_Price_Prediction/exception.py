import sys


class CustomExecption(Exception):
    
    def __init__(self, error_msg, error_details : sys):
        self.error_msg = error_msg
        _,_,exc_traceback = error_details.exc_info()

        self.line_no = exc_traceback.tb_lineno
        self.filename = exc_traceback.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occured in python script name [{0}] and line no [{1}] error message [{2}]".format(
            self.filename, self.line_no, str(self.error_msg)
        )



if __name__ == "__main__":
     
    try:
         a = 2/0

    except Exception as e:
        raise CustomExecption(e, sys)