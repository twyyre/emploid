
class Scribe:

    def __init__(self):
        import tools
        self.tl = tools
        self.internal_path = "logs/"
        self.relative_path = True
        self.f = None

    def new_page(self, _filename: str, _type: str=".html"):
        self.tl.f_write(_filename=_filename)
        self.f = _filename
        return self.f
    
    def scribe(self, _content):
        self.tl.f_write(_filename=self.f, _content=_content)

    def record(self, _content):
        pass

    def recall(self, _filename):
        self.f = self.tl.f_read(_filename=_filename)

    def modify(self, _filename, _content):
        self.f = self.tl.f_read(_filename=_filename)

    def scribble(self, _content):
        pass

    
    
