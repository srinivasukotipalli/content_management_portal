# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01QuestionCreationAPITestCase::test_case status'] = 201

snapshots['TestCase01QuestionCreationAPITestCase::test_case body'] = {
    'problem_description': {
        'content': 'string',
        'content_type': 'MARKDOWN'
    },
    'question_id': 1,
    'short_title': 'string'
}

snapshots['TestCase01QuestionCreationAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '117',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'text/html; charset=utf-8'
    ],
    'vary': [
        'Accept-Language, Origin, Cookie',
        'Vary'
    ],
    'x-frame-options': [
        'SAMEORIGIN',
        'X-Frame-Options'
    ]
}
