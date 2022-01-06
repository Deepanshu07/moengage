import requests
from requests.auth import HTTPBasicAuth
from moengage.exceptions import MoengageAPIException, MoengageWrapperException


class Moengage:
    def __init__(self, base_url, app_id, api_key):
        self.moengage_base_url = base_url
        self.app_id = app_id
        self.api_key = api_key
        self.auth = HTTPBasicAuth(self.app_id, self.api_key)
        self.headers = {
            "MOE-APPKEY": self.app_id,
        }

    def create_or_update_user(self, auth_id, name=None, phone_number=None, email=None, **kwargs):
        try:
            data = {
                "type": "customer",
                "customer_id": auth_id,
                "attributes": {
                }
            }
            if name is not None:
                data["attributes"]['name'] = name
            if phone_number is not None:
                data["attributes"]['mobile'] = phone_number
            if email is not None:
                data["attributes"]['email'] = email
            for key, val in kwargs.items():
                data["attributes"][key] = val
            response = requests.post(
                self.moengage_base_url + "/v1/customer/{}".format(self.app_id),
                auth=self.auth,
                headers=self.headers,
                json=data,
            )
            response_json = response.json()
            if response_json["status"] == "fail":
                raise MoengageAPIException(response_json["error"]["message"])
        except MoengageAPIException as e:
            raise e
        except Exception as e:
            raise MoengageWrapperException("moengage wrapper internal error")
        return

    def publish_event(self, auth_id, event_name, **kwargs):
        try:
            data = {
                "type": "event",
                "customer_id": auth_id,
                "actions": [{
                    "action": event_name,
                    "attributes": {},
                    "user_timezone_offset": 19800,
                },
                ]
            }
            for key, val in kwargs.items():
                data["actions"][0]["attributes"][key] = val
            response = requests.post(
                self.moengage_base_url + "/v1/event/{}".format(self.app_id),
                auth=self.auth,
                headers=self.headers,
                json=data,
            )
            response_json = response.json()
            if response_json["status"] == "fail":
                raise MoengageAPIException(response_json["error"]["message"])
        except MoengageAPIException as e:
            raise e
        except Exception as e:
            raise MoengageWrapperException("moengage wrapper internal error")
        return
