import matplotlib.pyplot as plt
import numpy as np
import posixpath
import json
import time
import os
import config

from location import DLLocation
from collections import defaultdict


root_file_path = posixpath.join(os.path.dirname(__file__), 'config')

class digital_lync_chart:
    def __init__(self, location=''):
        if location:
            self.loc = location
        else:
            self.loc = DLLocation().location
        self.list_of_courses = config.DigitalLoc().courses
        self.student_cofig_path = posixpath.join(root_file_path, 'students', '{}.json'.format(self.loc))
        if os.path.exists(self.student_cofig_path):
            student_fp = open(self.student_cofig_path, 'r')
            self.student_stat_dict = json.load(student_fp)
            student_fp.close()
        else:
            self.student_stat_dict = {}
        self.mentor_config_path = posixpath.join(root_file_path, '/mentors', self.loc + '.json')
        if os.path.exists(self.mentor_config_path):
            mentor_fp = open(self.mentor_config_path, 'r')
            self.mentor_stat_dict = json.load(mentor_fp)
            mentor_fp.close()
        else:
            self.mentor_stat_dict = {}
        self.fig, self.ax = plt.subplots()


    def get_total_student_count(self):
        return len(self.student_stat_dict)

    def get_total_mentor_count(self):
        return len(self.mentor_stat_dict)

    def get_student_course_count(self):
        student_course_count_dict = {}
        for course_item in self.list_of_courses:
            student_course_count_dict[course_item] = 0
            if not self.student_stat_dict:
                continue
            for student_item in self.student_stat_dict:
                if course_item.lower() in self.student_stat_dict[student_item]['__courses_opted']:
                    student_course_count_dict[course_item] += 1
                else:
                    continue
        return student_course_count_dict

    def plot_student_chart(self):
        print("Plotting Student chart...")
        course_label = []
        course_size = []
        for item, count in self.get_student_course_count().items():
            course_label.append(item)
            course_size.append(count)
        plt.rc('font', size=8)
        self.fig.set_size_inches(12.0, 5.0)
        y_pos = np.arange(len(course_label))
        self.ax.barh(y_pos, course_size, align='center', alpha=0.5, color='green')
        self.ax.set_yticks(y_pos)
        self.ax.set_yticklabels(course_label)
        self.ax.set_ylabel('Courses')
        self.ax.invert_yaxis()
        self.ax.set_xlabel('Number Of Students (Total: {})'.format(str(self.get_total_student_count())))
        self.ax.set_title('Digital Lync Student')
        plt.savefig('./assets/stat_data/student_count_bar.png')
        time.sleep(2)
        # plt.show()

    def plot_mentor_chart(self):
        pass


if __name__ == "__main__":
    inst = digital_lync_chart()
    inst.plot_student_chart()
