"""Entry point for the IT request generation and automation system.
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

from random import randint
from it_requests import create_it_request, run_power_automate

def main():
    """Generate and submit IT service desk requests.
    
    Creates a random number (2-6) of simulated IT request tickets and
    submits them through Power Automate for processing. The requests
    include randomly assigned users and estimated delay times.
    
    Returns:
        None
    """
    json_body = create_it_request(num=randint(2,6))
    run_power_automate(json_body)

if __name__ == "__main__":
    main()
