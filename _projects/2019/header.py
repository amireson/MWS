import glob

x=glob.glob('*.md')

for fn in x:
    filecontents=open(fn,'r').readlines()
    if fn[:4]=='home':
        h=['---\n','author: \n','year: 2019 \n', 'title: \n']
        h=h+['<img src="{{site.baseurl}}/images/MWS_logo_notext.png" align="right" width=90px>\n']
        filecontents=h+filecontents
    else:   
        filecontents=['---\n','---\n','\n']+filecontents
    out=open(fn,'w')
    for line in filecontents: out.write(line)
    out.close()

