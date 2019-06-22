import os, sys

def debug(*a, **kw):
  if is_verbose:
    print(*a, **kw)

is_verbose = os.environ.get('DEBUG_VERBOSE')
if isinstance(is_verbose, str):
  verbose_req = is_verbose.lower()
  if verbose_req in ('false', 'no', 'off'):
    is_verbose = False
elif is_verbose is None and sys.stdout.isatty():
  is_verbose = True
debug('Running with verbose debugging')
