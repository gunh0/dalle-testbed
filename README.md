# DALL-E Testbed

> This app uses the OpenAI DALL-E API to generate images from prompts. The code uses the Pynecone library, which is built on top of Flask and React.

![dall-e-demo](README.assets/dall-e-demo.gif)<br/>

### Setup

```
python --version
Python 3.10.9
```

Before running the code, make sure to install the required libraries. You can do this by running:

```
pip install -r requirements.txt
```

Next, create a `dalle2-testbed/.env` file with your OpenAI API key:

```
OPENAI_API_KEY=""
```

<br/>

### References

-   Pynecone documentation : https://pynecone.io/docs/getting-started/introduction
-   OpenAI DALL-E API documentation : https://platform.openai.com/docs/api-reference/images/dall-e/
