#!/usr/bin/env python3
"""Static TeX reference and dependency checker; not a mathematical proof."""
from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
seen={}
def visit(name):
    p=root/name
    if name in seen:return
    s=re.sub(r'(?<!\\)%[^\n]*','',p.read_text(encoding='utf8'))
    seen[name]=s
    for u in re.findall(r'\\input\{([^}]+)\}',s):
        visit(u if u.endswith('.tex') else u+'.tex')
visit('papers/nc-cubic-unmark.tex')
s='\n'.join(seen.values())
labels=re.findall(r'\\label\{([^}]+)\}',s)
refs=re.findall(r'\\(?:eqref|ref|pageref|autoref)\{([^}]+)\}',s)
bib=re.findall(r'\\bibitem\{([^}]+)\}',s)
cites=[x.strip() for a in re.findall(r'\\cite(?:\[[^]]*\])*\{([^}]+)\}',s) for x in a.split(',')]
assert len(labels)==len(set(labels)),'duplicate label'
assert len(bib)==len(set(bib)),'duplicate bibliography'
assert not set(refs)-set(labels),set(refs)-set(labels)
assert not set(cites)-set(bib),set(cites)-set(bib)
assert (root/'computations/verify_marking_lattice.py').is_file()
print(f"PASS: {len(seen)} TeX sources, {len(labels)} labels, {len(refs)} refs, {len(bib)} bib entries, {len(cites)} citations")
