from os import linesep
from .html401 import element
class Tag(type):
    def __call__(cls):
        try:print(cls.__value)
        except:pass
    def ___del__(cls):
        super(Tag,cls).__del__()
        cls.__value=None
        del(cls.__value)
    def __init__(cls,name,base,dict):
        global linesep
        if name=='a':linesep=''
        try:
            if dict['compression']:linesep='\r\n'
        except:dict['compression']=None
        if ('tags' in dict) and not(name in dict['tags']):pass
        else:
            cls.__value='<%s'%name
            try:
                for k,v in dict['attributes'].items():cls.__value=' '.join((cls.__value,'%s="%s"'%(k,v)))
            except:pass
            try:
                if dict['content']:
                    if not(list(dict['content'])):dict['content']=[dict['content']]
                    cls.__value=''.join((cls.__value,'>%s'%linesep))
                    for item in dict['content']:cls.__value=''.join((cls.__value,'%s%s'%(item,linesep)))
                    if ('singleton' in dict) and not(name in dict['singleton']):cls.__value=''.join((cls.__value,'</%s>'%name))
            except:
                if ('singleton' in dict) and (name in dict['singleton']):cls.__value=''.join((cls.__value,'>'))
                else:cls.__value=' '.join((cls.__value,'/>'))
        super(Tag,cls).__init__(name,base,dict)
    def __new__(cls,name,base,dict):
        try:dict['compression']
        except:dict['compression']=None
        try:dict['dtd_type']
        except:dict['dtd_type']='strict'
        if not(dict['dtd_type'] == 'loose' or name in element['strict'].keys()):
            if name in element['frameset'].keys():dict['dtd_type']='frameset'
            elif name in element['loose'].keys():dict['dtd_type']='loose'
        attrslist=()
        try:attrslist+=element['strict'][name]
        except:pass
        try:attrslist+=element['frameset'][name]
        except:pass
        try:
            for item in dict['attributes'].keys():
                if item not in attrslist:
                    if item in element['loose'][name]:dict['dtd_type']='loose'
                    else:del(dict['attributes'][item])
        except:pass
        return type.__new__(cls,name,base,dict)
    def __str__(cls):
        if cls.__value:return cls.__value
