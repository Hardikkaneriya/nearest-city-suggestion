import pytest
import pandas as pd
import numpy as np
from srs.common import remove_duplicate,remove_null,read_csv
import srs.log
from srs.main import  main,get_city_names
from unittest import  mock
import argparse


@pytest.fixture
def df():
    # read testing data
    #df = read_csv('/Users/HKaner/Desktop/HK/Tour/input/test.csv')
    df = read_csv('./input/test.csv')
    return df

def test_columns_present(df):
    # ensures that the expected columns are all present
    assert "connection" in df.columns
    assert "distance" in df.columns
    assert "duration" in df.columns

def test_non_empty( df):
    # ensures that there is more than one row of data
    assert len(df.index) != 0

def test_remove_null(df):
    # ensure that we have removed the null value rows from dataframe
    expected_df_count= (5,3)
    ad=remove_null(df)
    assert ad.shape == expected_df_count

def test_remove_duplicate(df):
    # ensure that we have removed the duplicate value rows from dataframe
    expected_df_count= (6,3)
    ad=remove_duplicate(df)
    assert ad.shape == expected_df_count

@mock.patch('main.get_city_names')
def test_main_a(get_city_names):
    # main(['--city_name', 'Berlin','--durartion','10'])
    city_lst= get_city_names(df,'Berlin')
    assert city_lst == ['Prague']

