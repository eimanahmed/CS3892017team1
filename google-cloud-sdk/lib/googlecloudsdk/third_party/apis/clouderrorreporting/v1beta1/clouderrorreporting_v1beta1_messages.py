"""Generated message classes for clouderrorreporting version v1beta1.

Stackdriver Error Reporting groups and counts similar errors from cloud
services. The Stackdriver Error Reporting API provides a way to report new
errors and read access to error groups and their associated errors.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding


package = 'clouderrorreporting'


class ClouderrorreportingProjectsDeleteEventsRequest(_messages.Message):
  """A ClouderrorreportingProjectsDeleteEventsRequest object.

  Fields:
    projectName: [Required] The resource name of the Google Cloud Platform
      project. Written as `projects/` plus the [Google Cloud Platform project
      ID](https://support.google.com/cloud/answer/6158840). Example: `projects
      /my-project-123`.
  """

  projectName = _messages.StringField(1, required=True)


class ClouderrorreportingProjectsEventsListRequest(_messages.Message):
  """A ClouderrorreportingProjectsEventsListRequest object.

  Enums:
    TimeRangePeriodValueValuesEnum: Restricts the query to the specified time
      range.

  Fields:
    groupId: [Required] The group for which events shall be returned.
    pageSize: [Optional] The maximum number of results to return per response.
    pageToken: [Optional] A `next_page_token` provided by a previous response.
    projectName: [Required] The resource name of the Google Cloud Platform
      project. Written as `projects/` plus the [Google Cloud Platform project
      ID](https://support.google.com/cloud/answer/6158840). Example: `projects
      /my-project-123`.
    serviceFilter_resourceType: [Optional] The exact value to match against
      [`ServiceContext.resource_type`](/error-
      reporting/reference/rest/v1beta1/ServiceContext#FIELDS.resource_type).
    serviceFilter_service: [Optional] The exact value to match against
      [`ServiceContext.service`](/error-
      reporting/reference/rest/v1beta1/ServiceContext#FIELDS.service).
    serviceFilter_version: [Optional] The exact value to match against
      [`ServiceContext.version`](/error-
      reporting/reference/rest/v1beta1/ServiceContext#FIELDS.version).
    timeRange_period: Restricts the query to the specified time range.
  """

  class TimeRangePeriodValueValuesEnum(_messages.Enum):
    """Restricts the query to the specified time range.

    Values:
      PERIOD_UNSPECIFIED: <no description>
      PERIOD_1_HOUR: <no description>
      PERIOD_6_HOURS: <no description>
      PERIOD_1_DAY: <no description>
      PERIOD_1_WEEK: <no description>
      PERIOD_30_DAYS: <no description>
    """
    PERIOD_UNSPECIFIED = 0
    PERIOD_1_HOUR = 1
    PERIOD_6_HOURS = 2
    PERIOD_1_DAY = 3
    PERIOD_1_WEEK = 4
    PERIOD_30_DAYS = 5

  groupId = _messages.StringField(1)
  pageSize = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(3)
  projectName = _messages.StringField(4, required=True)
  serviceFilter_resourceType = _messages.StringField(5)
  serviceFilter_service = _messages.StringField(6)
  serviceFilter_version = _messages.StringField(7)
  timeRange_period = _messages.EnumField('TimeRangePeriodValueValuesEnum', 8)


class ClouderrorreportingProjectsEventsReportRequest(_messages.Message):
  """A ClouderrorreportingProjectsEventsReportRequest object.

  Fields:
    projectName: [Required] The resource name of the Google Cloud Platform
      project. Written as `projects/` plus the [Google Cloud Platform project
      ID](https://support.google.com/cloud/answer/6158840). Example: `projects
      /my-project-123`.
    reportedErrorEvent: A ReportedErrorEvent resource to be passed as the
      request body.
  """

  projectName = _messages.StringField(1, required=True)
  reportedErrorEvent = _messages.MessageField('ReportedErrorEvent', 2)


class ClouderrorreportingProjectsGroupStatsListRequest(_messages.Message):
  """A ClouderrorreportingProjectsGroupStatsListRequest object.

  Enums:
    AlignmentValueValuesEnum: [Optional] The alignment of the timed counts to
      be returned. Default is `ALIGNMENT_EQUAL_AT_END`.
    OrderValueValuesEnum: [Optional] The sort order in which the results are
      returned. Default is `COUNT_DESC`.
    TimeRangePeriodValueValuesEnum: Restricts the query to the specified time
      range.

  Fields:
    alignment: [Optional] The alignment of the timed counts to be returned.
      Default is `ALIGNMENT_EQUAL_AT_END`.
    alignmentTime: [Optional] Time where the timed counts shall be aligned if
      rounded alignment is chosen. Default is 00:00 UTC.
    groupId: [Optional] List all <code>ErrorGroupStats</code> with these IDs.
    order: [Optional] The sort order in which the results are returned.
      Default is `COUNT_DESC`.
    pageSize: [Optional] The maximum number of results to return per response.
      Default is 20.
    pageToken: [Optional] A `next_page_token` provided by a previous response.
      To view additional results, pass this token along with the identical
      query parameters as the first request.
    projectName: [Required] The resource name of the Google Cloud Platform
      project. Written as <code>projects/</code> plus the <a
      href="https://support.google.com/cloud/answer/6158840">Google Cloud
      Platform project ID</a>.  Example: <code>projects/my-project-123</code>.
    serviceFilter_resourceType: [Optional] The exact value to match against
      [`ServiceContext.resource_type`](/error-
      reporting/reference/rest/v1beta1/ServiceContext#FIELDS.resource_type).
    serviceFilter_service: [Optional] The exact value to match against
      [`ServiceContext.service`](/error-
      reporting/reference/rest/v1beta1/ServiceContext#FIELDS.service).
    serviceFilter_version: [Optional] The exact value to match against
      [`ServiceContext.version`](/error-
      reporting/reference/rest/v1beta1/ServiceContext#FIELDS.version).
    timeRange_period: Restricts the query to the specified time range.
    timedCountDuration: [Optional] The preferred duration for a single
      returned `TimedCount`. If not set, no timed counts are returned.
  """

  class AlignmentValueValuesEnum(_messages.Enum):
    """[Optional] The alignment of the timed counts to be returned. Default is
    `ALIGNMENT_EQUAL_AT_END`.

    Values:
      ERROR_COUNT_ALIGNMENT_UNSPECIFIED: <no description>
      ALIGNMENT_EQUAL_ROUNDED: <no description>
      ALIGNMENT_EQUAL_AT_END: <no description>
    """
    ERROR_COUNT_ALIGNMENT_UNSPECIFIED = 0
    ALIGNMENT_EQUAL_ROUNDED = 1
    ALIGNMENT_EQUAL_AT_END = 2

  class OrderValueValuesEnum(_messages.Enum):
    """[Optional] The sort order in which the results are returned. Default is
    `COUNT_DESC`.

    Values:
      GROUP_ORDER_UNSPECIFIED: <no description>
      COUNT_DESC: <no description>
      LAST_SEEN_DESC: <no description>
      CREATED_DESC: <no description>
      AFFECTED_USERS_DESC: <no description>
    """
    GROUP_ORDER_UNSPECIFIED = 0
    COUNT_DESC = 1
    LAST_SEEN_DESC = 2
    CREATED_DESC = 3
    AFFECTED_USERS_DESC = 4

  class TimeRangePeriodValueValuesEnum(_messages.Enum):
    """Restricts the query to the specified time range.

    Values:
      PERIOD_UNSPECIFIED: <no description>
      PERIOD_1_HOUR: <no description>
      PERIOD_6_HOURS: <no description>
      PERIOD_1_DAY: <no description>
      PERIOD_1_WEEK: <no description>
      PERIOD_30_DAYS: <no description>
    """
    PERIOD_UNSPECIFIED = 0
    PERIOD_1_HOUR = 1
    PERIOD_6_HOURS = 2
    PERIOD_1_DAY = 3
    PERIOD_1_WEEK = 4
    PERIOD_30_DAYS = 5

  alignment = _messages.EnumField('AlignmentValueValuesEnum', 1)
  alignmentTime = _messages.StringField(2)
  groupId = _messages.StringField(3, repeated=True)
  order = _messages.EnumField('OrderValueValuesEnum', 4)
  pageSize = _messages.IntegerField(5, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(6)
  projectName = _messages.StringField(7, required=True)
  serviceFilter_resourceType = _messages.StringField(8)
  serviceFilter_service = _messages.StringField(9)
  serviceFilter_version = _messages.StringField(10)
  timeRange_period = _messages.EnumField('TimeRangePeriodValueValuesEnum', 11)
  timedCountDuration = _messages.StringField(12)


class ClouderrorreportingProjectsGroupsGetRequest(_messages.Message):
  """A ClouderrorreportingProjectsGroupsGetRequest object.

  Fields:
    groupName: [Required] The group resource name. Written as
      <code>projects/<var>projectID</var>/groups/<var>group_name</var></code>.
      Call <a href="/error-
      reporting/reference/rest/v1beta1/projects.groupStats/list">
      <code>groupStats.list</code></a> to return a list of groups belonging to
      this project.  Example: <code>projects/my-project-123/groups/my-
      group</code>
  """

  groupName = _messages.StringField(1, required=True)


class DeleteEventsResponse(_messages.Message):
  """Response message for deleting error events."""


class ErrorContext(_messages.Message):
  """A description of the context in which an error occurred. This data should
  be provided by the application when reporting an error, unless the error
  report has been generated automatically from Google App Engine logs.

  Fields:
    httpRequest: The HTTP request which was processed when the error was
      triggered.
    reportLocation: The location in the source code where the decision was
      made to report the error, usually the place where it was logged. For a
      logged exception this would be the source line where the exception is
      logged, usually close to the place where it was caught. This value is in
      contrast to `Exception.cause_location`, which describes the source line
      where the exception was thrown.
    user: The user who caused or was affected by the crash. This can be a user
      ID, an email address, or an arbitrary token that uniquely identifies the
      user. When sending an error report, leave this field empty if the user
      was not logged in. In this case the Error Reporting system will use
      other data, such as remote IP address, to distinguish affected users.
      See `affected_users_count` in `ErrorGroupStats`.
  """

  httpRequest = _messages.MessageField('HttpRequestContext', 1)
  reportLocation = _messages.MessageField('SourceLocation', 2)
  user = _messages.StringField(3)


class ErrorEvent(_messages.Message):
  """An error event which is returned by the Error Reporting system.

  Fields:
    context: Data about the context in which the error occurred.
    eventTime: Time when the event occurred as provided in the error report.
      If the report did not contain a timestamp, the time the error was
      received by the Error Reporting system is used.
    message: The stack trace that was reported or logged by the service.
    serviceContext: The `ServiceContext` for which this error was reported.
  """

  context = _messages.MessageField('ErrorContext', 1)
  eventTime = _messages.StringField(2)
  message = _messages.StringField(3)
  serviceContext = _messages.MessageField('ServiceContext', 4)


class ErrorGroup(_messages.Message):
  """Description of a group of similar error events.

  Fields:
    groupId: Group IDs are unique for a given project. If the same kind of
      error occurs in different service contexts, it will receive the same
      group ID.
    name: The group resource name. Example: <code>projects/my-
      project-123/groups/my-groupid</code>
    trackingIssues: Associated tracking issues.
  """

  groupId = _messages.StringField(1)
  name = _messages.StringField(2)
  trackingIssues = _messages.MessageField('TrackingIssue', 3, repeated=True)


class ErrorGroupStats(_messages.Message):
  """Data extracted for a specific group based on certain filter criteria,
  such as a given time period and/or service filter.

  Fields:
    affectedServices: Service contexts with a non-zero error count for the
      given filter criteria. This list can be truncated if multiple services
      are affected. Refer to `num_affected_services` for the total count.
    affectedUsersCount: Approximate number of affected users in the given
      group that match the filter criteria. Users are distinguished by data in
      the `ErrorContext` of the individual error events, such as their login
      name or their remote IP address in case of HTTP requests. The number of
      affected users can be zero even if the number of errors is non-zero if
      no data was provided from which the affected user could be deduced.
      Users are counted based on data in the request context that was provided
      in the error report. If more users are implicitly affected, such as due
      to a crash of the whole service, this is not reflected here.
    count: Approximate total number of events in the given group that match
      the filter criteria.
    firstSeenTime: Approximate first occurrence that was ever seen for this
      group and which matches the given filter criteria, ignoring the
      time_range that was specified in the request.
    group: Group data that is independent of the filter criteria.
    lastSeenTime: Approximate last occurrence that was ever seen for this
      group and which matches the given filter criteria, ignoring the
      time_range that was specified in the request.
    numAffectedServices: The total number of services with a non-zero error
      count for the given filter criteria.
    representative: An arbitrary event that is chosen as representative for
      the whole group. The representative event is intended to be used as a
      quick preview for the whole group. Events in the group are usually
      sufficiently similar to each other such that showing an arbitrary
      representative provides insight into the characteristics of the group as
      a whole.
    timedCounts: Approximate number of occurrences over time. Timed counts
      returned by ListGroups are guaranteed to be:  - Inside the requested
      time interval - Non-overlapping, and - Ordered by ascending time.
  """

  affectedServices = _messages.MessageField('ServiceContext', 1, repeated=True)
  affectedUsersCount = _messages.IntegerField(2)
  count = _messages.IntegerField(3)
  firstSeenTime = _messages.StringField(4)
  group = _messages.MessageField('ErrorGroup', 5)
  lastSeenTime = _messages.StringField(6)
  numAffectedServices = _messages.IntegerField(7, variant=_messages.Variant.INT32)
  representative = _messages.MessageField('ErrorEvent', 8)
  timedCounts = _messages.MessageField('TimedCount', 9, repeated=True)


class HttpRequestContext(_messages.Message):
  """HTTP request data that is related to a reported error. This data should
  be provided by the application when reporting an error, unless the error
  report has been generated automatically from Google App Engine logs.

  Fields:
    method: The type of HTTP request, such as `GET`, `POST`, etc.
    referrer: The referrer information that is provided with the request.
    remoteIp: The IP address from which the request originated. This can be
      IPv4, IPv6, or a token which is derived from the IP address, depending
      on the data that has been provided in the error report.
    responseStatusCode: The HTTP response status code for the request.
    url: The URL of the request.
    userAgent: The user agent information that is provided with the request.
  """

  method = _messages.StringField(1)
  referrer = _messages.StringField(2)
  remoteIp = _messages.StringField(3)
  responseStatusCode = _messages.IntegerField(4, variant=_messages.Variant.INT32)
  url = _messages.StringField(5)
  userAgent = _messages.StringField(6)


class ListEventsResponse(_messages.Message):
  """Contains a set of requested error events.

  Fields:
    errorEvents: The error events which match the given request.
    nextPageToken: If non-empty, more results are available. Pass this token,
      along with the same query parameters as the first request, to view the
      next page of results.
    timeRangeBegin: The timestamp specifies the start time to which the
      request was restricted.
  """

  errorEvents = _messages.MessageField('ErrorEvent', 1, repeated=True)
  nextPageToken = _messages.StringField(2)
  timeRangeBegin = _messages.StringField(3)


class ListGroupStatsResponse(_messages.Message):
  """Contains a set of requested error group stats.

  Fields:
    errorGroupStats: The error group stats which match the given request.
    nextPageToken: If non-empty, more results are available. Pass this token,
      along with the same query parameters as the first request, to view the
      next page of results.
    timeRangeBegin: The timestamp specifies the start time to which the
      request was restricted. The start time is set based on the requested
      time range. It may be adjusted to a later time if a project has exceeded
      the storage quota and older data has been deleted.
  """

  errorGroupStats = _messages.MessageField('ErrorGroupStats', 1, repeated=True)
  nextPageToken = _messages.StringField(2)
  timeRangeBegin = _messages.StringField(3)


class ReportErrorEventResponse(_messages.Message):
  """Response for reporting an individual error event. Data may be added to
  this message in the future.
  """



class ReportedErrorEvent(_messages.Message):
  """An error event which is reported to the Error Reporting system.

  Fields:
    context: [Optional] A description of the context in which the error
      occurred.
    eventTime: [Optional] Time when the event occurred. If not provided, the
      time when the event was received by the Error Reporting system will be
      used.
    message: [Required] The error message. If no `context.reportLocation` is
      provided, the message must contain a header (typically consisting of the
      exception type name and an error message) and an exception stack trace
      in one of the supported programming languages and formats. Supported
      languages are Java, Python, JavaScript, Ruby, C#, PHP, and Go. Supported
      stack trace formats are:  * **Java**: Must be the return value of [`Thro
      wable.printStackTrace()`](https://docs.oracle.com/javase/7/docs/api/java
      /lang/Throwable.html#printStackTrace%28%29). * **Python**: Must be the
      return value of [`traceback.format_exc()`](https://docs.python.org/2/lib
      rary/traceback.html#traceback.format_exc). * **JavaScript**: Must be the
      value of [`error.stack`](https://github.com/v8/v8/wiki/Stack-Trace-API)
      as returned by V8. * **Ruby**: Must contain frames returned by
      [`Exception.backtrace`](https://ruby-
      doc.org/core-2.2.0/Exception.html#method-i-backtrace). * **C#**: Must be
      the return value of [`Exception.ToString()`](https://msdn.microsoft.com
      /en-us/library/system.exception.tostring.aspx). * **PHP**: Must start
      with `PHP (Notice|Parse error|Fatal error|Warning)` and contain the
      result of
      [`(string)$exception`](http://php.net/manual/en/exception.tostring.php).
      * **Go**: Must be the return value of
      [`runtime.Stack()`](https://golang.org/pkg/runtime/debug/#Stack).
    serviceContext: [Required] The service context in which this error has
      occurred.
  """

  context = _messages.MessageField('ErrorContext', 1)
  eventTime = _messages.StringField(2)
  message = _messages.StringField(3)
  serviceContext = _messages.MessageField('ServiceContext', 4)


class ServiceContext(_messages.Message):
  """Describes a running service that sends errors. Its version changes over
  time and multiple versions can run in parallel.

  Fields:
    resourceType: Type of the MonitoredResource. List of possible values:
      https://cloud.google.com/monitoring/api/resources  Value is set
      automatically for incoming errors and must not be set when reporting
      errors.
    service: An identifier of the service, such as the name of the executable,
      job, or Google App Engine service name. This field is expected to have a
      low number of values that are relatively stable over time, as opposed to
      `version`, which can be changed whenever new code is deployed.  Contains
      the service name for error reports extracted from Google App Engine logs
      or `default` if the App Engine default service is used.
    version: Represents the source code version that the developer provided,
      which could represent a version label or a Git SHA-1 hash, for example.
      For App Engine standard environment, the version is set to the version
      of the app.
  """

  resourceType = _messages.StringField(1)
  service = _messages.StringField(2)
  version = _messages.StringField(3)


class SourceLocation(_messages.Message):
  """Indicates a location in the source code of the service for which errors
  are reported. `functionName` must be provided by the application when
  reporting an error, unless the error report contains a `message` with a
  supported exception stack trace. All fields are optional for the later case.

  Fields:
    filePath: The source code filename, which can include a truncated relative
      path, or a full path from a production machine.
    functionName: Human-readable name of a function or method. The value can
      include optional context like the class or package name. For example,
      `my.package.MyClass.method` in case of Java.
    lineNumber: 1-based. 0 indicates that the line number is unknown.
  """

  filePath = _messages.StringField(1)
  functionName = _messages.StringField(2)
  lineNumber = _messages.IntegerField(3, variant=_messages.Variant.INT32)


class StandardQueryParameters(_messages.Message):
  """Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    bearer_token: OAuth bearer token.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    pp: Pretty-print response.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    """Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    """V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default=u'json')
  bearer_token = _messages.StringField(4)
  callback = _messages.StringField(5)
  fields = _messages.StringField(6)
  key = _messages.StringField(7)
  oauth_token = _messages.StringField(8)
  pp = _messages.BooleanField(9, default=True)
  prettyPrint = _messages.BooleanField(10, default=True)
  quotaUser = _messages.StringField(11)
  trace = _messages.StringField(12)
  uploadType = _messages.StringField(13)
  upload_protocol = _messages.StringField(14)


class TimedCount(_messages.Message):
  """The number of errors in a given time period. All numbers are approximate
  since the error events are sampled before counting them.

  Fields:
    count: Approximate number of occurrences in the given time period.
    endTime: End of the time period to which `count` refers (excluded).
    startTime: Start of the time period to which `count` refers (included).
  """

  count = _messages.IntegerField(1)
  endTime = _messages.StringField(2)
  startTime = _messages.StringField(3)


class TrackingIssue(_messages.Message):
  """Information related to tracking the progress on resolving the error.

  Fields:
    url: A URL pointing to a related entry in an issue tracking system.
      Example: https://github.com/user/project/issues/4
  """

  url = _messages.StringField(1)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv',
    package=u'clouderrorreporting')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1',
    package=u'clouderrorreporting')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2',
    package=u'clouderrorreporting')
