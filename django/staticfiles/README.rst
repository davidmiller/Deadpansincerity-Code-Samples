Serving Authenticated Static Files With Django Nginx & A.N. Webserver
=====================================================================

* Protected model overrides storage so that document.url prepends /icanhaz
* Request comes to /icanhaz/file.ext
* View evaluates authentication level
* If allowed, passes to an internal only Nginx alias with appropriate headers
* If not, either redirects to login, or returns 'No' (Forbidden)
