import sublime, sublime_plugin


class DashesCommand(sublime_plugin.TextCommand):

    _line_length = 79
    _dash = '-'
    _prefix = '# '

    def run(self, edit):
        if self._is_python():
            for region in self.view.sel():
                self._dash_line(edit, region)

    def _dash_line(self, edit, region):
        text = self.view.substr(region)
        abs_begin = region.begin()

        if text:
            text = ' %s ' % text

        line_begin = self.view.line(abs_begin).begin()
        begin = abs_begin - line_begin
        length = self._line_length - begin

        ndashes = (length / 2) - (len(text) / 2)
        fit = int(length % 2)

        dashes_line = '{}{}{}{}'.format(
            self._prefix,
            self._dash * int(ndashes - len(self._prefix)),
            text,
            self._dash * int(ndashes + fit),
        )[:length]

        self.view.replace(edit, region, dashes_line.upper())

    def _is_python(self):
        sintax = self.view.settings().get('syntax')
        return sintax == 'Packages/Python/Python.tmLanguage'

# -----------------------------------------------------------------------------


class FinddashesCommand(sublime_plugin.TextCommand):

    _pattern = '^ *# ---.*---$'

    def run(self, edit):
        selection = self.view.sel()
        region = selection[0]

        found = self._find_next(region.begin())

        if found:
            selection.clear()
            selection.add(sublime.Region(found.end()))
            self.view.show(found.end())

    def _find_next(self, pos):
        found = self.view.find(self._pattern, pos)

        if pos > 0 and not found:
            found = self.view.find(self._pattern, 0)

        return found
