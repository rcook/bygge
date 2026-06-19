from __future__ import annotations

import os
from unittest.mock import patch

from bygge.util.env import env_truthy


def test_env_truthy_basics() -> None:
    with patch.dict(os.environ, {"OTHER_NAME1": "0", "OTHER_NAME2": "1"}, clear=True):
        assert env_truthy("NAME", default=True)
        assert not env_truthy("NAME", default=False)
        assert not env_truthy("OTHER_NAME1")
        assert env_truthy("OTHER_NAME2")
