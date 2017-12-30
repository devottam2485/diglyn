import json
import random
import posixpath
import time
import os

from location import DLLocation
from DLStatData import *

root_student_path = os.path.dirname(__file__)

loc = DLLocation().location
student_config_file_path = posixpath.join(root_student_path, 'config/students', loc + '.json')


class digital_lync_student(object, digital_lync_chart):
    def __init__(self, student_ID):
        digital_lync_chart.__init__(self)
        self.__student_ID = student_ID
        self.student_file_path = student_config_file_path
        self.load_student_dict()

    @property
    def get_student_ID(self):
        return self.__student_ID

    @property
    def get_student_fname(self):
        return self.__first_name

    @property
    def get_student_lname(self):
        return self.__last_name

    @property
    def get_student_dob(self):
        return self.__date_of_birth

    @property
    def get_student_qualification(self):
        return self.__qualification

    @property
    def get_student_address(self):
        return self.__address

    @property
    def get_student_mobile(self):
        return self.__mobile

    @property
    def get_student_email(self):
        return self.__email

    @property
    def get_student_profession(self):
        return self.__profession

    @property
    def get_student_courses_opted(self):
        return self.__courses_opted

    def update_student_details(self, first_name, last_name, dob, qualification, address, mob_num, email_id, profession=None, courses_opted=[], remove_flag=False):
        if remove_flag:
            if self.__student_ID in self.student_dict:
                self.student_dict.pop(self.__student_ID)
            else:
                print("The Student ID is Not Valid")
        else:
            if self.__student_ID in self.student_dict:
                self.student_dict[self.__student_ID].update({'__first_name': first_name, '__last_name': last_name, '__date_of_birth': dob,
                                                          '__qualification': qualification, '__address':address, '__mobile': mob_num,
                                                          '__email': email_id, '__profession':profession, '__courses_opted': courses_opted})
            else:
                self.student_dict[self.get_student_ID] = {'__first_name': first_name, '__last_name': last_name, '__date_of_birth': dob,
                                                          '__qualification': qualification, '__address':address, '__mobile': mob_num,
                                                          '__email': email_id, '__profession':profession, '__courses_opted': courses_opted}

        open_student_file = open(self.student_file_path, 'w')
        json.dump(self.student_dict, open_student_file, indent=2)
        open_student_file.close()
        print("Updating...")
        time.sleep(3)
        self.plot_student_chart()
        print("Updated.")
        self.student_dict={}


    def load_student_dict(self):
        try:
            fp = open(self.student_file_path, 'r')
            self.student_dict = json.load(fp)
            fp.close()
            if self.__student_ID in self.student_dict:
                self.__first_name = self.student_dict[self.__student_ID]['__first_name']
                self.__last_name = self.student_dict[self.__student_ID]['__last_name']
                self.__date_of_birth = self.student_dict[self.__student_ID]['__date_of_birth']
                self.__qualification = self.student_dict[self.__student_ID]['__qualification']
                self.__address = self.student_dict[self.__student_ID]['__address']
                self.__mobile = self.student_dict[self.__student_ID]['__mobile']
                self.__email = self.student_dict[self.__student_ID]['__email']
                self.__profession = self.student_dict[self.__student_ID]['__profession']
                self.__courses_opted = self.student_dict[self.__student_ID]['__courses_opted']
            else:
                self.student_dict[self.__student_ID] = {}
        except:
            self.student_dict = {}
            print("Unable to load student config")


    @classmethod
    def generate_student_ID(cls):
        total_student_count = 1000
        id_num = str(random.randrange(1, total_student_count)).zfill(5)
        if loc == 'gachibowli':
            loc_tag = 'gb'
        elif loc == 'kukatpally':
            loc_tag = 'kp'
        elif loc == 'srnagar':
            loc_tag = 'sn'
        else:
            print("Location Not Valid")
        try:
            fp = open(student_config_file_path, 'r')
            student_ID_dict = json.load(fp)
            fp.close()
            if len(student_ID_dict)>=total_student_count:
                print("No Admission Available")
                return False
            if str('_'.join(['dl_st', loc_tag, id_num])) in student_ID_dict.keys():
                return cls.generate_student_ID()
            else:
                return '_'.join(['dl_st', loc_tag, id_num])
        except:
            return '_'.join(['dl_st', loc_tag, id_num])

    @staticmethod
    def get_student_ID_list():
        try:
            fp = open(student_config_file_path, 'r')
            student_ID_dict = json.load(fp)
            fp.close()
            return student_ID_dict.keys()
        except:
            print("Unable to Load Student Config")
            return []




