import sys,re
idx,full=sys.argv[1:3]
I=open(idx,encoding='utf8').read().split('\n'); F=open(full,encoding='utf8').read().split('\n')
# full: line->(name,heading path)
fl={};h={};cur={}
for n,l in enumerate(F,1):
    m=re.match(r'(#+) (.*)',l)
    if m: cur[len(m.group(1))]=l; [cur.pop(k) for k in list(cur) if k>len(m.group(1))]
    elif l.startswith('- '):
        fl[n]=(l[2:], tuple(cur[k] for k in sorted(cur)))
cur={};il={};bad=0
for n,l in enumerate(I,1):
    m=re.match(r'(#+) (.*)',l)
    if m: cur[len(m.group(1))]=l; [cur.pop(k) for k in list(cur) if k>len(m.group(1))]; continue
    if not l.startswith('- '): continue
    m=re.match(r'- (.+) \| (\d+)$',l)
    if not m: print('IDX bad',n,l[:80]); continue
    name,ln=m.group(1),int(m.group(2))
    if ln in il: print('IDX dup line',ln,name,il[ln])
    il[ln]=name
    if ln not in fl: print('IDX->nonentry',n,name,ln); continue
    t,hp=fl[ln]
    if not (t==name or t.startswith(name+': ')): print('NAME mismatch idx',n,repr(name),'full',ln,repr(t[:50]))
    if hp[-1:]!=tuple(cur[k] for k in sorted(cur))[-1:]: print('HEAD mismatch',n,name,ln,hp[-1:], [cur[k] for k in sorted(cur)][-1:])
for ln,(t,_) in fl.items():
    if ln not in il: print('NOT INDEXED',ln,t[:60])
print(len(fl),len(il))
