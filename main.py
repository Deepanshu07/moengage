from moengage.wrapper import Moengage


def print_hi(name):
    print(f'Hi, {name}')


def test_create_user(moengage):
    moengage.create_or_update_user("12346", "testNameNew", "8920841864")


def test_publish_event(moengage):
    mo.publish_event("12346", "test_event_1", prop_1="prop1_val2", prop_2="prop2_val2")


if __name__ == '__main__':
    # print_hi('PyCharm')
    mo = Moengage("https://api-03.moengage.com", "5UQZMM1CD3E1XU2B5FG7AKEI_DEBUG", "XKFoic6P6MqAdC7FkjhmaEwN")
    test_create_user(mo)
    test_publish_event(mo)


