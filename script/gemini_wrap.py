"""Wrapper class for Google's Gemini AI API integration.
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

import os
import google.generativeai as genai
from script.decorator import rate_limit


class Gemini:
    """
    A utility class for interacting with Google's Gemini AI models.

    This class provides a simplified interface for text generation using Gemini AI,
    with support for model selection and configurable request timeouts. It implements
    class methods to allow direct usage without instantiation.

    Attributes:
        __model (GenerativeModel): Internal reference to the Gemini model instance.

    Class Methods:
        set_model(model: str = "gemini-1.5-pro") -> None
            Configure which Gemini model to use for generation.
        
        generate(prompt: str, timeout: int = 100) -> str
            Generate text content using the configured model.

    Environment Variables:
        GEMINI_API_KEY: Required API key for authenticating with Gemini services.

    Example:
        >>> # Set custom model (optional)
        >>> Gemini.set_model("gemini-1.5-pro")
        >>> 
        >>> # Generate content
        >>> response = Gemini.generate("Explain quantum computing")
        >>> print(response)

    Notes:
        - API key must be set in environment variables before using the class
        - Default model is "gemini-1.5-pro" if not explicitly set
        - The model is automatically initialized on first generation if not set
    """

    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    __model = None

    @classmethod
    def get_model(cls) -> str:
        """Get the Gemini model to be used for generation.
        """
        return cls.__model

    @classmethod
    def set_model(cls, model: str = "gemini-1.5-pro") -> None:
        """Set the Gemini model to be used for generation.

        Args:
            model (str, optional): The model identifier to use. Defaults to "gemini-1.5-pro".
        """
        cls.__model = genai.GenerativeModel(model)

    @classmethod
    @rate_limit(calls=60, period=60)
    def generate(cls, message: str, timeout: int = 100) -> str:
        """Generate text content using the configured Gemini model.

        Args:
            prompt (str): The input text prompt for generation.
            timeout (int, optional): Request timeout in seconds. Defaults to 100.

        Returns:
            str: The generated text response.

        Raises:
            RuntimeError: If model is not set before calling generate.
        """
        if cls.__model is None:
            cls.set_model()

        # generate response json
        ans = cls.__model.generate_content(
            contents=message
            , request_options={"timeout": timeout}
        )
        return ans.text


if __name__ == "__main__":
    from random import randint

    num_questions = randint(2,6)
    print(num_questions)

    with open(file="./prompt.txt", mode="r", encoding="utf-8") as f:
        prompt = f.read()

    response = Gemini.generate(prompt.format(num_questions))

    with open("b.txt", "w", encoding="utf-8") as f:
        f.write(response)
