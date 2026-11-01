import json,zipfile,xml.etree.ElementTree as ET, pathlib, re
p=pathlib.Path(__file__).resolve().parent/'RAJ_GROUP_Party_Master.xlsx'
n={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with zipfile.ZipFile(p) as z:
 ss=[]
 if 'xl/sharedStrings.xml' in z.namelist():
  root=ET.fromstring(z.read('xl/sharedStrings.xml'))
  ss=[''.join(x.itertext()) for x in root.findall('m:si',n)]
 def rows(sheet):
  root=ET.fromstring(z.read(f'xl/worksheets/sheet{sheet}.xml'))
  for row in root.findall('.//m:sheetData/m:row',n):
   vals={}
   for c in row.findall('m:c',n):
    col=re.match('[A-Z]+',c.attrib['r']).group();v=c.find('m:v',n)
    if c.attrib.get('t')=='inlineStr':val=''.join(c.find('m:is',n).itertext())
    elif v is not None:val=ss[int(v.text)] if c.attrib.get('t')=='s' else v.text
    else:val=''
    vals[col]=(val or '').strip()
   yield vals
 life={};guj={};cities={}
 for r in list(rows(1))[1:]:
  a=r.get('A','').lower();b=r.get('B','')
  if a and b:life[a]=b
 for r in list(rows(2))[1:]:
  a=r.get('A','').lower();b=r.get('B','');c=r.get('C','')
  if a and b:guj[a]=b
  if a and c:cities[a]=c
 out={'life':life,'gujarati':guj,'cities':cities}
 (p.parent/'master-data.json').write_text(json.dumps(out,ensure_ascii=False,separators=(',',':')),encoding='utf-8')
 print(f'Master generated: {len(life)} mappings, {len(guj)} Gujarati, {len(cities)} cities')
