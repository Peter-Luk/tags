se=('a','abbr','acronym','address','area','b','base','bdo','big','blockquote','body','br','button','caption','cite','code','col','colgroup','dd','del','dfn','div','dl','dt','em','fieldset','form','h1','h2','h3','h4','h5','h6','head','hr','html','i','iframe','img','input','ins','kbd','label','legend','li','link','map','meta','noscript','object','ol','optgroup','option','p','param','pre','q','samp','script','select','small','span','strong','style','sub','sup','table','tbody','td','textarea','tfoot','th','thead','title','tr','tt','ul','var')
de,fe=('applet','basefont','center','dir','font','isindex','menu','s','strike','u'),('frame','frameset','noframes')
da={'align':('caption','applet','iframe','img','input','object','legend','table','hr','div','h1','h2','h3','h4','h5','h6','p')}
sa,fa={'abbr':('td','th')},{'cols':('frameset',)}

sa['accept-charset'],sa['accept'],sa['action']=('form',),('form','input'),('form',)
sa['accesskey']=('a','area','button','input','label','legend','textarea')
sa['align']=('col','colgroup','tbody','td','tfoot','th','thead','tr')
sa['alt'],sa['archive'],sa['axis']=('area','img','input'),('object',),('td','th')
for item in ('border','cellpadding','cellspacing'):sa[item]=('table',)
sa['char']=('col','colgroup','tbody','td','tfoot','th','thead','tr')
sa['charoff']=('col','colgroup','tbody','td','tfoot','th','thead','tr')
sa['charset'],sa['checked']=('a','link','script'),('input',)
sa['cite']=('blockquote','q','del','ins')
for item in ('classid','codebase','codetype'):sa[item]=('object',)
sa['cols'],sa['colspan'],sa['content']=('textarea',),('td','th'),('meta',)
sa['coords'],sa['data'],sa['datetime']=('a','area'),('object',),('del','ins')
sa['disabled']=('button','input','optgroup','option','select','textarea')
sa['declare'],sa['defer'],sa['enctype']=('object',),('script',),('form',)
sa['for'],sa['frame'],sa['headers']=('label',),('table',),('td','th')
sa['height'],sa['href']=('img','object'),('a','area','base','link')
sa['hreflang'],sa['http-equiv'],sa['ismap']=('a','link'),('meta',),('img','input')
sa['label'],sa['longdesc'],sa['maxlength']=('option',),('img',),('input',)
sa['media'],sa['method'],sa['multiple']=('style','link'),('form',),('select',)
sa['name']=('button','textarea','select','img','a','input','object','map','param','meta')
sa['nohref'],sa['onchange']=('area',),('input','select','textarea')
for item in ('onblur','onfocus'):sa[item]=('a','area','button','input','label','select','textarea')
sa['onload'],sa['onreset'],sa['onselect']=('body',),('form',),('input','textarea')
sa['onsubmit'],sa['onunload'],sa['profile']=('form',),('body',),('head',)
sa['readonly'],sa['rel'],sa['rev']=('input','textarea'),('a','link'),('a','link')
sa['rows'],sa['rowspan'],sa['rules']=('textarea',),('td','th'),('table',)
sa['scheme'],sa['scope'],sa['selected']=('meta',),('td','th'),('option',)
sa['shape'],sa['size'],sa['span']=('a','area'),('input','select'),('col','colgroup')
sa['src'],sa['standby'],sa['summary']=('img','input','script'),('object',),('table',)
sa['tabindex']=('a','area','button','input','object','select','textarea')
sa['type']=('a','link','object','param','script','style','input','button')
sa['valign']=('col','colgroup','tbody','td','tfoot','th','thead','tr')
sa['usemap'],sa['value']=('img','input','object'),('input','option','param','button')
sa['valuetype'],sa['width']=('param',),('col','colgroup','img','object','table')

da['alink'],da['alt'],da['archive']=('body',),('applet',),('applet',)
da['background'],da['bgcolor']=('body',),('table','tr','td','th','body')
da['border'],da['clear'],da['code']=('img','object'),('br',),('applet',)
da['compact']=('dir','dl','menu','ol','ul')
da['codebase'],da['color'],da['face']=('applet',),('basefont','font'),('basefont','font')
da['height'],da['hspace']=('applet','iframe','td','th'),('applet','img','object')
da['language'],da['link'],da['name']=('script',),('body',),('applet',)
da['noshade'],da['nowrap'],da['object']=('hr',),('td','th'),('applet',)
da['prompt'],da['size']=('isindex',),('basefont','font','hr')
da['start'],da['target']=('ol',),('a','area','base','form','link')
da['text'],da['type'],da['value']=('body',),('li','ol','ul'),('li',)
da['version'],da['vlink'],da['vspace']=('html',),('body',),('applet','img','object')
da['width']=('applet','iframe','pre','td','th')

for item in ('frameborder','longdesc','marginheight','marginwidth','name','scrolling','src'):fa[item]=('frame','iframe')
fa['noresize']=('frame',)
for item in ('onload','onunload','rows'):fa[item]=('frameset',)

exlist=('base','head','html','meta','script','style','title')
sa['id']=tuple(filter(lambda v:v not in exlist,se))
da['id']=tuple(filter(lambda v:v not in exlist,de))
fa['id']=tuple(filter(lambda v:v not in exlist,fe))
exlist=('base','basefont','head','html','meta','param','script','title')
sa['title']=tuple(filter(lambda v:v not in exlist,se))
da['title']=tuple(filter(lambda v:v not in exlist,de))
fa['title']=tuple(filter(lambda v:v not in exlist,fe))
exlist=('applet','base','basefont','br','frame','frameset','iframe','param','script')
for item in ('dir','lang'):
    sa[item]=tuple(filter(lambda v:v not in exlist,se))
    da[item]=tuple(filter(lambda v:v not in exlist,de))
    fa[item]=tuple(filter(lambda v:v not in exlist,fe))
exlist=('base','basefont','head','html','meta','param','script','style','title')
for item in ('class','style'):
    sa[item]=tuple(filter(lambda v:v not in exlist,se))
    da[item]=tuple(filter(lambda v:v not in exlist,de))
    fa[item]=tuple(filter(lambda v:v not in exlist,fe))
exlist=('applet','base','basefont','bdo','br','font','frame','frameset','head','html','iframe','isindex','meta','param','script','style','title')
for item in ('onclick','ondblclick','onkeydown','onkeypress','onkeyup','onmousedown','onmousemove','onmouseout','onmouseover','onmouseup'):
    sa[item]=tuple(filter(lambda v:v not in exlist,se))
    da[item]=tuple(filter(lambda v:v not in exlist,de))
    fa[item]=tuple(filter(lambda v:v not in exlist,fe))
def tag_attrs(attrs):
    holder={}
    for i in attrs.keys():
        for j in attrs[i]:
            try:holder[j]+=(i,)
            except:holder[j]=(i,)
    return holder
element={'strict':tag_attrs(sa)}
element['loose'],element['frameset']=tag_attrs(da),tag_attrs(fa)
if __name__=='__main__':
    print(element['loose']['td'])
