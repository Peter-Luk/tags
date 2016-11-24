from .tag import Tag
from .html401 import element
from .config import Config
dtd_type,tagList=[],()
for item in ('strict','loose','frameset'):tagList+=tuple(element[item].keys())
noEnd=('area','base','basefont','br','colgroup','frame','hr','img','input','isindex','link','meta','param')
for item in tagList:
    exec("""
class %sTag:
    def __call__(self):
        self.__Tag()
    def __del__(self):
        self.dtd_type=self.__Tag=self.__value=None
        del(self.dtd_type)
        del(self.__Tag)
        del(self.__value)
    def __init__(self,value):
        self.__value=value
        self.__value['tags']=tagList
        self.__value['singleton']=noEnd
        self.__Tag=Tag('%s',(),self.__value)
        self.dtd_type=self.__Tag.dtd_type
    def __str__(self):
        return self.__Tag._Tag__value
"""%(item,item))
for item in tagList:
    if item in noEnd:
        exec("""
class %s:
    def __call__(self):
        self.__Tag()
    def __del__(self):
        self.__Tag=self.dtd_type=None
    def __init__(self,attrs,compression=None):
        self.__Tag=%sTag({'attributes':attrs,'compression':compression})
        dtd_type.append(self.__Tag.dtd_type)
    def __str__(self):
        return str(self.__Tag)
"""%(item.upper(),item))
    else:
        exec("""
class %s:
    def __call__(self):
        self.__Tag()
    def __del__(self):
        self.__Tag=self.dtd_type=None
    def __init__(self,content,attrs={},compression=None):
        if str(content):content=[content]
        try:dtd_type.extend([v.dtd_type for v in content])
        except:pass
        self.__Tag=%sTag({'content':content,'attributes':attrs,'compression':compression})
        dtd_type.append(self.__Tag.dtd_type)
    def __str__(self):
        return str(self.__Tag)
"""%(item.upper(),item))
class GeMETA(META):
    def __call__(self):
        try:return self.content
        except:pass

    def __del__(self):
        self.content = None
        del(self.content)

    def __init__(self,basic,advance=None):
        try:
            if advance:self.content=self.proceed(self.__process_multiple({'original':basic,'extra':advance}))
            else:self.content=self.proceed(basic['Meta'])
        except:pass

    def proceed(self,data,exemption=('keywords','description','Expires','Language','Owner','Rating','Robots')):
        holder = []
        try:
            for k, v in data.items():
                if v:
                     try:
                         if int(v):
                             if k in exemption:holder.append(META({'name':k, 'content':v}))
                             else:holder.append(META({'http-equiv':k, 'content':v}))
                     except:
                         if k in exemption:holder.append(META({'name':k, 'content':v}))
                         else:holder.append(META({'http-equiv':k, 'content':v}))
            return holder
        except:pass

    def __process_multiple(self,data):
        holder = {}
        try:
            for ke, ve in data['extra']['Meta'].items():
                for ko, vo in data['original']['Meta'].items():
                    if vo:
                        try:
                            if int(vo):holder[ko] = vo
                        except:holder[ko] = vo
                    if ke == ko:
                        if ve:
                            try:
                                if int(ve):holder[ke] = ve
                                else:del(holder[ke])
                            except:holder[ke] = ve
            return holder
        except:pass
def doc_type4_1(lang='EN'):
    holder,version,doc_string='','4.01','<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML %s//%s" "http://www.w3.org/TR/%s.dtd">'
    if 'loose' in dtd_type:holder=doc_string%('%s %s'%(version,'Transitional'),lang,'1999/REC-html401-19991224/%s'%'loose')
    elif 'frameset' in dtd_type:holder=doc_string%('%s %s'%(version,dtd_type.capitalize()),lang,'1999/REC-html401-19991224/%s'%'frameset')
    else:holder=doc_string%(version,lang,'html4/%s'%'strict')
    print(holder)
def form(uri,trs=None,cols=2,submit_name=None):
    attrs={'type':'submit'}
    if submit_name:attrs['name']=submit_name
    holder=TR(TD(INPUT(attrs),{'colspan':cols,'style':'text-align:center'}))
    try:
        if not(0 in [isinstance(v,TR) for v in trs]):
            trs.append(holder)
            holder=trs
    except:pass
    return FORM(TABLE(holder,{'border':0}),{'action':uri,'method':'post'})
