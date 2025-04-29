on_func_names = [
    # # guilds
    # "on_guild_create",  # (self, guild: Guild)  当机器人加入新guild时
    # "on_guild_update",  # (self, guild: Guild)  当guild资料发生变更时
    # "on_guild_delete",  # (self, guild: Guild)  当机器人退出guild时
    # "on_channel_create",  # (self, channel: Channel)  当channel被创建时
    # "on_channel_update",  # (self, channel: Channel)  当channel被更新时
    # "on_channel_delete",  # (self, channel: Channel)  当channel被删除时
    # # guild_members
    # "on_guild_member_add",  # (self, member:Member): 当成员加入时
    # "on_guild_member_update",  # (self, member:Member): 当成员资料变更时
    # "on_guild_member_remove",  # (self, member:Member): 当成员被移除时
    # guild_messages  注意：仅 *私域* 机器人能够设置此 intents
    "on_message_create",  # (self,message:Message):
    # 发送消息事件，代表频道内的全部消息，而不只是 at 机器人的消息。内容与 AT_MESSAGE_CREATE 相同
    "on_message_delete",  # (self,message:Message): 删除（撤回）消息事件
    # guild_message_reactions
    "on_message_reaction_add",  # 为消息添加表情表态
    "on_message_reaction_remove",  # 为消息删除表情表态
    # direct_message
    "on_direct_message_create",  # 当收到用户发给机器人的私信消息时
    "on_direct_message_delete ",  # 删除（撤回）消息事件
    # # interaction
    # "on_message_audit_pass",  # 消息审核通过
    # "on_message_audit_reject",  # 消息审核不通过
    # # forums  注意：仅 *私域* 机器人能够设置此 intents
    # "on_forum_thread_create",  #        当用户创建主题时
    # "on_forum_thread_update",  #        当用户更新主题时
    # "on_forum_thread_delete",  #        当用户删除主题时
    # "on_forum_post_create",  #          当用户创建帖子时
    # "on_forum_post_delete",  #          当用户删除帖子时
    # "on_forum_reply_create",  #         当用户回复评论时
    # "on_forum_reply_delete",  #         当用户删除评论时
    # "on_forum_publish_audit_result",  # 当用户发表审核通过时
    # # audio_action
    # "on_audio_start",  # 音频开始播放时
    # "on_audio_finish",  # 音频播放结束时
    # "on_audio_on_mic",  # 上麦时
    # "on_audio_off_mic",  # 下麦时
    # public_guild_messages
    "on_at_message_create",  # 当收到@机器人的消息时
    "on_public_message_delete",  # 当频道的消息被删除时
    # # audio_or_live_channel_member
    # "on_audio_or_live_channel_enter",  # 用户进入音视频/直播子频道时
    # "on_audio_or_live_channel_exit",   # 用户退出音视频/直播子频道时
    # # open_forum_event
    # "on_open_forum_thread_create",     # 用户创建主题时
    # "on_open_forum_thread_update",     # 用户修改主题时
    # "on_open_forum_thread_delete",     # 用户删除主题时
    # "on_open_forum_post_create",       # 用户创建帖子时
    # "on_open_forum_post_delete",       # 用户删除帖子时
    # "on_open_forum_reply_create",      # 用户回复评论时
    # "on_open_forum_reply_delete",      # 用户删除评论时
    # public_messages
    "on_group_at_message_create",  # 当收到群@机器人的消息时
    "on_c2c_message_create",  # 当收到c2c的消息时
    "on_group_add_robot",  # 机器人加入群聊
    "on_group_del_robot",  # 机器人退出群聊
    "on_group_msg_reject",  # 群聊拒绝机器人主动消息
    "on_group_msg_receive",  # 群聊接受机器人主动消息
    "on_friend_add",  # 用户添加机器人
    "on_friend_del",  # 用户删除机器人
    "on_c2c_msg_reject",  # 用户拒绝机器人主动消息
    "on_c2c_msg_receive",  # 用户接受机器人主动消息
]
