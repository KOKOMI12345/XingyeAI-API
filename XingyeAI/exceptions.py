

"""
异常类的定义
"""

class XingyeAIAPiError(Exception):
    """
    调用XingyeAI API时发生错误
    """
    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message
        super().__init__(f"XingyeAI API Error: {code} - {message}")

    def __str__(self):
        return f"XingyeAI API Error: {self.code} - {self.message}"
    
class XingyeAIFunctionalityError(XingyeAIAPiError):
    """
    调用XingyeAI API时发生功能错误
    """
    def __init__(self, message: str):
        super().__init__("FUNCTIONAL_ERROR", message)