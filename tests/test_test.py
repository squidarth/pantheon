from __future__ import absolute_import

import pytest
import context
import os
import sys
sys.path.insert(0, os.path.join(context.src_dir, 'experiments'))
import test as mut

def test_parse(args):
    tests = mut.get_tests(args)
    if tests[0].cc == 'test-bbr-cubic':
        test_bbr_cubic = tests[0]
        test_bbr_2cubic = tests[1]
    else:
        test_bbr_cubic = tests[1]
        test_bbr_2cubic = tests[0]
        
    assert(test_bbr_cubic.flow_objs[1].cc == 'bbr')
    assert(test_bbr_cubic.flow_objs[2].cc == 'cubic')
    #['scheme':'bbr', 'scheme':'cubic'])
    assert(test_bbr_2cubic.cc == 'test-bbr-2cubic')
    assert(test_bbr_2cubic.flow_objs[1].cc == 'bbr')
    assert(test_bbr_2cubic.flow_objs[2].cc == 'cubic')
    assert(test_bbr_2cubic.flow_objs[3].cc == 'cubic')
    #['scheme':'bbr', 'scheme':'cubic', 'scheme':'cubic'])
    for test in tests:
        assert(test.mode == 'local')
        assert(test.run_id == 1)
        assert(test.flows == 1)
        assert(test.runtime == 15)
        assert(test.interval == 0)
        assert(test.run_times == 1)
    
