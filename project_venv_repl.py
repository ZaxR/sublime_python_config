import sublime
import sublime_plugin


class ProjectReplOpenCommand(sublime_plugin.TextCommand):
    """Starts a SublimeREPL, attempting to use project's specified python interpreter."""

    def run(self, edit,
            view_id=None,
            external_id=None,
            cmd=None,
            cwd="$file_path",
            extend_env={'PYTHONIOENCODING': 'utf-8'},
            python_interpreter=None,
            cmd_flags=["-i", "-u"],
            open_file="$file",
            **kwds):
        """Called on project_repl_open command."""
        self.save_changed_files()

        if cmd is None:
            cmd = []
            if python_interpreter:
                cmd.append(python_interpreter)
            else:
                cmd.append(self.get_project_interpreter())

            cmd.extend(cmd_flags)
            cmd.append(open_file)
        print(cmd)
        self.view.window().run_command(
            'repl_open', {
                'encoding': "utf8",
                'type': "subprocess",
                'syntax': "Packages/Python/Python.tmLanguage",
                'view_id': view_id,
                'external_id': external_id,
                'cmd': cmd,
                'cwd': cwd,
                'extend_env': extend_env,
                "autocomplete_server": 'true'
            }
        )

    def save_changed_files(self):
        """Write out every buffer (active window) with changes and a file name."""
        window = sublime.active_window()
        for view in window.views():
            if view.is_dirty() and view.file_name():
                view.run_command('save')

    def get_project_interpreter(self):
        """Return the project's specified python interpreter, if any."""
        return self.view.settings().get("python_interpreter", "python")
