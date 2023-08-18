# -*- coding: utf-8 -*-


class LazyAdminConfig:
    template_folder = "templates"


class LazyAdmin:
    """
    LazyAdmin initializer. If config is None, default config will be used.

    :param config: LazyAdminConfig

    :return: None
    """

    config: LazyAdminConfig

    def __init__(self, config: LazyAdminConfig | None):
        self.config = config or LazyAdminConfig()
