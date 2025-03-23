from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit,
                             QPushButton, QComboBox, QTextEdit, QCheckBox, QApplication)
from application import get_recommendations


# Okno wyboru studiów
class StudyChoiceApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Wybór Studiów")
        self.resize(800, 800)
        self.center_window()

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setSpacing(15)  # Odstęp między widgetami
        layout.setContentsMargins(30, 15, 30, 15)  # Marginesy wokół układu

        # Nagłówek
        header = QLabel("Wybierz swoją ścieżkę kariery!", self)
        header.setFont(QFont('Arial', 18, QFont.Weight.Bold))
        header.setStyleSheet("color: white; background-color: #6699ff; padding: 10px; border-radius:20px;")
        header.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(header)


        # Wiersz 1: Miasto i Profil studiów
        city_profile_layout = QHBoxLayout()
        city_profile_layout.setSpacing(20)  # Odstęp między polami

        # Miasto
        city_layout = QVBoxLayout()
        city_layout.setSpacing(0)
        self.city_label = QLabel("Podaj miasto:")
        self.city_label.setFont(QFont('Arial', 14))
        city_layout.addWidget(self.city_label)
        self.city_input = QLineEdit()
        self.city_input.setFont(QFont('Arial', 12))
        self.city_input.setSizePolicy(self.city_input.sizePolicy().horizontalPolicy(),
                                      self.city_input.sizePolicy().verticalPolicy())
        city_layout.addWidget(self.city_input)
        city_profile_layout.addLayout(city_layout, 1)

        # Profil studiów
        profile_layout = QVBoxLayout()
        profile_layout.setSpacing(0)
        self.profile_label = QLabel("Profil studiów:")
        self.profile_label.setFont(QFont('Arial', 14))
        profile_layout.addWidget(self.profile_label)
        self.profile_input = QComboBox()
        self.profile_input.setFont(QFont('Arial', 12))
        self.profile_input.addItems(["Dowolny", "Praktyczny", "Ogólnoakademicki"])
        self.profile_input.setSizePolicy(self.profile_input.sizePolicy().horizontalPolicy(),
                                         self.profile_input.sizePolicy().verticalPolicy())
        profile_layout.addWidget(self.profile_input)
        city_profile_layout.addLayout(profile_layout, 1)

        layout.addLayout(city_profile_layout)


        # Wiersz 2: Stopień studiów i Rodzaj uczelni
        level_inst_layout = QHBoxLayout()
        level_inst_layout.setSpacing(20)  # odstęp między polami

        # Stopień studiów
        level_layout = QVBoxLayout()
        level_layout.setSpacing(0)
        self.level_label = QLabel("Stopień studiów:")
        self.level_label.setFont(QFont('Arial', 14))
        level_layout.addWidget(self.level_label)
        self.level_input = QComboBox()
        self.level_input.setFont(QFont('Arial', 12))
        self.level_input.addItems(["Jednolite magisterskie", "Pierwszego stopnia", "Drugiego stopnia"])
        level_layout.addWidget(self.level_input)
        level_inst_layout.addLayout(level_layout)

        # Rodzaj uczelni
        institution_layout = QVBoxLayout()
        institution_layout.setSpacing(0)
        self.institution_label = QLabel("Rodzaj uczelni:")
        self.institution_label.setFont(QFont('Arial', 14))
        institution_layout.addWidget(self.institution_label)
        self.institution_input = QComboBox()
        self.institution_input.setFont(QFont('Arial', 12))
        self.institution_input.addItems(
            ["Dowolna", "Uczelnia publiczna", "Uczelnia niepubliczna", "Uczelnia kościelna"])
        institution_layout.addWidget(self.institution_input)
        level_inst_layout.addLayout(institution_layout)

        layout.addLayout(level_inst_layout)


        # Zainteresowania
        interest_layout = QVBoxLayout()
        interest_layout.setSpacing(0)
        self.interest_label = QLabel("Podaj swoje zainteresowania:")
        self.interest_label.setFont(QFont('Arial', 14))
        interest_layout.addWidget(self.interest_label)
        self.interest_input = QLineEdit()
        self.interest_input.setFont(QFont('Arial', 12))
        interest_layout.addWidget(self.interest_input)

        # Dodanie checkboxów z przykładowymi zainteresowaniami
        checkbox_layout = QHBoxLayout()
        checkbox_layout.setSpacing(20)

        # Lista do przechowywania checkboxów
        self.interest_checkboxes = []

        # Funkcja obsługująca zmianę stanu checkboxa
        def on_interest_checkbox_toggled(checkbox, checked):
            if checked:
                for cb in self.interest_checkboxes:
                    if cb is not checkbox:
                        cb.blockSignals(True)
                        cb.setChecked(False)
                        cb.blockSignals(False)
                self.interest_input.setText(checkbox.text())
            else:
                if not any(cb.isChecked() for cb in self.interest_checkboxes):
                    self.interest_input.clear()

        # Checkbox 1: Programowanie
        checkbox1 = QCheckBox("Programowanie 🖥️")
        checkbox1.setFont(QFont('Arial', 12))
        checkbox1.toggled.connect(lambda checked, cb=checkbox1: on_interest_checkbox_toggled(cb, checked))
        self.interest_checkboxes.append(checkbox1)
        checkbox_layout.addWidget(checkbox1)

        # Checkbox 2: Muzyka
        checkbox2 = QCheckBox("Muzyka 🎵")
        checkbox2.setFont(QFont('Arial', 12))
        checkbox2.toggled.connect(lambda checked, cb=checkbox2: on_interest_checkbox_toggled(cb, checked))
        self.interest_checkboxes.append(checkbox2)
        checkbox_layout.addWidget(checkbox2)

        # Checkbox 3: Sztuka
        checkbox3 = QCheckBox("Sztuka 🎨")
        checkbox3.setFont(QFont('Arial', 12))
        checkbox3.toggled.connect(lambda checked, cb=checkbox3: on_interest_checkbox_toggled(cb, checked))
        self.interest_checkboxes.append(checkbox3)
        checkbox_layout.addWidget(checkbox3)

        # Checkbox 4: Sport
        checkbox4 = QCheckBox("Sport ⚽")
        checkbox4.setFont(QFont('Arial', 12))
        checkbox4.toggled.connect(lambda checked, cb=checkbox4: on_interest_checkbox_toggled(cb, checked))
        self.interest_checkboxes.append(checkbox4)
        checkbox_layout.addWidget(checkbox4)

        interest_layout.addLayout(checkbox_layout)
        layout.addLayout(interest_layout)


        # Przycisk wyszukiwania
        self.search_button = QPushButton("Znajdź kierunki studiów")
        self.search_button.setFont(QFont('Arial', 16, QFont.Weight.Bold))
        self.search_button.setStyleSheet("""
            QPushButton {
                background-color: #6699ff;
                color: white;
                border: none;
                padding: 15px 32px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                border-radius: 12px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        self.search_button.clicked.connect(self.search)
        layout.addWidget(self.search_button)


        # Pole do wyświetlania wyników
        self.result_label = QLabel("Wyniki:")
        self.result_label.setFont(QFont('Arial', 14))
        layout.addWidget(self.result_label)
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setFont(QFont('Arial', 14))
        self.result_text.setStyleSheet("background-color: #f4f4f9; border: 1px solid #ccc; color: #000000; border-radius:20px;")
        layout.addWidget(self.result_text)

        self.setLayout(layout)

    def center_window(self):
        screen = QApplication.primaryScreen().geometry()
        self.move((screen.width() - self.width()) // 2, (screen.height() - self.height()) // 2)

    def search(self):
        city = self.city_input.text()
        profile = self.profile_input.currentText()
        level = self.level_input.currentText()
        institution_kind = self.institution_input.currentText()
        interests = self.interest_input.text()

        results = get_recommendations(city, profile, level, institution_kind, interests)
        # Formatowanie wyników (aby poprawnie były wypisywane)
        if all(isinstance(item, str) and len(item) == 1 for item in results):
            formatted_results = "".join(results)  # Scala pojedyncze litery w tekst
        else:
            formatted_results = "\n\n".join(map(str, results))  # Łączy wyniki w pełne zdania, oddzielone nowymi liniami

        self.result_text.setText(formatted_results)

