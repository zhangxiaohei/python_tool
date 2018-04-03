import argparse

# https://docs.python.org/3/library/argparse.html
def get_config_from_cmdline():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='count', default=0,
            help='Increase verbosity')
    parser.add_argument('--target', required=True, nargs='+',
        choices=['aaa', 'bbb', 'ccc', 'ddd'],
        help='Calculate target.')
    options = parser.parse_args()
    
    return options

    
import configparser

# https://docs.python.org/3/library/configparser.html
def get_config_from_file():
    config = configparser.ConfigParser()
    config.read('config.ini')
    for section in config.sections():
         for item in config[section]:
             print(item, config[section][item])
    
