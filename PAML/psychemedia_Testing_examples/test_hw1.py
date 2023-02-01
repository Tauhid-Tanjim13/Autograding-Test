from pages import explore_dataset
import pandas as pd
import pytest

class ExampleClass:
    property = None
########################### Check Point 1 ######################################
def test_uploader():
    #print(type(explore_dataset.file_uploader()))
    #print(type(ExampleClass.property))
    print(explore_dataset.file_uploader())
    assert isinstance(explore_dataset.file_uploader(),type(ExampleClass.property)) 

print(explore_dataset.file_uploader())
test_filepath ="test_datasets/housing.csv"
student_filepath ="datasets/housing/housing.csv"


def test_uploaded_dataframe(s_filepath=student_filepath,t_filepath=test_filepath):
    student_dataframe= explore_dataset.read_uploaded_file(s_filepath)
    expected_dataframe = pd.read_csv(t_filepath)
    pd.testing.assert_frame_equal(student_dataframe,expected_dataframe)
#####################################################################################


test_dataframe = pd.read_csv(test_filepath)
student_dataframe = pd.read_csv(student_filepath)

########### Check point 2 ################# still trying to figure out 
def test_display_features(s_dataframe= student_dataframe,t_dataframe= test_dataframe):
    a = len(t_dataframe.columns)
    assert a==explore_dataset.display_features(s_dataframe)
#################################################

########################## Checkpoint 3 #########################



######################################################

