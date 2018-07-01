import sys
import shlex
from urllib.parse import unquote
from subprocess import run

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DropWidget(QWidget):
    def __init__(self, parent=None, cmdline=None):
        super().__init__()
        self.setWindowTitle('dropkick')
        self.cmdline = cmdline
        if cmdline:
            self.label = QLabel(' '.join(cmdline), self)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        event.accept()
        mimeData = event.mimeData()
        d = unquote(str(mimeData.data('text/uri-list'), encoding='utf-8'))
        # print(repr(d))
        assert d.startswith('file://')
        d = d.rstrip()[len('file://'):]
        if self.cmdline:
            cmdline = self.cmdline[:]
            for i, c in enumerate(cmdline):
                if c == '{}':
                    cmdline[i] = d
                    break
            else:
                cmdline.append(d)
            print(' '.join(shlex.quote(c) for c in cmdline))
            run(cmdline)
        else:
            print(d)


def main():
    app = QApplication([sys.argv[0]])
    cmdline = sys.argv[1:]
    w = DropWidget(cmdline=cmdline)
    w.resize(200, 100)
    w.show()
    w.raise_()
    app.exec_()


if __name__ == '__main__':
    main()
