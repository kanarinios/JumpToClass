import sublime
import sublime_plugin
import re

class JumpToClassCommand(sublime_plugin.TextCommand):
    def run(self, edit):
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
            self.view.window().run_command("insert", {"characters": " "})

        settings.set("word_separators", old_word_separators)

class SearchForWord(sublime_plugin.TextCommand):
    def run(self, edit):
        settings = self.view.settings()
        old_word_separators = settings.get("word_separators")
        jump_to_class_word_separators = settings.get("jump_to_class_word_separators")

        settings.set("word_separators", jump_to_class_word_separators)

        for sel in self.view.sel():
            if sel.empty():
                sel = self.view.word(sel)
            word_sel = self.view.substr(sel)
            self.view.window().run_command("show_panel", { 'panel': 'find_in_files' } )
            self.view.window().run_command("insert", {"characters": word_sel})

        settings.set("word_separators", old_word_separators)
