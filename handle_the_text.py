import win32clipboard

# Change data
def change_by_type(type, data_initial):
	if (type=='cas'):
		handle_cas_text(data_initial)
	if(type=='name'):
		handle_synonym_text(data_initial)

def handle_cas_text(data_initial):
	return data_initial+' c'

def handle_synonym_text(data_initial):
	return data_initial+' s'

def change_clipboard(text):
	print text
	# Read clipboard data
	data_initial = clipboard_read()
	#Defind a kind of change required
	change_by_type(text, data_initial)
	# Change the data
	data = data_initial + ' '+text
	# Write clipboard data
	clipboard_write(data)
	trigger=True

def clipboard_read():
	win32clipboard.OpenClipboard()
	data = win32clipboard.GetClipboardData()
	win32clipboard.CloseClipboard()
	return data

def clipboard_write(data):
	win32clipboard.OpenClipboard()
	win32clipboard.EmptyClipboard()
	win32clipboard.SetClipboardText(data)
	win32clipboard.CloseClipboard()

