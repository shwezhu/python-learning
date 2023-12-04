messages = []


def with_user(msg: str) -> None:
    messages.append(msg)


def trim_last_two_messages() -> None:
    global messages
    print("in trim func, before trim, len of messages:" + str(len(messages)), "id: ", id(messages))
    if len(messages) > 2:
        # use del messages[-2:] instead.
        messages = messages[:-2]
        print("in trim func, after trim, len of messages:" + str(len(messages)), "id: ", id(messages))


if __name__ == "__main__":
    pass
