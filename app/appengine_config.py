# Copyright (c) 2012, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

import os
import re

from google.appengine.api import namespace_manager

_PRODUCTION_DATABASE_VERSIONS = ['preview', 'coming-soon']
"""The versions of pub.dartlang.org that should use the production database.

In addition to these versions, any version that's just a number will use the
production database."""

def namespace_manager_default_namespace_for_request():
    """Choose which namespace to use for a given request.

    The database, task queue, and memcache are all automatically partitioned
    based on the current namespace. We use two namespaces: the empty string for
    the production environment, and "staging" for the staging environment.
    """
    version = os.environ.get('CURRENT_VERSION_ID')
    version_name = version.split('.')[0]
    if version_name in _PRODUCTION_DATABASE_VERSIONS or \
            re.match(r"^[0-9]+$", version_name):
        return ""
    return "staging"
