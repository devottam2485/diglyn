from location import DLLocation
from DLStudent import *
from DLMentor import *

from __UI import DLTrackerUI
from PyQt4 import QtCore
from PyQt4 import QtGui

import config
import time
import sys

DL_SPLASH = posixpath.join(os.path.dirname(__file__), 'assets', 'icon', 'dl.png')
DL_ICON_PATH = posixpath.join(os.path.dirname(__file__), 'assets', 'icon', 'dl3.png')

class Digital_Lync(QtGui.QMainWindow, DLTrackerUI.Ui_MainWindow, digital_lync_student, digital_lync_mentor):
    def __init__(self, parent=None):
        super(Digital_Lync, self).__init__()
        self.Digital_Lync_location = DLLocation().location
        self.setWindowTitle("Digital Lync")
        self.setWindowIcon(QtGui.QIcon(DL_ICON_PATH))
        self.setupUi(self)

        #for registration page connection
        self.student_radioButton.setChecked(True)
        self.mentor_radioButton.clicked.connect(self.registration_ui_changes)
        self.student_radioButton.clicked.connect(self.registration_ui_changes)
        self.studentID_lineEdit.returnPressed.connect(self.load_registration_id)
        self.loadID_pushButton.clicked.connect(self.load_registration_id)
        self.reset_pushButton.clicked.connect(self.reset_student_page)
        self.add_course_pushButton.clicked.connect(self.add_course)
        self.remove_course_pushButton.clicked.connect(self.remove_course)
        self.courses_listWidget.addItems([item.capitalize() for item in config.DigitalLoc().courses])
        self.update_pushButton.setEnabled(False)
        self.update_pushButton.clicked.connect(self.update_registration_id)
        self.generateID_pushButton.clicked.connect(self.get_registration_id)
        self.remove_student_checkBox.clicked.connect(self.student_remove_event)
        self.student_fname_lineEdit.textChanged.connect(self.validate_fname)
        self.student_lname_lineEdit.textChanged.connect(self.validate_lname)
        self.mob_number_lineEdit.textChanged.connect(self.validate_mobile_number)
        self.emailid_lineEdit.textChanged.connect(self.validate_email_id)
        self.registration_ui_changes()

        #for Tracker page connection

        #for Batch page connection

    #FOR REGISTRATION PAGE METHODS

    def registration_ui_changes(self):
        if self.mentor_radioButton.isChecked():
            self.generateID_pushButton.setText("Generate Mentor ID")
            self.remove_student_checkBox.setText("Remove Mentor")
            self.profession_label.setText("Experience")
            self.course_label.setText("Subjects")
            self.course_opted_label.setText("Mentor Subject Expert")
            self.id_label.setText("Mentor ID")
            self.bar_graph_label.setPixmap(QtGui.QPixmap('./assets/stat_data/mentor_count_bar.png'))
        else:
            self.generateID_pushButton.setText("Generate Student ID")
            self.remove_student_checkBox.setText("Remove Student")
            self.profession_label.setText("Profession")
            self.course_label.setText("Courses Available")
            self.course_opted_label.setText("Courses Opted")
            self.id_label.setText("Student ID")
            self.bar_graph_label.setPixmap(QtGui.QPixmap('./assets/stat_data/student_count_bar.png'))
        self.registration_auto_completer()
        self.reset_student_page()

    def student_remove_event(self):
        if self.remove_student_checkBox.isChecked():
            self.update_pushButton.setText("Remove")
            self.update_pushButton.setEnabled(True)
            self.studentID_lineEdit.setEnabled(False)
            self.student_fname_lineEdit.setEnabled(False)
            self.student_lname_lineEdit.setEnabled(False)
            self.dob_lineEdit.setEnabled(False)
            self.qualification_lineEdit.setEnabled(False)
            self.profession_lineEdit.setEnabled(False)
            self.address_textEdit.setEnabled(False)
            self.mob_number_lineEdit.setEnabled(False)
            self.emailid_lineEdit.setEnabled(False)
            self.course_opted_listWidget.setEnabled(False)
            self.generateID_pushButton.setEnabled(False)
            self.add_course_pushButton.setEnabled(False)
            self.remove_course_pushButton.setEnabled(False)
        else:
            self.update_pushButton.setText("Update")
            self.studentID_lineEdit.setEnabled(True)
            self.student_fname_lineEdit.setEnabled(True)
            self.student_lname_lineEdit.setEnabled(True)
            self.dob_lineEdit.setEnabled(True)
            self.qualification_lineEdit.setEnabled(True)
            self.profession_lineEdit.setEnabled(True)
            self.address_textEdit.setEnabled(True)
            self.mob_number_lineEdit.setEnabled(True)
            self.emailid_lineEdit.setEnabled(True)
            self.course_opted_listWidget.setEnabled(True)
            self.generateID_pushButton.setEnabled(True)
            self.add_course_pushButton.setEnabled(True)
            self.remove_course_pushButton.setEnabled(True)

    def reset_student_page(self):
        self.studentID_lineEdit.clear()
        self.student_fname_lineEdit.clear()
        self.student_lname_lineEdit.clear()
        self.dob_lineEdit.clear()
        self.qualification_lineEdit.clear()
        self.profession_lineEdit.clear()
        self.address_textEdit.clear()
        self.mob_number_lineEdit.clear()
        self.emailid_lineEdit.clear()
        self.course_opted_listWidget.clear()
        self.studentID_lineEdit.setEnabled(True)
        self.generateID_pushButton.setEnabled(True)
        self.student_fname_lineEdit.setEnabled(True)
        self.student_lname_lineEdit.setEnabled(True)
        self.dob_lineEdit.setEnabled(True)
        self.qualification_lineEdit.setEnabled(True)
        self.profession_lineEdit.setEnabled(True)
        self.address_textEdit.setEnabled(True)
        self.mob_number_lineEdit.setEnabled(True)
        self.emailid_lineEdit.setEnabled(True)
        self.course_opted_listWidget.setEnabled(True)
        self.remove_student_checkBox.setChecked(False)
        self.update_pushButton.setText("Update")

    def add_course(self):
        self.course_opted_listWidget.clear()
        self.course_opted_listWidget.addItems([items.text() for items in self.courses_listWidget.selectedItems()])

    def remove_course(self):
        list_of_opted_course = self.course_opted_listWidget.selectedItems()
        for course_item in list_of_opted_course:
            self.course_opted_listWidget.takeItem(self.course_opted_listWidget.row(course_item))

    def registration_auto_completer(self):
        self.registration_completer = QtGui.QCompleter()
        registration_model = QtGui.QStringListModel()
        self.registration_completer.setModel(registration_model)
        if self.student_radioButton.isChecked():
            registration_model.setStringList(digital_lync_student.get_student_ID_list())
        else:
            registration_model.setStringList(digital_lync_mentor.get_mentor_ID_list())
        self.studentID_lineEdit.setCompleter(self.registration_completer)

    def get_registration_id(self, id_name=''):
        '''

        :param id_name:
        :return:
        '''
        if self.student_radioButton.isChecked():
            if id_name:
                digital_lync_student.__init__(self, id_name)
            else:
                self.studentID_lineEdit.setText(digital_lync_student.generate_student_ID())
                self.generateID_pushButton.setEnabled(False)
                self.studentID_lineEdit.setEnabled(False)
        else:
            if id_name:
                digital_lync_mentor.__init__(self, id_name)
            else:
                self.studentID_lineEdit.setText(digital_lync_mentor.generate_mentor_ID())
                self.generateID_pushButton.setEnabled(False)
                self.studentID_lineEdit.setEnabled(False)

    def validate_fname(self):
        get_fname = str(self.student_fname_lineEdit.text())
        if not get_fname:
            self.fname_valid_label.setText('mandatory field')
            return
        if not get_fname.isalpha():
            self.student_fname_lineEdit.setText(str(get_fname[:-1].upper()))
            self.fname_valid_label.setText('valid')
            return
        self.student_fname_lineEdit.setText(str(get_fname.upper()))
        self.fname_valid_label.setText('valid')

    def validate_lname(self):
        get_lname = str(self.student_lname_lineEdit.text())
        if not get_lname:
            self.lname_valid_label.setText('mandatory field')
            return
        if not get_lname.isalpha():
            self.student_lname_lineEdit.setText(str(get_lname[:-1].upper()))
            self.lname_valid_label.setText('Valid')
            return
        self.student_lname_lineEdit.setText(str(get_lname.upper()))
        self.lname_valid_label.setText('Valid')

    def validate_mobile_number(self):
        '''

        :return:
        '''
        get_text = str(self.mob_number_lineEdit.text())
        if not get_text:
            self.mob_num_label.setText('mandatory field')
        for item in get_text:
            if ord(item) not in range(48, 58):
                self.mob_number_lineEdit.setText(get_text[:-1])
                return
            else:
                if len(get_text)>=10:
                    self.mob_number_lineEdit.setText(get_text[:10])
                    self.update_pushButton.setEnabled(True)
                    self.mob_num_label.setText('valid')
                    return
                else:
                    self.mob_number_lineEdit.setText(get_text[:10])
                    self.update_pushButton.setEnabled(False)
                    self.mob_num_label.setText('Invalid')

    def validate_email_id(self):
        valid_email = str(self.emailid_lineEdit.text())
        if str(self.emailid_lineEdit.text()).rsplit('.', 1)[-1] in ('com', 'in', 'org', 'gov', 'edu', 'net') and \
                        len(str(self.emailid_lineEdit.text()).split('@')) == 2:
            self.emailid_lineEdit.setText(valid_email)
            self.email_id_label.setText('valid')
            self.update_pushButton.setEnabled(True)
        else:
            self.update_pushButton.setEnabled(False)
            self.email_id_label.setText('Invalid')

    def update_registration_id(self):
        '''

        :return:
        '''
        registration_id = str(self.studentID_lineEdit.text())
        if registration_id:
            if self.student_radioButton.isChecked():
                digital_lync_student.__init__(self, registration_id)
            else:
                digital_lync_mentor.__init__(self, registration_id)
        else:
            print("Student ID is Required")
            return
        registration_fname = str(self.student_fname_lineEdit.text())
        if not registration_fname:
            print("Student First Name is Required")
            return
        registration_lname = str(self.student_lname_lineEdit.text())
        if not registration_lname:
            print("Student last Name is Required")
            return
        registration_dob = str(self.dob_lineEdit.text())
        registration_qulfctn = str(self.qualification_lineEdit.text())
        registration_prof = str(self.profession_lineEdit.text())
        registration_addrs = str(self.address_textEdit.toPlainText())
        registration_mob = str(self.mob_number_lineEdit.text())
        if not registration_mob:
            print("Student Mobile Number is Required")
            return
        registration_email = str(self.emailid_lineEdit.text())
        registration_course_opted = [str(self.course_opted_listWidget.item(item).text()).lower() for item in range(self.course_opted_listWidget.count())]
        if not registration_course_opted:
            print("Please Add atleast 1 course")
            return
        if self.student_radioButton.isChecked():
            if self.remove_student_checkBox.isChecked():
                self.update_student_details(registration_fname, registration_lname, registration_dob, registration_qulfctn, registration_addrs, registration_mob, registration_email, registration_prof, registration_course_opted, remove_flag=True)
            else:
                self.update_student_details(registration_fname, registration_lname, registration_dob, registration_qulfctn, registration_addrs, registration_mob, registration_email, registration_prof, registration_course_opted)
        else:
            if self.remove_student_checkBox.isChecked():
                self.update_mentor_details(registration_fname, registration_lname, registration_dob, registration_qulfctn, registration_addrs, registration_mob, registration_email, registration_prof, registration_course_opted, remove_flag=True)
            else:
                self.update_mentor_details(registration_fname, registration_lname, registration_dob, registration_qulfctn, registration_addrs, registration_mob, registration_email, registration_prof, registration_course_opted)
        self.reset_student_page()
        self.registration_auto_completer()
        self.registration_ui_changes()


    def load_registration_id(self):
        registration_id = str(self.studentID_lineEdit.text())
        if registration_id:
            if self.student_radioButton.isChecked():
                digital_lync_student.__init__(self, registration_id)
                self.student_fname_lineEdit.setText(self.get_student_fname)
                self.student_lname_lineEdit.setText(self.get_student_lname)
                self.dob_lineEdit.setText(self.get_student_dob)
                self.qualification_lineEdit.setText(self.get_student_qualification)
                self.profession_lineEdit.setText(self.get_student_profession)
                self.address_textEdit.setText(self.get_student_address)
                self.mob_number_lineEdit.setText(self.get_student_mobile)
                self.emailid_lineEdit.setText(self.get_student_email)
                self.course_opted_listWidget.clear()
                self.course_opted_listWidget.addItems(self.get_student_courses_opted)
            else:
                digital_lync_mentor.__init__(self, registration_id)
                self.student_fname_lineEdit.setText(self.get_mentor_fname)
                self.student_lname_lineEdit.setText(self.get_mentor_lname)
                self.dob_lineEdit.setText(self.get_mentor_dob)
                self.qualification_lineEdit.setText(self.get_mentor_qualification)
                self.profession_lineEdit.setText(self.get_mentor_experience)
                self.address_textEdit.setText(self.get_mentor_address)
                self.mob_number_lineEdit.setText(self.get_mentor_mobile)
                self.emailid_lineEdit.setText(self.get_mentor_email)
                self.course_opted_listWidget.clear()
                self.course_opted_listWidget.addItems(self.get_mentor_subject_expert)
            self.generateID_pushButton.setEnabled(False)
            self.update_pushButton.setEnabled(True)
        else:
            print("Student ID is Required")
            self.reset_student_page()
            return


def main():
    app = QtGui.QApplication(sys.argv)
    splash_pix = QtGui.QPixmap(DL_SPLASH)
    splash = QtGui.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    label = QtGui.QLabel(splash)
    label.move(135, 0)
    label.setText("Initializing ...")
    label.setStyleSheet("QLabel{color: black}")
    splash.show()
    time.sleep(2)
    app.closeAllWindows()
    buildapp = Digital_Lync()
    buildapp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()