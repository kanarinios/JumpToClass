import sublime
import sublime_plugin
import re


class JumpToClassCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        print("haha")
        settings = self.view.settings()
        separator = settings.get("jump_to_class_separator")
        old_word_separators = settings.get("word_separators")
        jump_to_class_word_separators = settings.get("jump_to_class_word_separators")

        settings.set("word_separators", jump_to_class_word_separators)

        for sel in self.view.sel():
            if sel.empty():
                sel = self.view.word(sel)
            word_sel = self.view.substr(sel)
            word_sel = word_sel.replace(separator, ' ')
            self.view.window().run_command("show_overlay", {"overlay": "goto", "text": word_sel})
            ## Workaraound for selecting first match in GoTo Anywhere:
            self.view.window().run_command("indent")
            self.view.window().run_command("unindent")

        settings.set("word_separators", old_word_separators)
