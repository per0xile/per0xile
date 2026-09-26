
import hashlib
import json
import math
import os
import re
import secrets
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


STATE_FILE = Path(".readme-langs.json")
README_FILE = Path("README.md")
SVG_FILE = Path("stats.svg")
