from XingyeAI import XingyeLogin

if __name__ == '__main__':
    login = XingyeLogin()
    data = login.AttemptingToLogin().ToJson()
    print(data)