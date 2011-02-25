from django import template
register = template.Library()
from ..lib.manager import BlockManager

block_manager = BlockManager()

@register.tag
def navigationbar ( parser, token ):
	try:
		tag_name, bar_name = token.split_contents()
	except ValueError:
		raise template.TemplateSyntaxError, "%r tag requires a single argument" % token.contents[0]
	return BlockNode( bar_name )

class BlockNode ( template.Node ):
	def __init__ ( self, block_name ):
		self.block_name = block_name

	def render ( self, context ):
		try :
			block = block_manager.get_block( self.block_name )
			return block.render()
		except:
			return ""

