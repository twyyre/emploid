import os
import datetime
class Scribe: 
    def __init__(self, _report_path):
        """Scribe is a custom module for generating simplistic test reports."""
        self.internal_path = "reports/"
        self.relative_path = True
        self.f = None
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.file_path = _report_path
        self.page_template = self.f_read(_filename=self.path+"/templates/page_template.py")
        self.scribble_template = self.f_read(_filename=self.path+"/templates/scribble_template.py")
        self.scribe_count = 0

    def new_page(self, _filename: str, _type: str=".py"):
        date = self.get_time()
        filename = f"{self.file_path}/{_filename}{date}--{datetime.datetime.now().hour}-{datetime.datetime.now().minute}-{datetime.datetime.now().second}.html"
        self.f_write(_filename=filename, _content=self.page_template)

        self.f = filename
        
        self.fill_argument("page_name", "report", self.f)
        self.fill_argument("page_date", self.get_time(), self.f)

        self.fill_argument("column_1", "#", self.f)
        self.fill_argument("column_2", "automated step", self.f)
        self.fill_argument("column_3", "expected result", self.f)
        self.fill_argument("column_4", "actual result", self.f)
        # self.fill_argument("column_5", "dsdsdsdsd", self.f)

        return self.f
    
    def find_line(self, _filename, _content):
        with open(_filename) as f:
            for (i, line) in enumerate(f):
                if _content in line:
                    return i
            return False

    def get_arguments(self, _template):
        template = self.f_read(_template)
        openning_bracket_list = []
        closing_bracket_list = []

        for char in template:
            if(char == "{{"):
                openning_bracket_list.append(char)
                continue
            if(char == "}}"):
                closing_bracket_list.append(char)
                continue

    def arg_replace(self, _file, _arg, _value):
        return _file.replace("{{"+_arg+"}}", _value)

    def record(self, _content):
        pass

    def recall(self, _filename):
        self.f = self.f_read(_filename=_filename)

    def modify(self, _filename, _content):
        self.f = self.f_read(_filename=_filename)

    def fill_argument(self, _arg, _value, _file):
        file_content = self.f_read(self.f)
        file_content = self.arg_replace(file_content, _arg, _value)
        self.f_write(self.f, file_content)
    
    def scribble(self, _arg, _value):
        file_content = self.f_read(self.f)
        file_content = self.arg_replace(file_content, _arg, _value)
        self.f_write(self.f, file_content)
        
    def finish(self):
        
        # scribble = """
        #     <tr style='display: block; width: 100%; text-align: center;'">
        #         <td>FINISHED</td>
        #     </tr>
        # """
        
        # scribble = self.arg_replace(scribble, "action_name", "FINISHED")
        # self.scribble("nextrow", scribble)
        pass

    def f_write(self, _filename, _content, _encoding="utf-8-sig"):
        with open(_filename, "w", encoding=_encoding) as file:
            file.write(str(_content))

    def f_append(self, _filename, content, encoding="utf-8-sig"):
        file = open(_filename, "a", encoding=encoding)
        file.write(str(content))
        file.close()

    def f_read(self, _filename, encoding="utf-8-sig"):
        file = open(_filename, "r", encoding=encoding)
        content = file.read()
        file.close()
        return content

    def f_read_int(self, _filename):
        file = open(_filename, "r")
        content = int(file.read())
        file.close()
        return content

    def f_read_once(self, _filename):
        file = open(_filename, "r")
        content = file.read()
        file.close()
        return content

    def f_read_lines(self, _filename):
        file = open(str(_filename))
        lines = file.readlines()
        for line in lines:
            lines[lines.index(line)] = line.replace("\n", "")
        return lines

    def get_time(arg=None):
        import datetime
        return f" {datetime.date.today().year}-{datetime.date.today().month}-{datetime.date.today().day}"
    
    def insert_row(self, _row_number="", _action_name="", _expected_result="", _actual_result="", _result_state="", _scribble=False):
        
        if(_scribble):
            if(_result_state):
                _result_state = "btn-success"
                _actual_result = "success"
            else:
                _result_state = "btn-danger"
                _actual_result = "failed"

            scribble = self.scribble_template

            scribble = self.arg_replace(scribble, "row_number", str(_row_number))
            scribble = self.arg_replace(scribble, "action_name", str(_action_name))
            scribble = self.arg_replace(scribble, "expected_result", str(_expected_result))
            scribble = self.arg_replace(scribble, "actual_result", str(_actual_result))
            scribble = self.arg_replace(scribble, "result_state", str(_result_state))
            # scribble = self.arg_replace(scribble, "dsdsdsdsd", str(_fourth_column))
            
            self.scribble("nextrow", scribble)
    def __del__(self):
        self.finish()
