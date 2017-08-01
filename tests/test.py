# -*- coding: utf-8 -*-
import unittest
from app import app
from werkzeug.exceptions import HTTPException

class TestCase(unittest.TestCase):


    #创建测试客户端
    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        rv = self.app.get('/index/')
        assert "frontend index" in rv.data

    def test_404(self):
        rv = self.app.get('/404')
        assert "not found" in rv.data