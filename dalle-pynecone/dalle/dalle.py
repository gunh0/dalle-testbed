"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config
from dotenv import dotenv_values

import openai
import pynecone as pc

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"

config = dotenv_values("../.env")
openai.api_key = config["OPENAI_API_KEY"]


class State(pc.State):
    """The app state."""

    prompt = ""
    image_url0 = ""
    image_url1 = ""
    image_url2 = ""
    image_url3 = ""
    image_url4 = ""
    image_url5 = ""
    image_url6 = ""
    image_url7 = ""
    image_processing = False
    image_made = False

    def on_process(self):
        """Set the image processing flag to true and indicate that the image has not been made yet."""
        self.image_made = False
        self.image_processing = True

    def get_image(self):
        """Get the image from the prompt."""
        try:
            response = openai.Image.create(prompt=self.prompt, n=8, size="256x256")
            self.image_url0 = response["data"][0]["url"]
            self.image_url1 = response["data"][1]["url"]
            self.image_url2 = response["data"][2]["url"]
            self.image_url3 = response["data"][3]["url"]
            self.image_url4 = response["data"][4]["url"]
            self.image_url5 = response["data"][5]["url"]
            self.image_url6 = response["data"][6]["url"]
            self.image_url7 = response["data"][7]["url"]

            # Set the image processing flag to false and indicate that the image has been made.
            self.image_processing = False
            self.image_made = True
        except:
            self.image_processing = False
            return pc.window_alert("Error with OpenAI Execution.")


def index():
    return pc.center(
        pc.vstack(
            pc.heading("DALL-E", font_size="1.5em"),
            pc.input(placeholder="Enter a prompt..", on_blur=State.set_prompt),
            pc.button(
                "Generate Image",
                width="100%",
                on_click=[State.on_process, State.get_image],
            ),
            pc.divider(),
            pc.cond(
                State.image_processing, pc.circular_progress(is_indeterminate=True)
            ),
            pc.cond(
                State.image_made,
                pc.vstack(
                    pc.hstack(
                        pc.image(
                            src=State.image_url0,
                            height="10em",
                            width="10em",
                        ),
                        pc.image(
                            src=State.image_url1,
                            height="10em",
                            width="10em",
                        ),
                        pc.image(
                            src=State.image_url2,
                            height="10em",
                            width="10em",
                        ),
                        pc.image(
                            src=State.image_url3,
                            height="10em",
                            width="10em",
                        ),
                    ),
                    pc.hstack(
                        pc.image(
                            src=State.image_url4,
                            height="10em",
                            width="10em",
                        ),
                        pc.image(
                            src=State.image_url5,
                            height="10em",
                            width="10em",
                        ),
                        pc.image(
                            src=State.image_url6,
                            height="10em",
                            width="10em",
                        ),
                        pc.image(
                            src=State.image_url7,
                            height="10em",
                            width="10em",
                        ),
                    ),
                ),
            ),
            bg="white",
            padding="2em",
            shadow="lg",
            border_radius="lg",
        ),
        width="100%",
        height="100vh",
        background="radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(0,0%,100%,0) 19%),radial-gradient(circle at 82% 25%,rgba(33,150,243,.18),hsla(0,0%,100%,0) 35%),radial-gradient(circle at 25% 61%,rgba(250, 128, 114, .28),hsla(0,0%,100%,0) 55%)",
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index, title="Pynecone:DALL-E")
app.compile()
