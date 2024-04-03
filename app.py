from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the model
model = joblib.load('logistic_regression_model.pkl')

# Render the form page
@app.route('/')
def form():
    return render_template('predict.html')

# Handle form submission and provide prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    features = []
    try:
        # Time
        features.append(float(request.form['Time']))

        # Cranial-Capacity
        features.append(float(request.form['Cranial-Capacity']))

        # Height
        features.append(float(request.form['Height']))


        # Location
        location = request.form['Location']
        features.extend([1 if location == 'Asia' else 0,
    
                        1 if location == 'Europe' else 0])

        # Zone
        zone = request.form['Zone']
        features.extend([1 if zone == 'oriental' else 0,
                        1 if zone == 'south' else 0,
                        1 if zone == 'west' else 0
                        ])

        # Current Country
        current_country = request.form['current-country']
        features.extend([1 if current_country == country else 0 for country in ['Georgia', 'Germany', 'Indonesia', 'Kenya', 'Republic of Chad', 'South Africa', 'Spain']])

        # Habitat
        habitat = request.form['Habitat']
        features.extend([1 if habitat == 'forest' else 0,
                        1 if habitat == 'mixed' else 0,
                        1 if habitat == 'forest-gallery' else 0])

        
        # Incisor Size
        incisor_size = request.form['Incisor_Size']
        features.extend([1 if incisor_size == size else 0 for size in ['small', 'big', 'megadony', 'very small', 'medium large']])

        # Jaw Shape
        jaw_shape = request.form['Jaw_Shape']
        features.extend([1 if jaw_shape == shape else 0 for shape in ['U shape', 'conical', 'V shape', 'modern']])

        # Torus Supraorbital
        torus_supraorbital = request.form['Torus_Supraorbital']
        features.extend([1 if torus_supraorbital == torus else 0 for torus in ['very protruding', 'little protruding', 'less protruding', 'ultra protruding', 'flat']])

        # Prognathism
        prognathism = request.form['Prognathism']
        features.extend([1 if prognathism == p else 0 for p in ['absent', 'medium', 'medium-high', 'high', 'very high', 'reduced']])

        # Foramen MAignum Position
        foramen_maignum = request.form['Foramen_MAignum_Position']
        features.extend([1 if foramen_maignum == pos else 0 for pos in ['posterior', 'semi-anterior', 'anterior', 'modern']])

        # Canine Size
        canine_size = request.form['Canine_Size']
        features.extend([1 if canine_size == size else 0 for size in ['small', 'big']])

        # Canines Shape
        canines_shape = request.form['Canines_Shape']
        features.extend([1 if canines_shape == shape else 0 for shape in ['conicalls', 'incisiform']])

        # Tooth Enamel
        tooth_enamel = request.form['Tooth_Enamel']
        features.extend([1 if tooth_enamel == enamel else 0 for enamel in ['thin', 'thick', 'very thin', 'very thick', 'medium thin', 'medium thick', 'thick medium']])

        # Tecno
        tecno = request.form['Tecno']
        features.extend([1 if tecno == t else 0 for t in ['yes', 'no', 'likely']])

        # Tecno Type
        tecno_type = request.form['Tecno_type']
        features.extend([1 if tecno_type == t else 0 for t in ['no', 'mode 1', 'mode 2', 'mode 3', 'mode 4', 'primitive']])

        # Biped
        biped = request.form['biped']
        features.extend([1 if biped == b else 0 for b in ['yes', 'low probability', 'high probability', 'modern']])

        # Arms
        arms = request.form['Arms']
        features.extend([1 if arms == a else 0 for a in ['climbing', 'walk', 'manipulate']])

        # Foots
        foots = request.form['Foots']
        features.extend([1 if foots == f else 0 for f in ['climbing', 'walk']])

        # Diet
        diet = request.form['Diet']
        features.extend([1 if diet == d else 0 for d in ['dry fruits', 'soft fruits', 'hard fruits', 'omnivore', 'carnivore']])

        # Sexual Dimorphism
        sexual_dimorphism = request.form['Sexual_Dimorphism']
        features.extend([1 if sexual_dimorphism == s else 0 for s in ['High', 'Medium', 'Medium_High', 'Reduced']])

        # Hip
        hip = request.form['Hip']
        features.extend([1 if hip == h else 0 for h in ['slim', 'wide', 'modern', 'very modern']])

        # Verical Front
        verical_front = request.form['Verical_Front']
        features.extend([1 if verical_front == v else 0 for v in ['yes', 'no', 'modern']])

        # Anatomy
        anatomy = request.form['Anatomy']
        features.extend([1 if anatomy == a else 0 for a in ['old', 'mixed', 'modern', 'very modern']])

        # Migrated
        migrated = request.form['Migrated']
        features.extend([1 if migrated == m else 0 for m in ['yes', 'no']])

        # Skeleton
        skeleton = request.form['Skeleton']
        features.extend([1 if skeleton == s else 0 for s in ['light', 'refined', 'robust']])
    except:
        pass
    # Make prediction
    print([features])
    prediction = model.predict([features])
    print(prediction)

    # Render the result page with prediction
    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run
