import re, sys

pat = re.compile(r'([\u4e00-\u9fff々〇]+)')
src = open(sys.argv[1], encoding='utf-8').read()
out = pat.sub(r'{% ruby \1 ... %}', src)
open(sys.argv[1], 'w', encoding='utf-8').write(out)