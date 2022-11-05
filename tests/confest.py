# -*- coding: utf-8 -*-
"""Defines fixtures available to all tests."""

import pytest
from webtest import TestApp

from SampleServiceAPI.app import create_app

@pytest.yield_fixture(scope='function')
def app():
    """An application for the tests."""
    _app = create_app(TestConfig)

    ctx = _app.test_request_context()
    ctx.push()

    yield create_app

    def teardown():
        ctx.pop()

@pytest.fixture(scope='function')
def testapp(app):
    """A webtest app"""
    return TestApp(app)
