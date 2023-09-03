# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime, timedelta

class ActionMoreInfoXuanHuongLake(Action):
    def name(self) -> Text:
        return "action_more_info_xuan_huong_lake"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # send some more information about Xuan Huong Lake
        dispatcher.utter_message(text="Hồ Xuân Hương là một hồ nước xinh đẹp nằm giữa lòng Đà Lạt. Đây là một địa điểm nổi tiếng đối với khách du lịch cũng như người dân địa phương, mang đến một bầu không khí yên bình và cảnh quan tuyệt đẹp.")
        
        return []

class ConversationCleanerMiddleware:
    def __init__(self):
        self.last_cleanup_time = datetime.now()

    def process_message(self, message, _):
        now = datetime.now()
        if (now - self.last_cleanup_time) > timedelta(minutes=1):
            # Code xóa các cuộc trò chuyện cũ ở đây
            self.last_cleanup_time = now
        return None