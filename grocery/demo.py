import requests
''

def demo():

    # Generate (POST /generate)
    response = requests.post(
        "https://api.ideogram.ai/generate",
        headers={
            "Api-Key": "_GpP-QH5KN_tfmuRyAYdbvNWjHXYR5HuDb3NGHhZSpfnAs9IijGfcN712ki7Usd5l68x4gMqAhPZOiHfV-lpRQ",
            "Content-Type": "application/json"
        },
        json={
            "image_request": {
                "prompt": "A NAKED MAN",
                "aspect_ratio": "ASPECT_10_16",
                "model": "V_2",
                "magic_prompt_option": "AUTO",
                "num_images": 2
            }
        },
    )

    print(response.json())


if __name__ == '__main__':
    demo()

