#coding=utf-8

# -*- coding:utf-8 -*-
import pytest
@pytest.fixture(scope='function')
def setup_function(n):
    return n

# @pytest.fixture(scope='module')
# def setup_module(request):
#     def teardown_module():
#         print("teardown_module called.")
#     request.addfinalizer(teardown_module)
#     print('setup_module called.')

# @pytest.mark.website
def test_1():
    assert setup_function(3) == 4

def test_2():
    assert setup_function(3) == 3

def test_3():
    # print('Test_3 called.')
    assert 2==1+1              # 通过assert断言确认测试结果是否符合预期