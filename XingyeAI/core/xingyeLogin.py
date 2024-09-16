import requests
import json
import time
from ..exceptions import XingyeAIFunctionalityError
from ..utils import logger
from .datamodels import XingyeLoginUserData

class XingyeLogin:
    """
    这里是尝试登录的逻辑类
    """
    def __init__(self, username: str = "", password: str = "") -> None:
        self.username = username if username is not None and username!= "" else "u___183908751847858"
        self.password = password if password is not None and password!= "" else "UP7Odz1HgP"
        self.token_url = "https://a1-xingye.easemob.com/1147220623101786/xingye/token"
        self.headers = \
        {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
        }
        self.login_body = {
            "grant_type": "password",
            "username": self.username,
            "password": self.password,
            "timestamp": str(int(time.time()))
        }

    def AttemptingToLogin(self) -> XingyeLoginUserData:
        """
        尝试登录
        """
        try:
            resp = requests.post(self.token_url, headers=self.headers, json=self.login_body)
            access_token = json.loads(resp.text)["access_token"]
            expire_timestamp = json.loads(resp.text)["expires_in"]
            user = json.loads(resp.text)["user"]
            resp.raise_for_status()
            logger.success("登录成功")
            return XingyeLoginUserData(access_token, expire_timestamp, user)
        except json.JSONDecodeError:
            raise XingyeAIFunctionalityError("登录失败,请检查用户名和密码是否正确")
        except requests.exceptions.HTTPError:
            logger.warning("登录失败,请检查用户名和密码是否正确")
        except KeyError:
            logger.warning("登录失败,请检查用户名和密码是否正确")
            raise XingyeAIFunctionalityError(f"登录失败,请检查用户名和密码是否正确: {resp.text}")