import logging

from django.template.loader import render_to_string
from django.template import Context, loader
from django.utils.safestring import mark_safe

from autorender import auto_render

LOGGER = logging.getLogger(__name__)

class BlockDoesNotExistError(Exception):
	def __init__(self,value=None):
		self.value = value

	def render(self):
		return "Block does not exist"

BLOCKS = {}

class BlockManager:
	platform_display = ''

	def __init__(self):
		pass

	def get_block(self, name):
		if name in BLOCKS.keys() :
			block = BLOCKS[name]
		else :
			LOGGER.log(logging.DEBUG, "Could not find block with name : %s " % name)
			block = None
		return block

	def add_block(self, name, data):
		block = self.get_block(name)
		if not block :
			BLOCKS[name] = Block(self, name, data)
		else :
			LOGGER.log(logging.DEBUG, "Block aready exists : %s " % name)

	def remove_block(self, name):
		block = self.get_block(name)
		if block :
			del BLOCKS[name]
		else :
			LOGGER.log(logging.DEBUG, "Tried to remove : %s " % name)

	def blocks(self, filter=None):
		output = []
		if filter :
			for name, block in BLOCKS.items() :
				if filter(block) :
					output.append(block)
		else :
			for name, block in BLOCKS.items() :
					output.append( mark_safe(block) )

		return output

#	def render(self, name, *args, **kwargs):
#		pass

class Block:
	_title = ''
	_content = []

	def __init__(self, manager=None, title=None, content=None):
		try :
			self.set_title(title)
			self.add_content(content)
			self.manager = manager
		except :
			raise "No manager provided."

	def set_title(self, title):
		self._title = title

	def get_title(self, title):
		return self._title

	title = property(get_title, set_title)

	def get_content(self, index=None):
		if index and index < len(self._content)-1 :
			return self._content[index]
		else :
			return self._content

	def add_content(self,value=None):
		if value :
			self._content.append(value)
		else :
			LOGGER.log("WARNING", "Tried to add 'None' content to block (%s)" % self.title)

	def remove_content(self, index):
		if index :
			self._content.pop(index)
		else:
			LOGGER.log("ERROR", "No index provided for referencing content item to delete.")

	content = property(get_content, add_content, remove_content, "Retrieve, Add, and Remove content items from the block")

	def render (self, template_path="snippets/block.html"):
		return render_to_string(template_path,{
			"Title": self._title,
			"Block": self._content
		})

	def __str__(self):
		return self.render()

