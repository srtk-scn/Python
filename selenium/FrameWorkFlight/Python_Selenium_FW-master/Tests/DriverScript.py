import unittest
import HtmlTestRunner
import sys
import json
import os

if len(sys.argv) < 1:
    raise ValueError('Please provide the name of DriverScript')

# Add Project Folder path to sys.path
sys.path.insert(0, '../')


def uniques_only(iterable, key=None):
    seen = set()
    unique = []
    for item in iterable:
        val = item if key is None else key(item)
        if val not in seen:
            seen.add(val)
            unique.append(item)
    return unique


def get_test_data(test_case):
    with open('test_data.json', 'r') as f:
        json_file = json.load(f)
        for data in json_file:
            if test_case in data.keys():
                return data.get(test_case)
        raise KeyError('Test case name not found in test_data file')


def get_failed_suite(t_result):
    f_tests = [fail.test_name for fail in t_result.failures]
    f_tests += [error.test_name for error in t_result.errors]
    return f_tests


def write_failed_tests(f_tests):
    final = []
    with open('test_suite_failed.json', 'w') as f:
        for item in f_tests:
            t_dict = {"name": item.split('.')[0], "execute": "Yes"}
            t_tests = [t.split('.')[1] + '.py' for t in f_tests if t.split('.')[0] == item.split('.')[0]]
            t_dict.update({"tests": t_tests})
            final.append(t_dict)
        unique_tests = uniques_only(final, key=lambda d: d.get('name'))
        json.dump(unique_tests, f, indent=2)


def run(t_tests):
    loader = unittest.TestLoader()
    temp_suite = [loader.discover(os.getcwd(), pattern=test) for test in t_tests]
    if temp_suite:
        suite = unittest.TestSuite(temp_suite)
        runner = HtmlTestRunner.HTMLTestRunner(output=os.getcwd() + '/' + 'reports',
                                               report_title='Sanity_Test', descriptions='Smoke', add_timestamp=True,
                                               combine_reports=True, report_name='Test_Results')
        test_result = runner.run(suite)
        failed_tests = get_failed_suite(test_result)
        write_failed_tests(failed_tests)


if len(sys.argv) > 1:
    if sys.argv[1].endswith('.json'):
        with open(sys.argv[1], 'r') as j:
            run_tests = []
            test_suite = json.load(j)
            for module in test_suite:
                if module.get('execute').lower() == 'yes':
                    run_tests += [test for test in module.get('tests')]
            run(run_tests)
    else:
        t = [temp_test for temp_test in sys.argv[1:] if temp_test.endswith('.py')]
        print('Running tests ', t)
        run(t)
elif len(sys.argv) == 1:
    from Data import *
    to_run_tests = get_modules_to_execute()
    print(to_run_tests)
    run(to_run_tests)
else:
    raise TypeError('Incorrect number of arguments in command line')
