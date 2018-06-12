"""
--------------
Video fixtures
--------------
"""

import os
import sys

import allure
import pytest

from ui_tests import config
from ui_tests.helpers import process_mutex
from ui_tests.helpers.video_recorder import VideoRecorder

if sys.platform != 'win32':
    import xvfbwrapper


@pytest.fixture(scope='session')
def virtual_display(request, variables):
    """Session fixture to run test in virtual X server."""
    vdisplay = None
    is_enabled = request.config.option.enable_virtual_display

    if is_enabled:
        vdisplay = xvfbwrapper.Xvfb(*variables['resolution'])
        args = ["-noreset", "-ac"]

        vdisplay.extra_xvfb_args.extend(args)

        with process_mutex.Lock(config.XVFB_LOCK):
            vdisplay.start()

    yield

    if is_enabled:
        vdisplay.stop()


@pytest.fixture(autouse=True)
def video_capture(request, variables, virtual_display, report_dir):
    """Autouse function fixture to capture video of test."""
    recorder = None
    is_enabled = request.config.option.enable_video_capture

    if is_enabled:
        recorder = VideoRecorder(os.path.join(report_dir, 'video.mp4'), variables['resolution'])
        recorder.start()

    yield

    if is_enabled:
        recorder.stop()
        with open(recorder.file_path, 'rb') as video_file:
            allure.attach(video_file.read(),
                          'video',
                          allure.attachment_type.MP4)
