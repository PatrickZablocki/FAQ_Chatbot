from flask import Flask, request, jsonify
from flask_cors import CORS  # Importiere CORS

app = Flask(__name__)
CORS(app)  # Aktiviere CORS für alle Routen

# FAQ-Daten (Fragen und Antworten)
faq_data = {
    "Was ist eure Öffnungszeiten?": "Unsere Öffnungszeiten sind Montag bis Freitag von 9:00 bis 18:00 Uhr.",
    "Wie kann ich euch kontaktieren?": "Du kannst uns per E-Mail unter kontakt@example.com erreichen.",
    "Bietet ihr Rückgaben an?": "Ja, wir bieten Rückgaben innerhalb von 30 Tagen nach dem Kauf an.",
    "Wo befindet sich euer Geschäft?": "Unser Geschäft befindet sich in der Musterstraße 123, 12345 Musterstadt.",
    "Was sind die Versandkosten?": "Die Versandkosten betragen 5,99 € innerhalb Deutschlands.",
    "Gibt es einen Mindestbestellwert?": "Ja, der Mindestbestellwert beträgt 20 €."
}

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data['message'].lower()  # Konvertiere die Eingabe in Kleinbuchstaben
    
    # Überprüfe auf Schlüsselwörter
    if "öffnungszeiten" in user_message:
        bot_response = faq_data["Was ist eure Öffnungszeiten?"]
    elif "kontaktieren" in user_message:
        bot_response = faq_data["Wie kann ich euch kontaktieren?"]
    elif "rückgaben" in user_message:
        bot_response = faq_data["Bietet ihr Rückgaben an?"]
    elif "geschäft" in user_message:
        bot_response = faq_data["Wo befindet sich euer Geschäft?"]
    elif "versandkosten" in user_message:
        bot_response = faq_data["Was sind die Versandkosten?"]
    elif "mindestbestellwert" in user_message:
        bot_response = faq_data["Gibt es einen Mindestbestellwert?"]
    else:
        bot_response = "Entschuldigung, ich kann dazu keine Informationen finden."
    
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)
