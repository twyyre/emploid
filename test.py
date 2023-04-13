from modules.portman.portman import Portman

pm = Portman()

pm.add_endpoint(_name="/", _content="<h1>hello world</h1>")
pm.serve(_port=4545, _debug=True)