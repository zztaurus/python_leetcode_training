from flask import Flask, render_template_string

app = Flask(__name__)

your_embed_token = "your_embed_token"

@app.route('/')
def embed_report():
    embed_url = "https://app.powerbi.com/reportEmbed?reportId=ea3ee973-f102-460a-b510-e7e50afd49d1&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly9XQUJJLUVBU1QtQVNJQS1BLVBSSU1BUlktcmVkaXJlY3QuYW5hbHlzaXMud2luZG93cy5uZXQiLCJlbWJlZEZlYXR1cmVzIjp7InVzYWdlTWV0cmljc1ZOZXh0Ijp0cnVlfX0%3d"
    embed_token =  your_embed_token
    report_id = "ea3ee973-f102-460a-b510-e7e50afd49d1"

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Power BI Report Embedding</title>
        <script src="https://cdn.jsdelivr.net/npm/powerbi-client@2.19.0/dist/powerbi.js"></script>
    </head>
    <body>
        <div id="reportContainer" style="height: 600px; width: 100%;"></div>

        <script>
            const embedUrl = "{embed_url}";
            const embedToken = "{embed_token}";
            const reportId = "{report_id}";

            const config = {{
                type: 'report',
                tokenType: window['powerbi-client'].models.TokenType.Embed,
                accessToken: embedToken,
                embedUrl: embedUrl,
                id: reportId,
                settings: {{
                    filterPaneEnabled: false,
                    navContentPaneEnabled: true
                }}
            }};

            const reportContainer = document.getElementById('reportContainer');
            const powerbi = window.powerbi;
            powerbi.embed(reportContainer, config);
        </script>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)