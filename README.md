# kinto-github-token

Github Authentication support for Kinto

### Usage

```
# changes to kinto.ini

multiauth.policies = github
multiauth.policy.github.use = kinto_github_token.authentication.GithubAuthenticationPolicy
```

### Authentication Flow

####  Redirect users to request GitHub access
```
GET https://github.com/login/oauth/authorize
```

#### After Github redirects back to your site, obtain the `code` and issue a request to Kinto API to get the `access_token`
```
POST http://localhost:888/v1/github/token
```

#### Having the access_token, use it as authorization headers to request Kinto API, or pass it to kinto.js client
```
collection.sync({
  headers: {
    Authorization: 'github+bearer <your_token>'
  }
})
```

### TODO
[ ]  load github client_id & client_secret from kinto.ini

### Licence

### Authors

`kinto-github-token` was written by `Anh Trinh <anh.trinhtrung@gmail.com>`_.
