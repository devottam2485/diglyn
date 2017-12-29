import json
import random
import posixpath
import os

from location import DLLocation

root_mentor_path = os.path.dirname(__file__)

loc = DLLocation().location
mentor_config_file_path = posixpath.join(root_mentor_path, 'config/mentors', loc + '.json')


class digital_lync_mentor(object):
    def __init__(self, mentor_ID):
        self.__mentor_ID = mentor_ID
        self.mentor_file_path = mentor_config_file_path
        self.load_mentor_dict()

    @property
    def get_mentor_ID(self):
        return self.__mentor_ID

    @property
    def get_mentor_fname(self):
        return self.__first_name

    @property
    def get_mentor_lname(self):
        return self.__last_name

    @property
    def get_mentor_dob(self):
        return self.__date_of_birth

    @property
    def get_mentor_qualification(self):
        return self.__qualification

    @property
    def get_mentor_address(self):
        return self.__address

    @property
    def get_mentor_mobile(self):
        return self.__mobile

    @property
    def get_mentor_email(self):
        return self.__email

    @property
    def get_mentor_experience(self):
        return self.__experience

    @property
    def get_mentor_subject_expert(self):
        return self.__subject_expert

    def update_mentor_details(self, first_name, last_name, dob, qualification, address, mob_num, email_id, experience=None, subject_expert=[], remove_flag=False):
        if remove_flag:
            if self.__mentor_ID in self.mentor_dict:
                self.mentor_dict.pop(self.__mentor_ID)
            else:
                print("The mentor ID is Not Valid")
        else:
            if self.__mentor_ID in self.mentor_dict:
                self.mentor_dict[self.__mentor_ID].update({'__first_name': first_name, '__last_name': last_name, '__date_of_birth': dob,
                                                          '__qualification': qualification, '__address':address, '__mobile': mob_num,
                                                          '__email': email_id, '__experience':experience, '__subject_expert': subject_expert})
            else:
                self.mentor_dict[self.get_mentor_ID] = {'__first_name': first_name, '__last_name': last_name, '__date_of_birth': dob,
                                                          '__qualification': qualification, '__address':address, '__mobile': mob_num,
                                                          '__email': email_id, '__experience':experience, '__subject_expert': subject_expert}

        open_mentor_file = open(self.mentor_file_path, 'w')
        json.dump(self.mentor_dict, open_mentor_file, indent=2)
        open_mentor_file.close()
        self.mentor_dict={}


    def load_mentor_dict(self):
        try:
            fp = open(self.mentor_file_path, 'r')
            self.mentor_dict = json.load(fp)
            fp.close()
            if self.__mentor_ID in self.mentor_dict:
                self.__first_name = self.mentor_dict[self.__mentor_ID]['__first_name']
                self.__last_name = self.mentor_dict[self.__mentor_ID]['__last_name']
                self.__date_of_birth = self.mentor_dict[self.__mentor_ID]['__date_of_birth']
                self.__qualification = self.mentor_dict[self.__mentor_ID]['__qualification']
                self.__address = self.mentor_dict[self.__mentor_ID]['__address']
                self.__mobile = self.mentor_dict[self.__mentor_ID]['__mobile']
                self.__email = self.mentor_dict[self.__mentor_ID]['__email']
                self.__experience = self.mentor_dict[self.__mentor_ID]['__experience']
                self.__subject_expert = self.mentor_dict[self.__mentor_ID]['__subject_expert']
            else:
                self.mentor_dict[self.__mentor_ID] = {}
        except:
            self.mentor_dict = {}
            print("Unable to load mentor config")


    @classmethod
    def generate_mentor_ID(cls):
        total_mentor_count = 1000
        id_num = str(random.randrange(1, total_mentor_count)).zfill(5)
        if loc == 'gachibowli':
            loc_tag = 'gb'
        elif loc == 'kukatpally':
            loc_tag = 'kp'
        elif loc == 'srnagar':
            loc_tag = 'sn'
        else:
            print("Location Not Valid")
        try:
            fp = open(mentor_config_file_path, 'r')
            mentor_ID_dict = json.load(fp)
            fp.close()
            if len(mentor_ID_dict)>=total_mentor_count:
                print("No Admission Available")
                return False
            if str('_'.join(['dl_mt', loc_tag, id_num])) in mentor_ID_dict.keys():
                return cls.generate_mentor_ID()
            else:
                return '_'.join(['dl_mt', loc_tag, id_num])
        except:
            return '_'.join(['dl_mt', loc_tag, id_num])

    @staticmethod
    def get_mentor_ID_list():
        try:
            fp = open(mentor_config_file_path, 'r')
            mentor_ID_dict = json.load(fp)
            fp.close()
            return mentor_ID_dict.keys()
        except:
            print("Unable to Load mentor Config")
            return []




