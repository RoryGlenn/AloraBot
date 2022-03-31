from PySide6.QtSvg import QSvgRenderer
from PySide6.QtCore import Qt, QSize, QObject
from PySide6.QtGui import QPixmap, QPainter, QFontDatabase, QFont


def load_svg(path: str, size: QSize) -> QPixmap:
    """Load a svg file and return a qpixmap"""
    svg_render = QSvgRenderer(path)
    new_image = QPixmap(size)
    painter = QPainter()

    new_image.fill(Qt.transparent)
    painter.begin(new_image)
    svg_render.render(painter)
    painter.end()
    return new_image


def set_font(target: QObject, size: int, italic: bool=False, bold: bool=False) -> None:
    """Set a custom font to the target"""
    # font_name = ':/fonts/Ubuntu-Regular.ttf' if not italic else ':/fonts/Ubuntu-Italic.ttf'
    font_name = 'src/resources/fonts/Ubuntu-Regular.ttf' if not italic else 'src/resources/fonts/Ubuntu-Italic.ttf'
    index = 0

    # add font to app database
    font_id = QFontDatabase.addApplicationFont(f'{font_name}')
    font_name = QFontDatabase.applicationFontFamilies(font_id)

    if len(font_name) > index:
        # get font name
        font = QFont(font_name[index])
        font.setPointSize(size)
        font.setBold(bold)
        font.setItalic(italic)
        font.setStyleStrategy(QFont.PreferAntialias)
        target.setFont(font)


def find_parent(obj: QObject, target: str):
    """Find the target parent of a children qobject"""
    parent = obj.parent()

    if hasattr(obj, 'objectName'):
        for _ in range(40):
            if obj.objectName() == target:
                return obj
            else:
                obj = obj.parent()
    return None
