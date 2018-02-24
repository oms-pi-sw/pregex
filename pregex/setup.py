from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

base = 'Console'

executables = [
    Executable('pregex.py', base=base)
]

setup(name='pregex',
      version = '0.1.0',
      description = 'regex matcher',
      options = dict(build_exe = buildOptions),
      executables = executables)
