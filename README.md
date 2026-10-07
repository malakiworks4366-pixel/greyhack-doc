# Grey Hack Docs

Unofficial community documentation for the game **Grey Hack**: gameplay, the terminal, GreyScript, and popular player-made tools. Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and published to GitHub Pages.

## Local preview

```bash
pip install -r requirements.txt
mkdocs serve
```

## Deploy

`.github/workflows/pages.yml` builds the site with `mkdocs build --strict` and deploys it on every push to `main`. Enable it under **Settings → Pages → Source: GitHub Actions**.
