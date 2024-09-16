import requests
import json
import time
from ..exceptions import XingyeAIFunctionalityError
from ..utils import logger

class XingyeLoginUserData:
    """
    XingyeLogin登录后,会返回一个包含此类信息的对象
    """
    def __init__(self,
        access_token: str,
        expire_timestamp: int,
        user_info: dict
    ) -> None:
        self.access_token: str = access_token
        self.expire_timestamp: int = expire_timestamp
        self.user_info_dict: dict = user_info
        self.user_uuid: str = user_info.get("uuid")
        self.is_user_activated: bool = user_info.get("activated")
        self.req_type: str = user_info.get("type")
        self.created_at: int = user_info.get("created")
        self.username: str = user_info.get("username")
        self.modified_at: int = user_info.get("modified")

    def ToJson(self) -> str:
        """
        将登录信息转换为json字符串
        """
        info = {
            "grand_type": "password",
            "access_token": self.access_token,
            "expire_in": self.expire_timestamp,
            "user": self.user_info_dict
        }
        return json.dumps(info)

    def __str__(self) -> str:
        return (
            f"XingyeLoginUserData( \n"
            f"access_token={self.access_token}, \n"
            f"expire_timestamp={self.expire_timestamp}, \n"
            f"user_uuid={self.user_uuid}, \n"
            f"is_user_activated={self.is_user_activated}, \n"
            f"req_type={self.req_type}, \n"
            f"created_at={self.created_at}, \n"
            f"username={self.username}, \n"
            f"modified_at={self.modified_at}\n)"
        )

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