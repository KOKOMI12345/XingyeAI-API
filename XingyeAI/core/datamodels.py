import json

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