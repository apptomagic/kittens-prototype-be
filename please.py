"""
Glorified shell script to set up stuff needed to run the service
"""

import os
os.environ['TZ'] = 'UTC'

import argparse
import pkg_resources
import re
import shutil
import subprocess
import sys
import time

PROTOS = [
  'post',
  'conversation',
  'topic',
]


def install_deps(config):
  # The pip docs specifically tell us not to do this… but IRL we can't trust our PATH in a cross-platform way, and we want to minimize upfront setup on  developer machines since this prototype is a temporary artifact
  from pip._internal import main as pip
  pip(['install', '-r', 'requirements.txt'])


def install_test_deps(config):
  # The pip docs specifically tell us not to do this… but IRL we can't trust our PATH in a cross-platform way, and we want to minimize upfront setup on  developer machines since this prototype is a temporary artifact
  from pip._internal import main as pip
  pip(['install', '-r', 'kittens-api/bdd/behave/requirements.txt'])


local_import_re = re.compile(r"import (.*_pb2) as (.*__pb2)")
pkg_local_import_re = re.compile(r"from (.*) import (.*_pb2) as (.*__pb2)")
def copy_and_fix_imports(filename, pkg = ''):
  with open("src/{}".format(filename)) as f_in:
    with open ("kittens-api/bdd/behave/features/client/{}".format(filename), "w") as f_out:
      for line in f_in:
        match = pkg_local_import_re.match(line)
        if match:
          i_pkg, i_mod, i_name = match.groups()
          if i_pkg == pkg:
            f_out.write("from . import {} as {}\n".format(i_mod, i_name))
          elif i_pkg.startswith("google"):
            f_out.write(line)
          else:
            f_out.write("from ..{} import {} as {}\n".format(i_pkg, i_mod, i_name))
        else:
          match = local_import_re.match(line)
          if match:
            i_mod, i_name = match.groups()
            if pkg:
              f_out.write("from .. import {} as {}\n".format(i_mod, i_name))
            else:
              f_out.write("from . import {} as {}\n".format(i_mod, i_name))
          else:
            f_out.write(line)

def build_proto(config):
  from grpc_tools.protoc import main

  proto_include = pkg_resources.resource_filename("grpc_tools", "_proto")

  args = [
    "protoc", # first one is ignored, as it would normally be sys.argv[0]
    "--python_out=./src",
    "--grpc_python_out=./src",
    # proto files go here,
    "--proto_path=" + proto_include,
    "--proto_path=" + config.path,
  ]
  args[3:3] = [config.path + "/" + proto + ".proto" for proto in PROTOS]
  print(args)
  res = main(args)

  if res: sys.exit(res)

  # copy generated files to kittens-api but fix imports
  for proto in PROTOS:
    copy_and_fix_imports("{}_pb2.py".format(proto))
    copy_and_fix_imports("{}_pb2_grpc.py".format(proto))


def serve(config):
  subprocess.run(['python', './src/prototype_service.py'])

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='One-stop script for managing the service')
  subparsers = parser.add_subparsers(help='sub-command help')

  cmdparser = subparsers.add_parser('deps', help='Install dependencies')
  cmdparser.set_defaults(func=install_deps)
  cmdparser = subparsers.add_parser('test-deps', help='Install test dependencies')
  cmdparser.set_defaults(func=install_test_deps)
  cmdparser = subparsers.add_parser('proto', help='Build Python files from protobuf definitions')
  cmdparser.set_defaults(func=build_proto)
  cmdparser.add_argument('path', nargs='?', default='./kittens-api/proto')
  cmdparser = subparsers.add_parser('serve', help='Run server')
  cmdparser.set_defaults(func=serve)

  args = parser.parse_args()
  try:
    args.func(args)
  except KeyboardInterrupt:
    pass
