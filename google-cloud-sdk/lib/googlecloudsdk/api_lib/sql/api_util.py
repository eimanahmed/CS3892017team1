# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Common utility functions for getting the SQL API."""

from googlecloudsdk.api_lib.util import apis
from googlecloudsdk.core import properties
from googlecloudsdk.core import resolvers
from googlecloudsdk.core import resources

# API version constants
API_VERSION_DEFAULT = 'v1beta4'
API_VERSION_FALLBACK = 'v1beta3'


class SqlClient(object):
  """Wrapper for SQL API client and associated resources."""

  def __init__(self, api_version):
    self.sql_client = apis.GetClientInstance('sql', api_version)
    self.sql_messages = self.sql_client.MESSAGES_MODULE
    self.resource_parser = resources.Registry()
    self.resource_parser.RegisterApiByName('sql', api_version)
    self.resource_parser.SetParamDefault(
        api='sql', collection=None, param='project',
        resolver=resolvers.FromProperty(properties.VALUES.core.project))
