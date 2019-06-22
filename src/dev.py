import os, sys

def debug(*a, **kw):
  if is_verbose:
    print(*a, **kw)

verbose_req = os.environ.get('DEBUG_VERBOSE')
if isinstance(verbose_req, str) and verbose_req:
  verbose_req = verbose_req.lower()
  if verbose_req in ('false', 'no', 'off'):
    is_verbose = False
  else:
    is_verbose = True
else:
  is_verbose = False
debug('Running with verbose debugging')
