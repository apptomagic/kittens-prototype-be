posts = {'': []}


class IterWithContext(object):
  def __init__(self, collection, context):
    self.collection = collection
    self.contexts = ['']
    for md in context.invocation_metadata():
      if md.key == 'use-data-contexts':
        self.contexts = md.value.split('+')
  
  def __iter__(self):
    # for now we only support one context, as more than one will complicate things
    # with regards to sorting and duplicates/cow
    for item in self.collection[self.contexts[0]]:
      yield item

class Pager(object):
  def __init__(self, request):
    self.after = request.after
    self.since = request.since.ToNanoseconds()
    self.seen = not self.after
  
  def __call__(self, post):
    if self.since > post.created.ToNanoseconds(): return False
    if self.after:
      if self.seen:
        return True
      if post.id == self.after:
        self.seen = True
        return False
      return False
    return True
