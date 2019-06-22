import json

class User: pass

def get_user_from_context(context):
  user = User()
  for md in context.invocation_metadata():
    if md.key == 'authenticated-user':
      data = json.loads(md.value)
      user.id = data['id']
      if data.get('displayName'):
        user.displayName = data['displayName']
      else:
        user.displayName = user.id
      return user
