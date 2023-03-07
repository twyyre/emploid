from modules.scribe.scribe import Scribe

scribe = Scribe()

scribe.new_page("emploid report")
scribe.scribble("{{rows}}", scribe.scribble_template)