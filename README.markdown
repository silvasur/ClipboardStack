ClipboardStack
==============

A Plugin for [Sublime Text 2](http://www.sublimetext.com) to organize your clipboard.

Need more than one clipboard? Push your current clipboard on a stack and retrieve it later by pop it from the top of the stack or selecting an arbitrary stack element.

Install
-------

Clone this repository into your *Packages* directory:

	$ cd ~/.config/sublime-text-2/Packages/
	$ git clone https://github.com/kch42/ClipboardStack.git

Commands
--------

Here is a list of implemented commands:

* `clipboard_stack_push` - Push clipboard content on stack
* `clipboard_stack_pop` - Pop content from stack to clipboard
* `clipboard_stack_select` - Select an element from the stack
* `clipboard_stack_clear` - Clear Stack

You can reach the commands from the **Command Palette** (`Ctrl+Shift+P`) and searching for `Clipboard Stack:`.

