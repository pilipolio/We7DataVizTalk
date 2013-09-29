from IPython.display import display, HTML, Javascript
import json

class HtmlScript(object):
    def __init__(self, div_id, js_lib=None):
        self.div_id = div_id
        self.js_lib = js_lib
        self.css_list = []
        self.vars = {}
        self.js = ['']
        self.html = ''

    def update_vars(self, **kw):
        # could do some (recursive) checking for keys and values here (as used to do convertVar)
        self.vars.update(**kw)
    
    def get_js_vars_lines(self):
        return ["var {0}={1};".format(k, json.dumps(pretty_floats(v))).replace("u'", "'") 
                for k,v in self.vars.iteritems()]

    def add_js(self, jsStr):
        if type(jsStr) != str:
           raise TypeError
        self.js.append(jsStr)

    def add_css(self, css):
        if type(css) != str:
           raise TypeError
        else:
            self.css_list.append(css)
       
    def get_html_only_lines(self):
        return ['<style>'] + self.css_list + ['</style>', '<div id="{div_id}">'.format(div_id=self.div_id), self.html, '</div>']

    def get_html_only(self):
        return '\n'.join(self.get_html_only_lines())

    def get_js(self):
        return '\n'.join(self.get_js_vars_lines() + self.js)
    
    def to_string(self):
        return '<script>\n' + self.get_js() + '</script>'

    def display(self):
        display(HTML(self.get_html_only()), Javascript(self.get_js(), lib=self.js_lib))

class PrettyFloat(float):
    """ As proposed here to handle arbitrary number of decimals.
    http://stackoverflow.com/questions/1447287/format-floats-with-standard-json-module
    """
    def __repr__(self):
        return '%.15g' % self
        
def pretty_floats(obj):
    if isinstance(obj, float):
        return PrettyFloat(obj)
    elif isinstance(obj, dict):
        return dict((k, pretty_floats(v)) for k, v in obj.items())
    elif isinstance(obj, (list, tuple)):
        return map(pretty_floats, obj)             
    return obj
