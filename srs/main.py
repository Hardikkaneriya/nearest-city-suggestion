import argparse
import common as common
from log import log_details
import sys
import re
import os


log = log_details()
log.handlers.pop()

def data_process(df,args_dict):
    try:
        city= args_dict['city_name'].lower()
        duration= int(args_dict['duration'])
        filter= (df["connection"].str.lower().str.contains(city, na=False)) & ( df["duration"] <= duration)
        df1=df.loc[filter]
        return df1
    except:
        log.exception('Failed during data filtering')
        sys.exit(1)


def get_city_names(df,source):
    try:
        destination = df['connection'].str.replace("<>","").str.replace(source,"",flags=re.I)
        return destination.tolist()
    except:
        log.exception('Failed while collecting city names')
        sys.exit(1)
        
def main(args):
    parser = argparse.ArgumentParser(description='Nearby Places locator')
    parser.add_argument('--city_name', required=True, default='',help='city name')
    parser.add_argument('--duration', required=True, default='',help='duration')

    args = parser.parse_args()
    args_dict = vars(args)
    log.info("Received Arguments...")
    log.info(args_dict)

    input_df= common.read_csv(os.getcwd()+'/input/input.csv')
    remove_null_df= common.remove_null(input_df)
    remove_duplicate_df=common.remove_duplicate(remove_null_df)

    filtered_df=data_process(remove_duplicate_df,args_dict)
    print(filtered_df)
    if filtered_df.empty:
        log.info("No such record found")
    else:
        print('Output : {}'.format(get_city_names(filtered_df,args_dict['city_name'])))
        common.save_json(filtered_df)

if __name__ == '__main__':
    log.info("Job execution started.......")
    main(sys.argv[1:])
    log.info("*" * 20 + " Job completed " + "*" * 20)
