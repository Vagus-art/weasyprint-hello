from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

font_config = FontConfiguration()

content = [
  {
    "id": "0dade706-c2ea-49f2-bd1c-a0293bc08ca2",
    "name": "funciona",
    "items": [
      {
        "created": "12/22/2020, 05:08:28",
        "id": "4b8b072f-9b7e-4fc5-8696-db67bf72f4e5",
        "name": "jaja funcionax3",
        "categoryId": "0dade706-c2ea-49f2-bd1c-a0293bc08ca2"
      },
      {
        "created": "12/22/2020, 05:08:28",
        "id": "f7e4a226-325d-4b27-bce5-2720e60b67b3",
        "name": "jaja funcionax2",
        "categoryId": "0dade706-c2ea-49f2-bd1c-a0293bc08ca2"
      }
    ]
  }
]

parsed_content = ""

for category in content:
    category_string = f"<h1>{category['name']}</h1>"
    for item in category['items']:
        category_string+= f"<p>{item['name']}</p>"
    parsed_content+=category_string


# HTML('<h1>foo') would be filename
html = HTML(string=parsed_content)
css = CSS(string='@page { size: A3; margin: 1cm }')

html.write_pdf(
    'example.pdf', stylesheets=[css],
    font_config=font_config)
