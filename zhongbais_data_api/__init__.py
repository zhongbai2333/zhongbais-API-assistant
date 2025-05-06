class zbDataAPI(object):
    @staticmethod
    def get_player_info() -> dict:
        """
        获取玩家信息字典

        Returns:
            dict: 玩家信息
        """
        pass

    @staticmethod
    def register_player_info_callback(func: function) -> dict:
        """
        注册回调函数，在player_info发生变化的时候触发

        Args:
            func (function): 回调函数接口
        Returns:
            dict: 玩家信息
        """
        pass

    @staticmethod
    def get_player_list() -> list:
        """
        获取在线玩家列表

        Returns:
            list: 玩家列表
        """
        pass

    @staticmethod
    def register_player_list_callback(func: function) -> list:
        """
        注册回调函数，在player_list发生变化的时候触发

        Args:
            func (function): 回调函数接口
        Returns:
            list: 玩家列表
        """
        pass

    @staticmethod
    def refresh_getpos() -> None:
        """
        手动刷新player_info
        """
        pass
