import re
header_str, content_str = '^\[%s:(?P<value>\w+)\]\s*', '^(?P<head>[\w|-]+)\s*=\s*\'?(?P<tail>[\w|\-|\.|@|;|/|,|\:| ]+)\'?\s*'
class Config:
    def __del__(self):
        self.__particulars = None
        del(self.__particulars)

    def __init__(self, filename, type='[D|d]efault'):
        self.__particulars, header, holder = {}, '', {}
        try:
            c_file = open(filename, 'rb')
            lines = c_file.readlines()
            if len(lines):
                c_file.close()
                del(c_file)
                header_re, content_re = re.compile(header_str%type), re.compile(content_str)
                for line in lines:
                    try:
                        temp = header_re.search(line).group('value')
                        if holder and header and header != temp:self.__particulars[header] = holder
                        header, holder = temp, {}
                    except:
                        try:
                            c_head, c_tail = map(lambda v:content_re.search(line).group(v), ('head', 'tail'))
                            try:holder[c_head] += ', %s' % c_tail
                            except:holder[c_head] = c_tail
                        except:holder={}
                    else:self.__particulars[header] = holder
        except:pass

    def __call__(self):
        return self.__particulars
