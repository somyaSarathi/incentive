"""IT service desk request generation and processing module.
Copyright (C) 2024  SOMYA SARATHI SAMAL

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import json
from random import shuffle

import requests
import numpy as np
import pandas as pd

from gemini_wrap import Gemini
from config import PROMPT, USERS, URL


def create_it_request(num: int = 6, timeout: int = 100) -> str:
    """Generate a specified number of simulated IT support tickets.

    Args:
        num: Number of IT requests to generate (default: 6)
        timeout: Maximum time in seconds to wait for Gemini API response (default: 100)

    Returns:
        str: JSON string containing the generated ticket data with fields:
            - request description (generated via Gemini)
            - estimated delay time (30-65 minutes)
            - requesting user (randomly assigned)
    """
    prompt = PROMPT.replace("{}", str(num))

    jsn = "\n".join(Gemini.generate(message=prompt, timeout=timeout).splitlines()[1:-1])

    df = pd.DataFrame(json.loads(jsn))
    df['delay'] = np.random.randint(low=30, high=65, size=len(df))

    shuffle(USERS)
    df['request_reported_by'] = USERS[:len(df)]

    json_string = df.to_json(orient="records", index=False)

    return json.loads(json_string)


def run_power_automate(body: str):
    """function documentation
    """
    response = requests.post(
        URL
        , json = body
        , headers = {"Content-Type": "application/json"}
        , timeout = None
    )

    return response.status_code


if __name__ == "__main__":
    from random import randint

    json_body = create_it_request(num=randint(2,6))
    run_power_automate(json_body)
