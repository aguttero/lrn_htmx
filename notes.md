# Prod Env Setup
## self-host htmx
Self-Host HTMX: Do not use the CDN link (unpkg.com) in production. Download the htmx.min.js file, put it into your app/static/js/ directory, and load it locally. This removes an external network point-of-failure and guarantees your JS file cannot be modified upstream.
