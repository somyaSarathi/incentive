# IT Request Generator

Copyright (C) 2024 SOMYA SARATHI SAMAL

This program generates and processes simulated IT service desk requests using Google's Gemini AI. It creates realistic support tickets and submits them through Power Automate for processing.

## Overview

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

## Features

- AI-powered ticket description generation using Gemini
- Configurable number of tickets (2-6 per batch)
- Random user assignment from configured user pool
- Automated submission to Power Automate
- Rate limiting protection for API calls
- Environment-based configuration

## Dependencies

This program requires:
- Python (>= 3.13)
- pandas
- numpy 
- requests
- google-generativeai

## Building from Source

1. Clone the repository
2. Install dependencies:
```bash
pip install pandas numpy requests google-generativeai
```

## Configuration

Before running, set environment variables:
```bash
export GEMINI_API_KEY="your-api-key"
export USERS="user1,user2,user3"
export URL="your-power-automate-endpoint"
```

Create `prompt.txt` in the project root with your Gemini prompt template. Use `{}` as placeholder for number of requests.

## Files

- `main.py`: Entry point
- `config.py`: Configuration management
- `decorator.py`: Custom decorators
- `gemini_wrap.py`: Gemini AI wrapper
- `it_requests.py`: Core request functionality

## Usage

### Basic Operation

Run directly:
```bash
python main.py
```

Import in code:
```python
from it_requests import create_it_request, run_power_automate
json_data = create_it_request(num=4)
status_code = run_power_automate(json_data)
```

### Environment Variables

Required configuration:
- `GEMINI_API_KEY`: Google Gemini API key
- `USERS`: Comma-separated user list
- `URL`: Power Automate endpoint

### Output Format

Generates JSON tickets:
```json
[
  {
    "title": "AI-generated title"
    "description": "AI-generated description",
    "delay": 45,
    "request_reported_by": "user1"
  }
]
```

<!-- ## Reporting Bugs

Report bugs to: [your-email/issue-tracker] -->

<!-- ## Contributing

Send patches and pull requests via: [your-repository-url] -->

## Authors

SOMYA SARATHI SAMAL

## Copyright

Copyright (C) 2024 SOMYA SARATHI SAMAL

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.