#!/bin/bash
test -e ssshtest ||  wget -q http://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_error_handling python collision_resolution.py --hash_fxn FNV --col_res ChainedHash --filename data/non_rand_words.txt --out_id figures/example_nonrand_
assert_exit_code 0
assert_no_stdout


run test_invalid_input python collision_resolution.py --hash_fxn FNV --col_res Nope --filename data/non_rand_words.txt --out_id figures/example_nonrand_
assert_exit_code 2
assert_in_stderr usage:


run test_invalid_file python collision_resolution.py --hash_fxn FNV --col_res Nope --filename no_file --out_id yo
assert_exit_code 2
assert_in_stderr collision_resolution

run test_invalid_file python collision_resolution.py --hash_fxn FNV --col_res Nope --filename data --out_id data
assert_exit_code 2
assert_in_stderr collision_resolution