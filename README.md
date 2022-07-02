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

## Known Issues

If you receive the following error, please check if you are using an AdBlocker.

```javascript
TypeError: NetworkError when attempting to fetch resource.
```
