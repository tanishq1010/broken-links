import os
import csv
import json
import string
import random
import requests
import sys
import traceback

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
        # self.host = 'https://preprodms.embibe.com'

    def callAPI(self, url, payload, method):
        self.headers[
            "embibe-token"] = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJyb2xlIjoic3R1ZGVudCIsInRpbWVfc3RhbXAiOiIyMDIwLTExLTAyIDA3OjM2OjM5IFVUQyIsImlzX2d1ZXN0IjpmYWxzZSwiaWQiOjM2MTU1OTQsImVtYWlsIjoiYzEzNDEzOGUwNDc1QGppby1lbWJpYmUuY29tIn0.wC4cNu2D6LAWpWfWPPVL_ErT6X5kW4MfXNNiQqxQw3CbVl_eZHbaScYpXvOY93axd1HU14ITXEvObmHG5sE9Hg'
        response = requests.request(method, url, headers=self.headers, data=payload)

        if response.status_code != 200:
            print(url + ' - ' + str(response.content))
            return None
        return response

    def main(self, df):
        df1 = pd.read_csv("broken links.csv")
        for ind in df.index:
            learnmap_id = df["Learnmap_id"][ind]
            learnpath_name = df["Learnpath_name"][ind]
            grade = df["Grade"][ind]
            goal=df["Goal"][ind]
            exam=df["Exam"][ind]
            subject=df["Subject"][ind]
            print("----------------new-----------------")
            print("------------------------------------")
            print(learnmap_id)
            # print(exam)
            print(exam)
            print(subject)
            print("\n")

            response1 = self.callAPI(
                "https://preprodms.embibe.com/fiber_ms/v1/chapters/learning-objects?&learnMapId=" + str(
                    learnmap_id) + "&contentTypes=Video",
                '{}', 'GET')

            try:
                print("all videos :" ,response1.status_code)

                if response1.status_code == 200:
                    videos = True
                else:
                    videos = False

            except Exception as e:
                print(traceback.format_exc())
                videos = False

            payload2 = {
                'learnmap_id': learnmap_id,
                'subject': df["Subject_tagged"][ind]
            }
            response2 = self.callAPI(
                "https://preprodms.embibe.com/fiber_ms/chapter/prerequisites",
                json.dumps(payload2), 'POST')
            # print(response2)
            try:
                print("all prerequisite :", response2.status_code)
                if response2.status_code == 200:
                    prerequisite = True
                else:
                    prerequisite = False
            except Exception as e:
                print(traceback.format_exc())
                prerequisite = False

            payload3 = {
                'learnmap_id': learnmap_id,
                'subject': df["Subject_tagged"][ind]
            }

            response3 = self.callAPI(
                "https://preprodms.embibe.com/fiber_ms/chapterTopics",
                json.dumps(payload3), 'POST')
            # print(response3.status_code)
            try:
                print("all topics :", response3.status_code)
                if response3.status_code == 200:
                    topics = True
                else:
                    topics = False
            except Exception as e:
                print(traceback.format_exc())
                topics = False

            payload4 = {
                'board': df["Goal"][ind],
                'chapter_name': df["Chapter"][ind],
                'child_id': int(df["Child_ID"][ind]),
                'exam': df["Exam"][ind],
                'goal': df["Goal"][ind],
                'grade': str(grade)
            }
            response4 = self.callAPI(
                "https://preprodms.embibe.com/fiber_ms/home/filter-test",
                json.dumps(payload4), 'POST')

            try:
                print("all tests :", response4.status_code)
                if response4.status_code == 200:
                    test = True
                else:
                    test = False
            except Exception as e:
                print(traceback.format_exc())
                test = False

            payload5 = {
                'learnmap_id': learnmap_id,
                'subject': df["Subject_tagged"][ind]
            }
            response5 = self.callAPI(
                "https://preprodms.embibe.com/fiber_ms/chapterPractices",
                json.dumps(payload5), 'POST')
            try:
                print("all practice :", response5.status_code)
                if response5.status_code == 200:
                    practice = True
                else:
                    practice = False
            except Exception as e:
                print(traceback.format_exc())
                practice = False
            df1.loc[len(df1)] = [df["Child_ID"][ind], df["Exam"][ind], df["Goal"][ind], df["Grade"][ind],
                                 df["Title"][ind], df["Type"][ind], df["Format_refrence"][ind], df["Section_name"][ind],
                                 df["Subject"][ind], df["Subject_tagged"][ind], df["Learnpath_name"][ind],
                                 df["Learnmap_id"][ind], df["Chapter"][ind], videos, topics, prerequisite, test,
                                 practice]
            df1.to_csv("broken links.csv",index=False)


def broken_link(df):
    src = Source()
    return src.main(df)

# goal_exam_grade_extractor()
