from flask import Flask, render_template_string

app = Flask(__name__)

your_embed_token = "H4sIAAAAAAAEAB3Tx46EVhQE0H-ZLZboJmPJC3JqoMlh98g5Z8v_7rH3pavSuaq_f77g7kaQ_fz54whCmMY60m-8fxgilwVnjrItuSFC0c-puuoDlR8aP8C2D9P3851mXaOWg4eHnYOcXb4gqLBTD3y5vXT9XT4cB39WhaVi_i0fpYJybQV2gaXzQaYLWQxLFOZcpMlQ38I3X3fhkRQXhE49DWRmFUB1mjiUr482urBCvL6OhXA_j4h6YpFqv5e_h4P10Harkrs_YhZL4qWPipkNlV00HA5QgsP0UKAUXim9TNIHeBsq_DQm3udDCRaJ6jxy1GcFK1vJ7vK1HJoT1_lWAJ17r6KHfre9g8HOM5edtZmgfZMXRBJyB-8uh5nqV-84Zse-vekWNi7NShTTL0LJue842yHq2sdaAUDc8qY8pGNUvzDKvVJzLxQTi2IAzhb2468SyTK1jJVg9hAZX1nUjNAguSGYjGuYZpoKBgGrbZUPO6XdgEgy5mCTnPtD3ABr6EX06EbgsX5azAE9QI8n3SLwkkXPVlamgRROxyfplHSPG8LCKIaAtwU5hsN-BZisklcE2w03oup3aTthkbGUHBR4NAW5oo76GD_MTql47VVAnTyauMdT4bwMJDWsGi4uMLVFp_TZx7o96tjbMOlCe_dFNKHBwSOK9T1sYS6ZOVNq65GZ6J2b6rg8Rb4ZElSz9-XVHM52PslY82wxKQTp28JKPMauTA_QBX6uCeWIrYRUS0fq-OM0HktOB40bn_fcwYXZdFElPbjlePSbTOjr2c5GfD8ozHp9ybXxgkZgNZwMdaa1gUCTD_3b-kx7B148xySJfKRXyhUpS5ElQgqfSDTjOn87b57_fhDaGCqoHKcpM5OPcVJJMmpSjNK-ZuudJ-jkw0psSeQ_f_xwyz1to5bfv3Na--i7x1BbY29v1sLLUiFevPzGedXsOpJwv6aBDWRyOMNqHsaJnBkk6tXHNRE8ZOYnlsi4PQ2lCInjGDVYUI1zUh_TuWJVwNaQxR0ELO-M_f3sKcMXkpJNcd2TuQ9K1XZOyGdVDNCxnBTTO1pepm01HEaInoU4Jlpo9PDQT2E1waQn32-W1432IllrVsopCKDF1--QW5On-a0q0wg0mZrmy3p2ZL9o5wt-X7OKFdfC9zWaaZvG4PkNXqddsbW_JqSNTxb-aaU-IMx3-xEPtGLubIauvsSrBvbmtOePzeKgWLXnCplKZXsxGQ6GLEWy697KmA6y_ZzXMX2d6knINZ3YAfPXX_8x31OVL4r_q2xUDRJHso7OmKfUb74xR04q_085dTmAbV_y39gF9IB6SSXc-dKGylxwV4jKvChq4zJsQll4HbccPigzxi7dsE6S11pRMfFguID_GiWhQHHez3MMMWW70vmg20UJuEfRsgU2E_FqZi6T3ev9ILgBo2b_ZeLl4y5rVPJA_tTCaMXD16Y5q8gzjn96HC2huShKlhJ8U5ITTdsoGRSvSw_GYZ_QUqyta_af-hudXd3frusBkWaCNE5CX9T7W_46dvnQlm90UxRTmNpWF9I6uIqPgiOJWz6YbnQcrvvkNhM8tereTZdDbMQBX_ETVoN1lxHN4dyjutY2mQRqbwH1ZPxNn3p-pw-q_5r84IhdOMgvuy1JDM87ABgmr1cYf-ri_GX-51_zdCiNQgYAAA==.eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly9XQUJJLUVBU1QtQVNJQS1BLVBSSU1BUlktcmVkaXJlY3QuYW5hbHlzaXMud2luZG93cy5uZXQiLCJleHAiOjE3NDE4NDEzNTYsInByaXZhdGVMaW5rc0VuYWJsZWQiOnRydWUsImFsbG93QWNjZXNzT3ZlclB1YmxpY0ludGVybmV0Ijp0cnVlfQ=="

@app.route('/')
def embed_report():
    embed_url = "https://app.powerbi.com/reportEmbed?reportId=06027c70-b428-4e59-ba94-e79865d020a1&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly9XQUJJLUVBU1QtQVNJQS1BLVBSSU1BUlktcmVkaXJlY3QuYW5hbHlzaXMud2luZG93cy5uZXQiLCJlbWJlZEZlYXR1cmVzIjp7InVzYWdlTWV0cmljc1ZOZXh0Ijp0cnVlfX0%3d"
    embed_token =  your_embed_token
    report_id = "06027c70-b428-4e59-ba94-e79865d020a1"

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
        <div id="reportContainer" style="height: 800px; width: 100%;"></div>
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
                    filterPaneEnabled: true,
                    navContentPaneEnabled: true,
                    filterPaneEnabled: true,
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