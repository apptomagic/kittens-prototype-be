class Pager(object):
  def __init__(self, collection, request):
    self.collection = collection
    self.after = request.after
    self.since = request.since.ToNanoseconds()
    self.seen = not self.after
  
  def __call__(self, item):
    if self.since > item.created.ToNanoseconds(): return False
    if self.after:
      if self.seen:
        return True
      if item.id == self.after:
        self.seen = True
        return False
      return False
    return True


class Collection(dict):
  def __init__(self):
    self.indexes = {}
    self.clear_all()

  def clear_all(self):
    self.clear()
    self[''] = []
    self.indexes[''] = {}
    
  def get_contexts(self, context):
    contexts = ['']
    for md in context.invocation_metadata():
      if md.key == 'use-data-contexts':
        contexts = md.value.split('+')
    return [ctx for ctx in contexts if ctx in self] or ['']

  def iter_with_context(self, context):
    # for now we only support one context, as more than one will complicate things
    # with regards to sorting and duplicates/cow
    for item in self[self.get_contexts(context)[0]]:
      yield item
  
  def pager(self, request):
    return Pager(self, request)
  
  def append(self, item, context):
    self[self.get_contexts(context)[0]].append(item)
  
  def get_one(self, id, context):
    for ctx in self.get_contexts(context):
      if id in self.indexes[ctx]:
        return self.indexes[ctx][id]
    raise KeyError(id)
  
  def populate(self, name, content):
    self[name] = list(content)
    self.indexes[name] = {}
    for item in self[name]:
      self.indexes[name][item.id] = item


posts = Collection()
conversations = Collection()

topics = [
  'chat',
  'introductions',
  'meta',
  'roadmap',
  'bugs',
  'suggestions',
  'help',
  'dev-help',
  'announcements',
  'documentation',
  'web',
]

related = [
  ('bugs', 'suggestions'),
  ('chat', 'introductions'),
  ('roadmap', 'announcements'),
  ('help', 'bugs'),
  ('help', 'documentation'),
  ('dev-help', 'documentation'),
  ('documentation', 'web'),
]
