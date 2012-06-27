import sublime, sublime_plugin

clipboard_stack = []

class ClipboardStackPushCommand(sublime_plugin.WindowCommand):
	def run(self):
		global clipboard_stack
		clipcontent = sublime.get_clipboard()
		clipboard_stack.append(clipcontent)
		r = repr(clipcontent)[1:-1]
		sublime.status_message("\'{content}{ellipsis}\' pushed to stack ({num} elements total).".format(content=r[:10], ellipsis="..." if len(r) > 10 else "", num=len(clipboard_stack)))

class ClipboardStackPopCommand(sublime_plugin.WindowCommand):
	def run(self):
		global clipboard_stack
		if len(clipboard_stack) == 0:
			sublime.status_message("Error: Clipboard stack is empty, can not pop.")
		else:
			el = clipboard_stack.pop()
			r = repr(el)[1:-1]
			sublime.set_clipboard(el)
			sublime.status_message("Clipboard is now '{content}{ellipsis}', stack has now {num} elements.".format(content=r[:10], ellipsis="..." if len(r) > 10 else "", num=len(clipboard_stack)))

class ClipboardStackSelectCommand(sublime_plugin.WindowCommand):
	def run(self):
		global clipboard_stack
		if len(clipboard_stack) == 0:
			sublime.status_message("Stack is empty.")
		
		self.window.show_quick_panel([ repr(x)[1:-1] for x in clipboard_stack[::-1] ], self.qp_response)
	
	def qp_response(self, idx):
		global clipboard_stack
		if idx == -1:
			return
		
		addr = -(idx+1)
		
		el = clipboard_stack[addr]
		r = repr(el)[1:-1]
		clipboard_stack = clipboard_stack[:addr] + clipboard_stack[addr+1:]
		sublime.set_clipboard(el)
		sublime.status_message("Clipboard is now '{content}{ellipsis}', stack has now {num} elements.".format(content=r[:10], ellipsis="..." if len(r) > 10 else "", num=len(clipboard_stack)))

class ClipboardStackClearCommand(sublime_plugin.WindowCommand):
	def run(self):
		global clipboard_stack
		clipboard_stack = []
		sublime.status_message("Clipboard stack is now empty.")