def label_input(name,value=None,alternative=None,pre=None,post=None,input_type='text'):
    attrs,holder={'type':input_type,'name':name,'style':'text-align:right'},name
    if value:attrs['value']=value
    if alternative:holder=alternative
    content=[INPUT(attrs)]
    if pre:content.insert(0,LABEL(pre,{'style':'color:purple'}))
    if post:content.append(LABEL(post,{'style':'color:purple'}))
    return [TD(LABEL('%s:'%holder.capitalize(),{'style':'color:blue;font-weight:bold','for':name}),{'style':'text-align:right'}),TD(content)]
def label_select(name,value,select=None,alternative=None):
    try:
        options,holder=[],value.keys()
        holder.sort()
        for item in holder:
            attrs={'value':value[item]}
            if item==select:attrs['selected']='selected'
            options.append(OPTION(item,attrs))
        holder=name
        if alternative:holder=alternative
        return [TD(LABEL('%s:'%holder.capitalize(),{'style':'color:blue;font-weight:bold','for':name}),{'style':'text-align:right'}),TD(SELECT(options,{'name':name}))]   
    except:pass
class Webpage(A,BODY,DIV,HEAD,GeMETA,HTML,INPUT,LABEL,META,OPTION,SELECT,TABLE,TD,TITLE,TR):
    def __call__(self):
        return self.page(self.__content,self.__title,self.__body_attributes,self.footer())
    def __del__(self):
        self.__config=self.__metas=self.__content=self.__title=self.__body_attributes=None
        del(self.__config)
        del(self.__metas)
        del(self.__content)
        del(self.__title)
        del(self.__body_attributes)
    def __init__(self,content,title,body_attrs=None,config_file='',status=None):
        if config_file:
            from config import Config
            self.__config=Config(config_file)()
            self.__metas=GeMETA(self.__config)()
            if status:self.__metas=GeMETA(self.__config,Config(config_file,status)())()
        self.__content,self.__title,self.__body_attributes=content,title,body_attrs
    def copyright(self, colspan=2):
        if colspan:return TR(TD('&copy; MMIV, all rights reserved.', {'colspan':colspan, 'style':'text-align:center;font-size:75%'}))
        return TR(TD('&copy; MMIV, all rights reserved.', {'style':'text-align:center;font-size:75%'}))
    def footer(self):
        try:
            company = self.__config['Company']
            trs = [TR([TD('%(address)s'%company, {'colspan':2, 'style':'text-align:center'})])]
            tds = [TD([DIV('Phone : %s'%', '.join(['(852)-%s'%v for v in [company['phone']]])), DIV(['email : ', A(company['email'], {'href':'mailto:%(email)s'%company})])])]
            tds.append(TD([DIV('Facsimile : %s'%', '.join(['(852)-%s'%v for v in [company['facsimile']]])), DIV(['Homepage : ', A(company['homepage'], {'href':'http://%(homepage)s/index.spy'%company})])], {'style':'text-align:right;font-weight:bold'}))
            trs.extend([TR(tds, {'style':'font-size:75%'}), self.copyright()])
            return TABLE(trs, {'border':0, 'width':'100%'})
        except:pass
    def page(self,content,title=None,body_attrs={},footer=None,compression=None):
        tlTag=TITLE(title,compression=compression)
        holder=[]
        try:
            if str(self.__metas):self.__metas=[self.__metas]
            holder.extend(list(filter(lambda v:isinstance(v,META),self.__metas)))
        except:pass
        holder.append(tlTag)
        for item in holder:
            try:dtd_type.append(item.dtd_type)
            except:pass
        hdTag=HEAD(holder,compression=compression)
        if str(content):content=[content]
        if footer:content.append(footer)
        for item in content:
            try:dtd_type.append(item.dtd_type)
            except:pass
        try:bdTag=BODY(content,body_attrs,compression)
        except:pass
        for item in (hdTag,bdTag):
            try:dtd_type.append(item.dtd_type)
            except:pass
        hTag=HTML([hdTag,bdTag],compression=compression)
        doc_type4_1()
        print("<!-- No direct modification required -->")
        hTag()
