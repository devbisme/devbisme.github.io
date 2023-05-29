#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = "Dave Vandenbout"
SITENAME = "No Direction Home"

# For local dev, use a blank site URL.
SITEURL = ""

TIMEZONE = "America/New_York"

DEFAULT_LANG = "en"

THEME = "themes/chunk"
# THEME = 'themes/pelican-simplegrey'
# THEME = 'themes/gum'
# THEME = 'foundation-default-colours'
# THEME = 'mg'

# Path where content is stored.
PATH = "content"

# Additional paths to include in output.
STATIC_PATHS = [
    "images",
    "misc",
    "files",
]

EXTRA_PATH_METADATA = {
    # Copy favicon to root directory.
    "images/favicon.ico": {"path": "favicon.ico"},
    # Place at top-level to disable Github Jekyll.
    "misc/.nojekyll": {"path": ".nojekyll"},
}

# PLUGINS = ["jinja2content"]

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {},
    },
    "output_format": "html5",
}

# Save blog posts using slug-date to prevent name conflicts.
ARTICLE_SAVE_AS = "{slug}-{date:%Y}-{date:%m}-{date:%d}.html"
ARTICLE_URL = ARTICLE_SAVE_AS

# Set the length of the summary in the listing of posts.
SUMMARY_MAX_LENGTH = 50

# Keep .nojekyll around even if output directory is cleared.
OUTPUT_RETENTION = [".nojekyll"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Remove all footer text.
FOOTER_TEXT = " "

# Menu. Mirror any changes here in publishconf.py!
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
#    ("Github", "https://github.com/devbisme/devbisme.github.io"),
    ('About', '/pages/about.html'),
    ("Forum", "https://github.com/devbisme/devbisme.github.io/discussions"),
    ("Home", f"{SITEURL}/"),
)

# Blogroll
LINKS = (
    # ('About', '/pages/about.html'),
    # ('Source', 'https://github.com/devbisme/devbisme.github.io'),
    # ('Home', '/')
)

# Social widget
SOCIAL = (
#     ("You can add links in your config file", "#"),
    ("Twitter", "@devbisme"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
