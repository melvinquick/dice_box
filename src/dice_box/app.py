"""
Dice roller for board games, card games, bets, etc.
"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QPushButton,
    QLabel,
    QSpinBox,
    QGridLayout,
)

from .dice_roller import DiceRoller
from .yaml_file_handler import YamlFileHandler


class DiceBox(QMainWindow):
    def __init__(self):
        super().__init__()

        config_file = YamlFileHandler("resources/configs/config.yaml")
        self.config = config_file.load_yaml_file()

        themes_file = YamlFileHandler("resources/configs/themes.yaml")
        self.themes = themes_file.load_yaml_file()

        self.init_ui()

    def init_ui(self):
        self.show()

        # * Set window default settings
        self.setWindowTitle(self.config["window_title"])
        self.setFixedSize(
            self.config["window_size"]["width"], self.config["window_size"]["height"]
        )

        # * Create end user widgets and apply settings to them
        self.generate_rolls = QPushButton("Roll the Dice!")
        self.generate_rolls.setFixedWidth(self.config["input_widgets"]["width"])

        self.rolls = QLabel(
            "Rolls: ", alignment=Qt.AlignmentFlag.AlignCenter, wordWrap=False
        )

        self.sum_of_rolls = QLabel(
            "Sum of Rolls: ", alignment=Qt.AlignmentFlag.AlignCenter, wordWrap=False
        )

        self.even_count = QLabel(
            "Count of Evens Rolled: ",
            alignment=Qt.AlignmentFlag.AlignCenter,
            wordWrap=False,
        )

        self.odd_count = QLabel(
            "Count of Odds Rolled: ",
            alignment=Qt.AlignmentFlag.AlignCenter,
            wordWrap=False,
        )

        self.even_sum = QLabel(
            "Sum of Evens Rolled: ",
            alignment=Qt.AlignmentFlag.AlignCenter,
            wordWrap=False,
        )

        self.odd_sum = QLabel(
            "Sum of Odds Rolled: ",
            alignment=Qt.AlignmentFlag.AlignCenter,
            wordWrap=False,
        )

        self.num_dice = QSpinBox(prefix="Number of Dice: ")
        self.num_dice.setRange(
            self.config["num_dice"]["min"], self.config["num_dice"]["max"]
        )
        self.num_dice.setValue(self.config["num_dice"]["default"])
        self.num_dice.setFixedWidth(self.config["input_widgets"]["width"])

        self.num_sides = QSpinBox(prefix="Number of Sides: ")
        self.num_sides.setRange(
            self.config["num_sides"]["min"], self.config["num_sides"]["max"]
        )
        self.num_sides.setValue(self.config["num_sides"]["default"])
        self.num_sides.setFixedWidth(self.config["input_widgets"]["width"])

        self.theme_toggle = QPushButton("Dark")
        self.theme_toggle.setFixedWidth(self.config["input_widgets"]["width"])

        # * Define button connections and/or actions
        self.generate_rolls.pressed.connect(self.get_rolls)
        self.theme_toggle.pressed.connect(self.toggle_theme)

        # * Create layouts
        page = QGridLayout()
        inputs = QGridLayout()
        outputs = QGridLayout()

        # * Add widgets to layouts
        inputs.addWidget(self.generate_rolls, 0, 0, 1, 1)
        inputs.addWidget(self.num_dice, 1, 0, 1, 1)
        inputs.addWidget(self.num_sides, 2, 0, 1, 1)
        inputs.addWidget(self.theme_toggle, 3, 0, 1, 1)

        outputs.addWidget(self.rolls, 0, 0, 1, 2)
        outputs.addWidget(self.sum_of_rolls, 1, 0, 1, 2)
        outputs.addWidget(self.even_count, 2, 0, 1, 1)
        outputs.addWidget(self.odd_count, 2, 1, 1, 1)
        outputs.addWidget(self.even_sum, 3, 0, 1, 1)
        outputs.addWidget(self.odd_sum, 3, 1, 1, 1)

        # * Setup overall page layout and set default window theme
        page.addLayout(inputs, 0, 0)
        page.addLayout(outputs, 0, 2)

        gui = QWidget()
        gui.setLayout(page)

        self.setCentralWidget(gui)

        self.apply_theme(self.theme_toggle.text().lower())
        self.set_font()

    def get_rolls(self):
        roller = DiceRoller()
        (
            rolls,
            sum_of_rolls,
            count_of_evens,
            count_of_odds,
            sum_of_evens,
            sum_of_odds,
        ) = roller.roll(self.num_sides.value(), self.num_dice.value())
        self.rolls.setText(f"Rolls: {', '.join(map(str, rolls))}")
        self.sum_of_rolls.setText(f"Sum of Rolls: {sum_of_rolls}")
        self.even_count.setText(f"Count of Evens Rolled: {count_of_evens}")
        self.odd_count.setText(f"Count of Odds Rolled: {count_of_odds}")
        self.even_sum.setText(f"Sum of Evens Rolled: {sum_of_evens}")
        self.odd_sum.setText(f"Sum of Odds Rolled: {sum_of_odds}")

    def toggle_theme(self):
        if self.theme_toggle.text() == "Dark":
            self.theme_toggle.setText("Light")
            theme = self.theme_toggle.text()
        else:
            self.theme_toggle.setText("Dark")
            theme = self.theme_toggle.text()

        self.apply_theme(theme.lower())

    def apply_theme(self, theme):
        self.main_stylesheet = f"""
            background-color: {self.themes[theme]["background-color"]};
            color: {self.themes[theme]["color"]};
            border: {self.themes[theme]["border"]};
            border-radius: {self.themes["general"]["border-radius"]};
            padding: {self.themes["general"]["padding"]};
            """
        self.widget_stylesheet = f"""
            background-color: {self.themes[theme]["widget-background-color"]};
            """
        self.setStyleSheet(self.main_stylesheet)
        self.generate_rolls.setStyleSheet(self.widget_stylesheet)
        self.rolls.setStyleSheet(self.widget_stylesheet)
        self.sum_of_rolls.setStyleSheet(self.widget_stylesheet)
        self.even_count.setStyleSheet(self.widget_stylesheet)
        self.odd_count.setStyleSheet(self.widget_stylesheet)
        self.even_sum.setStyleSheet(self.widget_stylesheet)
        self.odd_sum.setStyleSheet(self.widget_stylesheet)
        self.num_dice.setStyleSheet(self.widget_stylesheet)
        self.num_sides.setStyleSheet(self.widget_stylesheet)
        self.theme_toggle.setStyleSheet(self.widget_stylesheet)

        (
            self.theme_toggle.setText("Dark")
            if theme == "dark"
            else self.theme_toggle.setText("Light")
        )

    def set_font(self):
        font = QFont("Commit Mono Nerd Font", 11)

        self.setFont(font)
        self.generate_rolls.setFont(font)
        self.rolls.setFont(font)
        self.sum_of_rolls.setFont(font)
        self.even_count.setFont(font)
        self.odd_count.setFont(font)
        self.even_sum.setFont(font)
        self.odd_sum.setFont(font)
        self.num_dice.setFont(font)
        self.num_sides.setFont(font)
        self.theme_toggle.setFont(font)


def main():
    app = QApplication(sys.argv)
    main_window = DiceBox()  # noqa: F841
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
