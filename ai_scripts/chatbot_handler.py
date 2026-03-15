class ChatbotUIHandler:
    def __init__(self):
        self.history = []

    def format_message(self, role, content):
        message = {"role": role, "content": content}
        self.history.append(message)
        return message

    def get_context(self):
        return self.history[-5:]