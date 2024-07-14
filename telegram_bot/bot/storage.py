class UserInfoStorage:
    def __init__(self):
        self.user_id = None
        self.username = None
        self.phone_number = None

    def add(self, telegram_user_id, telegram_username, telegram_phone_number):
        self.user_id = telegram_user_id
        self.username = telegram_username
        self.phone_number = telegram_phone_number

    def data(self):
        return [self.user_id, self.username, self.phone_number]

    def clear_storage(self):
        self.user_id = None
        self.username = None
        self.phone_number = None


class TriggerStatusStorage:
    def __init__(self):
        self.stack = set()

    def add(self, trigger_status):
        self.stack.add(trigger_status)

    def clear(self):
        self.stack = set()

    def is_full(self):
        if len(self.stack) >= 3:
            return True
        else:
            return False

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def is_unique(self, trigger_status):
        if trigger_status in self.stack:
            return -1
        else:
            return 1

    def check_stack(self, trigger_status):
        if self.is_full():
            self.clear()
            return -1
        elif self.is_empty():
            self.add(
                trigger_status=trigger_status
            )
        elif self.is_unique(trigger_status=trigger_status) != -1:
            self.add(
                trigger_status=trigger_status
            )
        elif self.is_unique(trigger_status=trigger_status):
            return -1
