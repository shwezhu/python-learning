from message import messages
from message import with_user
from message import trim_last_two_messages

with_user('hello')
with_user('world')
with_user('foo')

print("main func, before trim:", messages, "id: ", id(messages))
trim_last_two_messages()
print("main func, after trim:", messages, "id: ", id(messages))

