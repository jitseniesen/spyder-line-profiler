"""
Test whether spyder_line_profiler can be imported.

Importing spyder_line_profiler requires a running X server on Linux,
so this Python file is run inside an Xvfb (X virtual framebuffer)
using xvfb-run. For this reason, we cannot use an import stanza in the
test section in meta.yaml.
"""

import spyder_line_profiler
