import os
import csv
import json
import string
import random
import requests
import sys

import pandas as pd
from openpyxl import Workbook, load_workbook


class Source(object):
    def __init__(self):
        super(Source, self).__init__()
        self.headers = {
            'Connection': 'keep-alive',
            'Accept': '*/*',
            'Content-Type': 'application/json',
        }
        self.host = 'https://preprodms.embibe.com'

    def callAPI(self, url, payload, method):
        response = requests.request(method, self.host + url, headers=self.headers, data=payload)
        if response.status_code != 200:
            print(url + ' - ' + str(response.content))
            return None
        return response

    def main(self):

        response1 = self.callAPI('/content_ms_fiber/v1/embibe/en/fiber-countries-goals-exams', "{}", 'GET')
        home_data = []
        if response1.status_code == 200 and response1.json()["success"] == True:
            for goal in response1.json()["data"]:
                _goal = goal["display_name"]
                if _goal == 'CBSE' or _goal == 'Banking' or _goal == 'Engineering' or _goal == 'Medical':

                    for exam in goal["exam"]:
                        # home = []

                        if str(exam["grade"]) != "None":
                            home_data.append([_goal, str(exam["grade"]), str(exam["name"])])

        df = pd.DataFrame(data=home_data, columns=["Goal", "Grade", "Exam_name"])



        return df


def goal_exam_grade_extractor():
    src = Source()
    return src.main()

# goal_exam_grade_extractor()
