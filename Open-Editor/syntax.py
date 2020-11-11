import sys
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QColor, QTextCharFormat, QFont, QSyntaxHighlighter


def format(color, style=''):
  
    _color = QColor()
    if type(color) is not str:
        _color.setRgb(color[0], color[1], color[2])
    else:
        _color.setNamedColor(color)

    _format = QTextCharFormat()
    _format.setForeground(_color)
    if 'bold' in style:
        _format.setFontWeight(QFont.Bold)
    if 'italic' in style:
        _format.setFontItalic(True)

    return _format




STYLES = {
    'keyword': format([240, 94, 22], 'bold'),
    'operator': format([150, 150, 150]),
    'brace': format('darkGray'),
    'defclass': format([95, 158, 85], 'bold'),
    'string': format([20, 110, 100]),
    'string2': format([30, 120, 110]),
    'comment': format([128, 128, 128], 'italic'),
    'self': format([150, 85, 140], 'italic'),
    'numbers': format([100, 150, 190]),
}


class PythonHighlighter(QSyntaxHighlighter):
   


    keywords = [
        'and', 'assert', 'break', 'class', 'continue', 'def',
        'del', 'elif', 'else', 'except', 'exec', 'finally',
        'for', 'from', 'global', 'if', 'import', 'in',
        'is', 'lambda', 'not', 'or', 'pass', 'print',
        'raise', 'return', 'try', 'while', 'yield',
        'None', 'True', 'False',
    ]

    
    operators = [
        '=',
      
        '==', '!=', '<', '<=', '>', '>=',
        
        '\+', '-', '\*', '/', '//', '\%', '\*\*',
        
        '\+=', '-=', '\*=', '/=', '\%=',
       
        '\^', '\|', '\&', '\~', '>>', '<<',
    ]

    #
    braces = [
        '\{', '\}', '\(', '\)', '\[', '\]',
    ]

    def __init__(self, document):
        QSyntaxHighlighter.__init__(self, document)

        
        self.tri_single = (QRegExp("'''"), 1, STYLES['string2'])
        self.tri_double = (QRegExp('"""'), 2, STYLES['string2'])

        rules = []

      
        rules += [(r'\b%s\b' % w, 0, STYLES['keyword'])
                  for w in PythonHighlighter.keywords]
        rules += [(r'%s' % o, 0, STYLES['operator'])
                  for o in PythonHighlighter.operators]
        rules += [(r'%s' % b, 0, STYLES['brace'])
                  for b in PythonHighlighter.braces]

        
        rules += [
           
            (r'\bself\b', 0, STYLES['self']),

            (r'"[^"\\]*(\\.[^"\\]*)*"', 0, STYLES['string']),
           
            (r"'[^'\\]*(\\.[^'\\]*)*'", 0, STYLES['string']),

            
            (r'\bdef\b\s*(\w+)', 1, STYLES['defclass']),
            
            (r'\bclass\b\s*(\w+)', 1, STYLES['defclass']),

        
            (r'#[^\n]*', 0, STYLES['comment']),

            
            (r'\b[+-]?[0-9]+[lL]?\b', 0, STYLES['numbers']),
            (r'\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b', 0, STYLES['numbers']),
            (r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b', 0, STYLES['numbers']),
        ]

        
        self.rules = [(QRegExp(pat), index, fmt)
                      for (pat, index, fmt) in rules]

    def highlightBlock(self, text):
    
        for expression, nth, format in self.rules:
            index = expression.indexIn(text, 0)

            while index >= 0:
              
                index = expression.pos(nth)
                length = len(expression.cap(nth))
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        in_multiline = self.match_multiline(text, *self.tri_single)
        if not in_multiline:
            in_multiline = self.match_multiline(text, *self.tri_double)

    def match_multiline(self, text, delimiter, in_state, style):

        if self.previousBlockState() == in_state:
            start = 0
            add = 0
   
        else:
            start = delimiter.indexIn(text)
      
            add = delimiter.matchedLength()

        while start >= 0:
            
            end = delimiter.indexIn(text, start + add)
          
            if end >= add:
                length = end - start + add + delimiter.matchedLength()
                self.setCurrentBlockState(0)
            
            else:
                self.setCurrentBlockState(in_state)
                length = len(text) - start + add
            
            self.setFormat(start, length, style)
         
            start = delimiter.indexIn(text, start + length)

    
        if self.currentBlockState() == in_state:
            return True
        else:
            return False
