from goal_exam_extractor import goal_exam_grade_extractor
from home_data_extractor import home_data
import pandas as pd
from links import  broken_link

from login_sign_up import *
# from embibe_explainers_home import embibe_explainers_learn
# from CG_embibe_explainers import *


# from miscellaneous import *
# from home_data_continue_learning import home_data


def for_all_exam_goal(goal_exam_grade):
    for ind in goal_exam_grade.index:
        print(goal_exam_grade["Goal"][ind], goal_exam_grade["Exam_name"][ind])
        # signup_data = Signup()
        # login_data = login(signup_data[0], "embibe1234")
        # # child_data=add_user(signup_data[1],login_data[0])
        # embibe_token = login_data[1]
        # child_id = signup_data[1]
        home_data(3615594, goal_exam_grade["Goal"][ind], goal_exam_grade["Grade"][ind],
                  goal_exam_grade["Exam_name"][ind],
                  goal_exam_grade["Goal"][ind], 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJyb2xlIjoic3R1ZGVudCIsInRpbWVfc3RhbXAiOiIyMDIwLTExLTAyIDA3OjM2OjM5IFVUQyIsImlzX2d1ZXN0IjpmYWxzZSwiaWQiOjM2MTU1OTQsImVtYWlsIjoiYzEzNDEzOGUwNDc1QGppby1lbWJpYmUuY29tIn0.wC4cNu2D6LAWpWfWPPVL_ErT6X5kW4MfXNNiQqxQw3CbVl_eZHbaScYpXvOY93axd1HU14ITXEvObmHG5sE9Hg')


if __name__ == '__main__':
    # df_negative_results = pd.DataFrame(columns=['Child_ID', 'Exam', 'Goal', "Grade",
    #                                             'Title', 'Type', 'Format_refrence', 'Section_name', 'Subject',
    #                                             'Subject_tagged', 'Learnpath_name', 'Learnmap_id',"Chapter"])
    # df_positive_results = pd.DataFrame(columns=['Child_ID', 'Exam', 'Goal', "Grade",
    #                                             'Title', 'Type', 'Format_refrence', 'Section_name', 'Subject',
    #                                             'Subject_tagged', 'Learnpath_name', 'Learnmap_id',"Chapter"])
    # df_negative_results.to_csv("negative_learn_results.csv", index=False)
    # df_positive_results.to_csv("positive_learn_results.csv", index=False)
    df_links = pd.DataFrame(columns=['Child_ID', 'Exam', 'Goal', "Grade",
                                                'Title', 'Type', 'Format_refrence', 'Section_name', 'Subject',
                                                'Subject_tagged', 'Learnpath_name', 'Learnmap_id', "Chapter","all videos  api present","topics in this chapter api present","prerequisite topic api present","tests in this chapter api present","practice on this chapter api present"])
    df_links.to_csv("broken links.csv",index=False)
    # goal_exam_grade = goal_exam_grade_extractor()
    # df=pd.read_csv("goal_exams.csv")
    # for_all_exam_goal(goal_exam_grade)
    df=pd.read_csv("positive_learn_results.csv")

    broken_link(df)


    # df = pd.read_csv("positive_learn_results.csv")
    # embibe_explainers_learn(df)











