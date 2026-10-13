# Site tools

- `build.py` generates `index.html` and every `cases/*.html` from the content defined inside it. Edit the content there, never the generated HTML, then run `python3 tools/build.py .` from the site root.
- `og_*.html` are the 1200×627 link-preview cards. To re-render one, run Chrome headless:
  `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --hide-scrollbars --virtual-time-budget=5000 --window-size=1200,627 --screenshot="$PWD/og/<name>.png" "file://$PWD/tools/og_<name>.html"`
