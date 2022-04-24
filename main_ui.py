import sys
from main_ui_lib import Ui_MainWindow

import manage_DB as db
from db_template import template_dict as TEMP_DATA
from output import docx_output

from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg


class ResumeDesign(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(ResumeDesign, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.actionSave.triggered.connect(self.save)
        self.actionOpen.triggered.connect(self.open_project)

        # TODO make email address n stuff bold
        # self.txt_email.clicked.connect(self.change_text_style(self.txt_email))

        self.btn_make.clicked.connect(self.make_resume)

    def change_text_style(self, txt_object):
        txt_object.setFont(False)
        pass

    def make_temp_data(self):
        TEMP_DATA["name"] = self.txt_name.text()
        TEMP_DATA["position"] = self.txt_position.text()
        TEMP_DATA["location"] = self.txt_loc.text()
        TEMP_DATA["email_address"] = self.txt_email.text()
        TEMP_DATA["linkedin_username"] = self.txt_linkd.text()
        TEMP_DATA["github_username"] = self.txt_git.text()
        # temp_data["introduction"] = self.

        # There is an AttributeError
        for row in range(self.tbl_skills.rowCount()):
            try:
                TEMP_DATA["relevant_skills"].append({
                    "label": str(self.tbl_skills.item(row, 0).text()),
                    "contents": str(self.tbl_skills.item(row, 1).text())
                })
            except AttributeError:
                pass

        for row in range(self.tbl_courses.rowCount()):
            try:
                TEMP_DATA["relevant_courses"].append({
                    "label": str(self.tbl_courses.item(row, 0).text()),
                    "contents": str(self.tbl_courses.item(row, 1).text())
                })
            except AttributeError:
                pass

        for row in range(self.tbl_edu.rowCount()):
            try:
                TEMP_DATA["educations"].append({
                    "major": str(self.tbl_edu.item(row, 0).text()),
                    "grad_date": str(self.tbl_edu.item(row, 1).text()),
                    "school_name": str(self.tbl_edu.item(row, 2).text()),
                    "school_loc": str(self.tbl_edu.item(row, 3).text()),
                    "gpa": str(self.tbl_edu.item(row, 4).text())
                })
            except AttributeError:
                pass

        for row in range(self.tbl_jobs.rowCount()):
            try:
                TEMP_DATA["work_experiences"].append({
                    "title": str(self.tbl_jobs.item(row, 0).text()),
                    "start_end": str(self.tbl_jobs.item(row, 1).text()),
                    "org_name": str(self.tbl_jobs.item(row, 2).text()),
                    # TODO make this work/ better
                    # "description": str(self.tbl_jobs.item(row, 3).text()),
                })
            except AttributeError:
                pass

        return TEMP_DATA

    def save(self):
        # TODO open a dialog box for user to enter file name
        context = self.make_temp_data()
        db.write_json(f"example", context)
        pass

    def make_resume(self):
        # TODO give a save popup box to user

        context = self.make_temp_data()

        db.write_json('new', context)

        docx_output(context, "EXAMPLE")

    def open_project(self):
        print("hello")
        pass


if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = ResumeDesign()
    widget.show()
    app.exec_()
