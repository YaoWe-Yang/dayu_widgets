#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################
from dayu_widgets.divider import MDivider
from dayu_widgets.label import MLabel
from dayu_widgets.tool_button import MToolButton
from dayu_widgets.line_tab_widget import MLineTabWidget
from dayu_widgets.qt import QWidget, QVBoxLayout, Qt


class LineTabWidgetExample(QWidget):
    def __init__(self, parent=None):
        super(LineTabWidgetExample, self).__init__(parent)
        self.setWindowTitle('Example for MLineTabWidget')
        self._init_ui()

    def _init_ui(self):
        main_lay = QVBoxLayout()

        tab_center = MLineTabWidget()
        tab_center.add_tab(MLabel('test 1 ' * 10),
                           {'text': u'Tab 1', 'svg': 'user_line.svg'})
        tab_center.add_tab(MLabel('test 2 ' * 10), {'svg': 'calendar_line.svg'})
        tab_center.add_tab(MLabel('test 3 ' * 10), u'Tab 3')
        tab_center.tool_button_group.set_dayu_checked(0)

        tab_left = MLineTabWidget(alignment=Qt.AlignLeft)
        tab_left.add_tab(MLabel('test 1 ' * 10), u'Tab 1')
        tab_left.add_tab(MLabel('test 2 ' * 10), u'Tab 2')
        tab_left.add_tab(MLabel('test 3 ' * 10), u'Tab 3')
        tab_left.tool_button_group.set_dayu_checked(0)

        tab_right = MLineTabWidget(alignment=Qt.AlignRight)
        tab_right.add_tab(MLabel('test 1 ' * 10), u'Tab 1')
        tab_right.add_tab(MLabel('test 2 ' * 10), u'Tab 2')
        tab_right.add_tab(MLabel('test 3 ' * 10), u'Tab 3')
        tab_right.tool_button_group.set_dayu_checked(0)

        tab_huge = MLineTabWidget()
        tab_huge.set_dayu_size(dayu_theme.huge)
        tab_huge.add_tab(MLabel('test 1 ' * 10),
                         {'text': u'Tab 1', 'svg': 'user_line.svg'})
        tab_huge.add_tab(MLabel('test 2 ' * 10), u'Tab 2')
        tab_huge.add_tab(MLabel('test 3 ' * 10), u'Tab 3')
        tab_huge.tool_button_group.set_dayu_checked(0)

        tab_append_insert = MLineTabWidget()
        tab_append_insert.add_tab(MLabel('test 1 ' * 10),
                         {'text': u'Tab 1', 'svg': 'user_line.svg'})
        tab_append_insert.add_tab(MLabel('test 2 ' * 10), u'Tab 2')
        tab_append_insert.add_tab(MLabel('test 3 ' * 10), u'Tab 3')
        tab_append_insert.tool_button_group.set_dayu_checked(0)
        tab_append_insert.insert_widget(MLabel("Insert Label").h4())
        tab_append_insert.append_widget(MToolButton().svg("refresh_line.svg").icon_only())

        main_lay.addWidget(MDivider('Center'))
        main_lay.addWidget(tab_center)
        main_lay.addSpacing(20)
        main_lay.addWidget(MDivider('Left'))
        main_lay.addWidget(tab_left)
        main_lay.addSpacing(20)
        main_lay.addWidget(MDivider('Right'))
        main_lay.addWidget(tab_right)
        main_lay.addSpacing(20)
        main_lay.addWidget(MDivider('Huge'))
        main_lay.addWidget(tab_huge)
        main_lay.addWidget(MDivider('append_widget/insert_widget'))
        main_lay.addWidget(tab_append_insert)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys
    from dayu_widgets.qt import QApplication
    from dayu_widgets import dayu_theme

    app = QApplication(sys.argv)
    test = LineTabWidgetExample()

    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
