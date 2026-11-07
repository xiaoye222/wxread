# config.py 自定义配置,包括阅读次数、推送token的填写
import os
import shlex
from http.cookies import SimpleCookie

"""
可修改区域
默认使用本地值如果不存在从环境变量中获取值
"""

# 阅读次数 默认40次/20分钟
READ_NUM = int(os.getenv('READ_NUM') or 40)
# 可选 email、pushplus、wxpusher、telegram、serverchan、webhook；多个渠道用英文逗号分隔。
PUSH_METHOD = "" or os.getenv('PUSH_METHOD')
# pushplus推送时需填
PUSHPLUS_TOKEN = "" or os.getenv("PUSHPLUS_TOKEN")
# telegram推送时需填
TELEGRAM_BOT_TOKEN = "" or os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = "" or os.getenv("TELEGRAM_CHAT_ID")
# wxpusher推送时需填
WXPUSHER_SPT = "" or os.getenv("WXPUSHER_SPT")
# SeverChan推送时需填
SERVERCHAN_SPT = "" or os.getenv("SERVERCHAN_SPT")


# read接口的bash命令，本地部署时可对应替换headers、cookies
curl_str = os.getenv('WXREAD_CURL_BASH')

# headers、cookies是一个省略模版，本地或者docker部署时对应替换
cookies = {
    'RK': 'oxEY1bTnXf',
    'ptcz': '53e3b35a9486dd63c4d06430b05aa169402117fc407dc5cc9329b41e59f62e2b',
    'pac_uid': '0_e63870bcecc18',
    'iip': '0',
    '_qimei_uuid42': '183070d3135100ee797b08bc922054dc3062834291',
    'wr_avatar': 'https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FeEOpSbFh2Mb1bUxMW9Y3FRPfXwWvOLaNlsjWIkcKeeNg6vlVS5kOVuhNKGQ1M8zaggLqMPmpE5qIUdqEXlQgYg%2F132',
    'wr_gender': '0',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ko;q=0.5',
    'baggage': 'sentry-environment=production,sentry-release=dev-1730698697208,sentry-public_key=ed67ed71f7804a038e898ba54bd66e44,sentry-trace_id=1ff5a0725f8841088b42f97109c45862',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
}


# 书籍（自选书单）
book = [
    "64e32ec0813abaccfg0159ba",  # 青春手记（西蒙娜·德·波伏瓦作品系列） - [法]西蒙娜·德·波伏瓦
    "86532410813aba15cg0177e4",  # 读懂三国：三国演义＋三国志＋易中天品读 - [明]罗贯中 [西晋]陈寿 裴松之 易中天
    "4cc32cb0813ab9d79g011dfe",  # 余华文学课：九岁的委屈和九十岁的委屈 - 余华
    "cdb328a0813ab72b7g014d7a",  # 如何有逻辑地表达 - 宋晓阳
    "24732e6072b28b1524746ba",  # 繁荣与停滞：日本经济发展和转型 - 伊藤隆敏 星岳雄
    "aed32c10717d45c7aeddf00",  # 在群中：数字媒体时代的大众心理学 - 韩炳哲
    "822322405cb2d68225b634b",  # 二手时间 - S.A.阿列克谢耶维奇
    "6e332dc0811e1a5eag017be3",  # 每周工作4小时 - [美]费里斯
    "57e324b05d047c57ebe463e",  # 杀死一只知更鸟（同名电影原著） - 哈珀·李
    "dd732db0813ab950dg01485c",  # 等一切风平浪静（治愈散文） - 刘同
    "6d832ca0813ab9330g010958",  # 必要的丧失 - [美]朱迪思·维奥斯特
    "bb432f60813ab8444g014d61",  # 深度关系 - 武志红
    "05032c10813ab81e7g0105ca",  # 深入北方的小路（布克奖震撼杰作） - 理查德•弗兰纳根
    "266327205ccc7b266a59c98",  # 台北人 - 白先勇
    "091322d05cd5230913042e3",  # 万历十五年（精装版） - 黄仁宇
    "7c2321f0729fc9317c2ff83",  # 金钱博弈 - 单伟建
    "b7d32470813ab7e0eg015e3f",  # 非暴力沟通（修订版） - [美]马歇尔·卢森堡
    "9f432800728dd5a09f4d4f3",  # 读水浒：人性的十三种刻度 - 押沙龙
    "d7d32d70722dd429d7d723d",  # 爱的艺术 - [美]艾里希·弗洛姆
    "56d325907203e8a856def7f",  # 高效能人士的七个习惯（30周年纪念版）（全新增订版） - 史蒂芬·柯维
    "286329405b40f728668c477",  # 我们生活在巨大的差距里 - 余华
    "7fe32070813ab7684g012bbf",  # 面纱（珍藏版） - [英]W.毛姆·萨默塞特
    "7fd324707183b7147fda6a5",  # 飘（世界文学名著名译典藏） - [美]玛格丽特·米切尔
    "f0e32c60813ab7e29g01307d",  # 一只鸟接着一只鸟：关于写作与人生的建议 - 安·拉莫特
    "3a832f705d0d1f3a8ec72ff",  # 悉达多（果麦经典） - [德]赫尔曼·黑塞
    "4ec322505d234a4ecf640ab",  # 人生的智慧 - 叔本华
    "6bf3215071a123016bf0b74",  # JavaScript设计模式与开发实践 - 曾探
    "845323407299950f8450b99",  # Webpack实战：入门、进阶与调优（第2版） - 居玉皓
    "27132c50725b7002271d9ad",  # JavaScript悟道 - 道格拉斯·克罗克福德
    "8d432a60726c875e8d4687a",  # 学习的方法：一位诺贝奖获得者的人生忠告 - 圣地亚哥·拉蒙-卡哈尔
]

