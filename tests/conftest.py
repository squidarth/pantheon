import pytest
import os
import context
import sys
sys.path.append(os.path.join(context.base_dir, 'helpers'))
sys.path.append(os.path.join(context.src_dir, 'experiments'))
from helpers import utils
import arg_parser

@pytest.fixture
def cmdline_good_config_file(request):
    sample_config_file = ('tests: \n' 
                          '    test-bbr-cubic: \n' 
                          '        flows: \n'
                          '            - scheme: bbr \n'
                          '            - scheme: cubic \n'
                          '    test-bbr-2cubic: \n'
                          '        flows: \n'
                          '            - scheme: bbr \n'
                          '            - scheme: cubic \n'
                          '            - scheme: cubic')
    config_name = 'good_config_file.yml'
    config_path = os.path.join(utils.tmp_dir, config_name)
    with open(config_path, 'w') as f:
        f.write(sample_config_file)
    def remove_tmp_test_file():
        if os.path.isfile(config_path):
            os.remove(config_path)
        # delete sample config file when done
    request.addfinalizer(remove_tmp_test_file)
    return ['-c', config_path, 'local', '--runtime', '15', '--pkill-cleanup']

@pytest.fixture
def args(cmdline_good_config_file):
    args = arg_parser.parse_test(cmdline_good_config_file)
    return args
