class CodeBuilder(object):
    def __init__(self, indent=0):
        self.code = []
        self.indent_level = indent

    def add_line(self, line):
        self.code.extend([" "*self.indent_level, line, '\n'])

    INDENT_STEP = 4
    def indent(self):
        self.indent_level += self.INDENT_STEP

    def dedent(self):
        self.indent_level -= self.INDENT_STEP

    def add_section(self):
        section = CodeBuilder(self.indent_level)
        self.code.append(section)
        return section

    def __str__(self):
        return "".join(str(c) for c in self.code)

    def get_globals(self):
        assert self.indent_level == 0
        python_source = str(self)
        global_namespace = {}
        exec(python_source, global_namespace)
        return global_namespace

    python_source = """\
    SEVENTEEN = 17

    def three():
        return 3
    """
    global_namespace = {}
    exec(python_source, global_namespace)