# 章节
chapter = [
    "ecc32f3013eccbc87e4b62e","a87322c014a87ff679a21ea","e4d32d5015e4da3b7fbb1fa","16732dc0161679091c5aeb1",
    "8f132430178f14e45fce0f7","c9f326d018c9f0f895fb5e4","45c322601945c48cce2e120","d3d322001ad3d9446802347",
    "65132ca01b6512bd43d90e3","c20321001cc20ad4d76f5ae","c51323901dc51ce410c121b","aab325601eaab3238922e53",
    "9bf32f301f9bf31c7ff0a60","c7432af0210c74d97b01b1c","70e32fb021170efdf2eca12","6f4322302126f4922f45dec"
]

"""
建议保留区域|默认读三体，其它书籍自行测试时间是否增加
"""
data = {
    "appId": "wb182564874603h266381671",
    "b": "ce032b305a9bc1ce0b0dd2a",
    "c": "7f632b502707f6ffaa6bf2e",
    "ci": 27,
    "co": 389,
    "sm": "19聚会《三体》网友的聚会地点是一处僻静",
    "pr": 74,
    "rt": 15,
    "ts": 1744264311434,
    "rn": 466,
    "sg": "2b2ec618394b99deea35104168b86381da9f8946d4bc234e062fa320155409fb",
    "ct": 1744264311,
    "ps": "4ee326507a65a465g015fae",
    "pc": "aab32e207a65a466g010615",
    "s": "36cc0815"
}


def convert(curl_command):
    """只解析 cURL 文本，绝不执行。兼容单/双引号及换行。"""
    tokens = shlex.split(curl_command.replace('\\\n', ''))
    parsed_headers, cookie_string = {}, ''
    for index, token in enumerate(tokens[:-1]):
        if token in ('-H', '--header') and ':' in tokens[index + 1]:
            key, value = tokens[index + 1].split(':', 1)
            if key.lower() == 'cookie':
                cookie_string = value.strip()
            else:
                parsed_headers[key.lower()] = value.strip()
        elif token in ('-b', '--cookie'):
            cookie_string = tokens[index + 1]
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    return parsed_headers, {key: value.value for key, value in cookie.items()}


headers, cookies = convert(curl_str) if curl_str else (headers, cookies)
