from base64 import b64encode
from io import BytesIO


def encode_data(data: bytes | BytesIO | str) -> str:
    """
    对数据进行 Base64 编码
    :param data: 要编码的数据，可以是字节串或字符串
    :return: 编码后的字符串
    """
    if isinstance(data, str):
        data = data.encode("utf-8")
    elif isinstance(data, BytesIO):
        data = data.getvalue()
    return b64encode(data).decode()
