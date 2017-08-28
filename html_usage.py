# -*-coding=utf-8-*-

#from xml.parsers.expat import ParserCreate
#
#class DefaultSaxHandler(object):
#	def start_element(self, name, attrs):
#		print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
#
#	def end_element(self, name):
#		print('sax:end_element: %s' % name)
#
#	def char_data(self, text):
#		print('sax:char_data: %s' % text)
#
#xml = r'''<?xml version="1.0"?>
#<ol>
#	<li><a href="/python">Python</a></li>
#	<li><a href="/ruby">Ruby</a></li>
#</ol>
#'''
#
#handler = DefaultSaxHandler()
#parser = ParserCreate()
#parser.returns_unicode = True
#parser.StartElementHandler = handler.start_element
#parser.EndElementHandler = handler.end_element
#parser.CharacterDataHandler = handler.char_data
#parser.Parse(xml)

#from HTMLParser import HTMLParser
#from htmlentitydefs import name2codepoint
#
#class MyHTMLParser(HTMLParser):
#	def handle_starttag(self, tag, attrs):
#		print('<%s>' % tag)
#
#	def handle_endtag(self, tag):
#		print('</%s>' % tag)
#
#	def handle_startendtag(self, tag, attrs):
#		print('<%s/>' % tag)
#
#	def handle_data(self, data):
#		print('data: %s' % data)
#
#	def handle_comment(self, data):
#		print('<!-- %s -->' % data)
#
#	def handle_entityref(self, name):
#		print('&%s;' % name)
#
#	def handle_charref(self, name):
#		print('&#%s;' % name)
#
#parser = MyHTMLParser()
#parser.feed('<html><head></head><body><p>Some <a href=\"#\">html</a> tutorial...<br>END</p></body></html>')

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

def rndChar():
	return chr(random.randint(65, 90))

def rndColor():
	return (random.randint(64,255), random.randint(64,255), random.randint(64,255))

def rndColor2():
	return (random.randint(32,127), random.randint(32,127), random.randint(32,127))

width = 60 * 4
height = 60
image = Image.new('RGB', (width,height), (255,255,255))
font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 36)
draw = ImageDraw.Draw(image)

for x in range(width):
	for y in range(height):
		draw.point((x,y), fill=rndColor())

for t in range(4):
	draw.text((60*t+10, 10), rndChar(), font=font, fill=rndColor2())

image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
