import os, sys, getopt, re, enum

def usage():
  print("pregex usage:")

def version():
  print("v0.1.0")
  
class Color(enum.Enum):
  black = 0
  red = 1
  green = 2
  yellow = 3
  blue = 4
  magenta = 5
  cyan = 6
  white = 7
  
__escape = "\x1b["
__fg = "1;3"
__end = "m"
__reset = __escape + __end

def pregex(pattern, color, colorVal):
  for line in sys.stdin:
    if line == '':
      break
    _line = line.strip(os.linesep)
    c = colorVal.value
    _sub = ""
    if color:
      _sub = pattern.sub(__escape + __fg + str(c) + __end + '\g<0>' + __reset, _line)
    else:
      _sub = pattern.sub('\g<0>', _line)
    print(_sub)

def main():
  try:
    opts, args = getopt.getopt(sys.argv[1:], "hve:ic:n", ["help", "version", "pattern=", "icase", "color=", "no-color="])
    pattern = None
    icase = False
    colorVal = Color.green
    color = True
    for o, a in opts:
      if o in ("-h", "--help"):
        usage()
        sys.exit()
      elif o in ("-v", "--version"):
        version()
        sys.exit()
      elif o in ("-e", "--pattern"):
        pattern = re.compile(str(a))
      elif o in ("-i", "--icase"):
        icase = True
      elif o in ("-c", "--color"):
        _c = str(a)
        for _color in Color:
          if _color.name == _c:
            colorVal = _color
            break
      elif o in ("-n", "--no-color"):
        color = False
    pregex(pattern, color, colorVal)
  except getopt.GetoptError as err:
    print(str(err))
    usage()
    sys.exit(1)


if __name__ == '__main__':
  main()
