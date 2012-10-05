# Copyright (c) 2012, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

import os

from google.appengine.api import namespace_manager

def namespace_manager_default_namespace_for_request():
    """Choose which namespace to use for a given request.

    The database, task queue, and memcache are all automatically partitioned
    based on the current namespace. We use two namespaces: the empty string for
    the production environment, and "staging" for the staging environment.
    """
    version = os.environ.get('CURRENT_VERSION_ID')
    if version.startswith('1.') or version.startswith('preview.'): return ""
    return "staging"