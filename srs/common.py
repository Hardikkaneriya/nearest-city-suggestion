import pandas as pd
import sys
import json

from log import log_details
log= log_details()

def read_csv(path):
    try:
        log.info('Reading csv file from path.....')
        df= pd.read_csv(path)
        log.info('Data reading complete.....')
        log.info('Record count {}'.format(df.shape))

        if df.empty:
            log.exception('there are no record to process')
            sys.exit(1)
        return df
    except Exception as e :
        log.exception('Error while reading csv file from path with error message {}'.format(e))

def remove_null(df):
    try:
        log.info('checking null values in dataframe.....')
        drop_null_df= df.dropna()
        log.info('Dropped {} records with null values '.format(len(df)-len(drop_null_df)))
    except Exception as e :
        log.exception('Error while dropping null values with error message'.format(e))
    return drop_null_df

def remove_duplicate(df):
    try:
        log.info('checking duplicate records in dataframe.....')
        drop_duplicate_df= df.drop_duplicates()
        log.info('Dropped {} duplicate records '.format(len(df)-len(drop_duplicate_df)))
    except Exception as e :
        log.exception('Error while removing duplicate records with message'.format(e))
    return drop_duplicate_df

def save_json(df):
    try:
        #df.to_json('/Users/HKaner/Desktop/HK/Tour/output/output.json')
        log.info('writing output into json format.....')
        df.to_json('./output/output.json')
        log.info('output saved in json format in ./output/ folder ')
    except Exception as e :
        log.exception('Error while storing output'.format(e))
