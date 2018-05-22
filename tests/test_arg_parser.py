import pytest
import context
import os
import sys
sys.path.append(os.path.join(context.base_dir, 'helpers'))
sys.path.append(os.path.join(context.src_dir, 'experiments'))
import arg_parser as mut # module under test


def test_parse_test_good(cmdline_good_config_file):
    args = mut.parse_test(cmdline_good_config_file)
    assert(hasattr(args, 'test_config'))
    assert(args.test_config is not None)
    assert('tests' in args.test_config)
    for test_description in args.test_config['tests'].values():
        assert('flows' in test_description)
    assert(args.runtime == 15) # check if cmdline arg value set correctly
    assert(args.interval == 0) # check if default value set correctly
    assert(args.mode == 'local')

def test_parse_test_bad(cmdline_bad_config_file):
    pass
    

