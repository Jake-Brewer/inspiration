import re,glob,os,sys
SP=sys.argv[1]
for d in sorted(glob.glob(SP+'/g/*/')):
    cat=os.path.basename(d.rstrip('/'))
    files=sorted(glob.glob(d+'s*.md'))+sorted(glob.glob(d+'g*.md'))
    if not files: continue
    title=cat.replace('_',' ').title()
    F=[f'# {title} Compendium (Full)','',f'Each item: `Name: description`, one per line. Index line numbers in {cat}_index.md must match this file; regenerate the index after any insertion.','']
    seen=set();drop=0
    for f in files:
        for l in open(f,encoding='utf8').read().split('\n'):
            l=l.rstrip()
            if not l: continue
            if l.startswith('#'):
                if l.startswith('# '): continue
                F.append(l); continue
            m=re.match(r'- ([^:]+): (.{20,})$',l)
            if not m or m.group(1).lower() in seen: drop+=1; continue
            seen.add(m.group(1).lower()); F.append(l)
    # drop headings with no entries
    G=[]
    for i,l in enumerate(F):
        if l.startswith('##'):
            nxt=next((x for x in F[i+1:] if x.startswith('#') or x.startswith('- ')),'')
            if not nxt.startswith('- ') and not(l.startswith('## ') and nxt.startswith('###')): continue
        G.append(l)
    F=G
    open(f'{cat}_full.md','w',encoding='utf8').write('\n'.join(F)+'\n')
    idx=[f'# {title} (index)','',f'Each line: `Name | line number in {cat}_full.md`. Open {cat}_full.md at that line for the description.','']
    for n,l in enumerate(F,1):
        if l.startswith('##'):
            if idx[-1]!='': idx.append('')
            idx+=[l,'']
        elif l.startswith('- '): idx.append(f"- {l[2:].split(': ')[0]} | {n}")
    open(f'{cat}_index.md','w',encoding='utf8').write('\n'.join(idx)+'\n')
    print(cat,len(files),'files',len(seen),'entries','dropped',drop)
