kinto-github-token
==================

Github Authentication support for Kinto

Usage
-----

Add Github Authentication to Kinto API

```
multiauth.policies = github
multiauth.policy.github.use = kinto_github_token.authentication.GithubAuthenticationPolicy

```

* Step 1: Redirect users to request GitHub access
  ```
  GET https://github.com/login/oauth/authorize
  ```

* Step 2: After Github redirects back to your site, obtain the `code` and issue a request to Kinto API to get the `access_token`
  ```
  POST http://localhost:888/v1/github/token
  ```

TODO
-------------
[ ]  load github client_id & client_secret from kinto.ini

Licence
-------

Authors
-------

`kinto-github-token` was written by `Anh Trinh <anh.trinhtrung@gmail.com>`_.
