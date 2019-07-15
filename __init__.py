import json
from cuda_fmt import get_config_filename
from .indent_x.xml_indent_formatter import XmlIndentFormatter

xml_fmt = XmlIndentFormatter()

def format_xml(text):

    fn = get_config_filename('XML IndentX')
    s = open(fn, 'r').read()
    d = json.loads(s)

    xml_fmt.indentString = d.get('indent_string', '  ')
    xml_fmt.removeComments = d.get('remove_comments', False)
    xml_fmt.removeEmptyLines = d.get('remove_empty_lines', False)

    return xml_fmt.indent(text)
