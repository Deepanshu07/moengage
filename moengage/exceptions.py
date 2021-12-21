class MoengageAPIException(Exception):
    def __init__(self, message):
        super().__init__(message)


class MoengageWrapperException(Exception):
    def __init__(self, message):
        super().__init__(message)
