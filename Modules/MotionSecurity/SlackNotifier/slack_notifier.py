from slackclient import SlackClient


class SlackNotifier:
    def __init__(self, slack_token, channel_name, bot_name="Motion Security Bot"):

        self.bot_name = bot_name
        self.channel_name = channel_name
        self.slack_token = slack_token
        self.slack_client = SlackClient(self.slack_token)

    def send_notification(self, message):
        self.slack_client.api_call('chat.postMessage', text=message, channel=self.channel_name, username=self.bot_name,
                                   icon_emoji=":robot_face:")
