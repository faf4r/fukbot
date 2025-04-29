# 动态绑定方法到api实例上，实现本地文件上传
from botpy import Client
from botpy.types import message
from botpy.http import Route


async def post_group_file(
    self: Client,
    group_openid: str,
    file_type: int,
    file_data: str,
    srv_send_msg: bool = False,
) -> message.Media:
    """
    上传/发送群聊图片

    Args:
        group_openid (str): 您要将消息发送到的群的 ID
        file_type (int): 媒体类型：1 图片png/jpg，2 视频mp4，3 语音silk，4 文件（暂不开放）
        file_data (str): 需要发送媒体资源的b64编码字符串
        srv_send_msg (bool): 设置 true 会直接发送消息到目标端，且会占用主动消息频次
    """
    payload = locals()
    payload.pop("self", None)
    route = Route("POST", "/v2/groups/{group_openid}/files", group_openid=group_openid)
    return await self._http.request(route, json=payload)


async def post_c2c_file(
    self: Client,
    openid: str,
    file_type: int,
    file_data: str,
    srv_send_msg: bool = False,
) -> message.Media:
    """
    上传/发送c2c图片

    Args:
        openid (str): 您要将消息发送到的用户的 ID
        file_type (int): 媒体类型：1 图片png/jpg，2 视频mp4，3 语音silk，4 文件（暂不开放）
        file_data (str): 需要发送媒体资源的b64编码字符串
        srv_send_msg (bool): 设置 true 会直接发送消息到目标端，且会占用主动消息频次
    """
    payload = locals()
    payload.pop("self", None)
    route = Route("POST", "/v2/users/{openid}/files", openid=openid)
    return await self._http.request(route, json=payload)
