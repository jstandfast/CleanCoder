import uuid
from datetime import datetime

class Project:
    def __init__(self, project_name, num_files, author, load_date=None, view_date=None):
        self.project_id = uuid.uuid4()
        self.project_name = project_name
        self.num_files = num_files
        self.author = author
        self.load_date = load_date if load_date else datetime.now()
        self.view_date = view_date

class File:
    def __init__(self, project_id, file_name, num_lines, file_lang, is_main):
        self.file_id = uuid.uuid4()
        self.project_id = project_id
        self.file_name = file_name
        self.num_lines = num_lines
        self.file_lang = file_lang
        self.is_main = is_main
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

class Line:
    def __init__(self, file_id, line_num, content):
        self.line_id = uuid.uuid4()
        self.file_id = file_id
        self.line_num = line_num
        self.content = content
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

class Dependency:
    def __init__(self, file_id, dependency_id, dependency_type)