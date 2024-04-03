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
                        1 if habitat == 'forest-gallery' else 0,
                        1 if habitat=='forest-savanna' else 0,
                        1 if habitat=='jungle' else 0,
                         1 if habitat == 'mixed' else 0])

        
        # Incisor Size
        incisor_size = request.form['Incisor_Size']
        features.extend([1 if incisor_size == size else 0 for size in ['medium large','megadony','small', 'very small' ]])

        # Jaw Shape
        jaw_shape = request.form['Jaw_Shape']
        features.extend([1 if jaw_shape == shape else 0 for shape in ['V shape','conical', 'modern']])

        # Torus Supraorbital
        torus_supraorbital = request.form['Torus_Supraorbital']
        features.extend([1 if torus_supraorbital == torus else 0 for torus in ['less protruding','little protruding','ultra protruding', 'very protruding']])

        # Prognathism
        prognathism = request.form['Prognathism']
        features.extend([1 if prognathism == p else 0 for p in [ 'high','medium', 'medium-high', 'reduced', 'very high' ]])

        # Foramen MAignum Position
        foramen_maignum = request.form['Foramen_MAignum_Position']
        features.extend([1 if foramen_maignum == pos else 0 for pos in ['modern','posterior', 'semi-anterior' ]])

        # Canine Size
        canine_size = request.form['Canine_Size']
        features.extend([1 if canine_size == size else 0 for size in ['small']])

        # Canines Shape
        canines_shape = request.form['Canines_Shape']
        features.extend([1 if canines_shape == shape else 0 for shape in [ 'incisiform']])

        # Tooth Enamel
        tooth_enamel = request.form['Tooth_Enamel']
        features.extend([1 if tooth_enamel == enamel else 0 for enamel in [ 'medium thin','thick','thick medium','thin','very thick',  'very thin' ]])

        # Tecno
        tecno = request.form['Tecno']
        features.extend([1 if tecno == t else 0 for t in ['no', 'yes']])

        # Tecno Type
        tecno_type = request.form['Tecno_type']
        features.extend([1 if tecno_type == t else 0 for t in [ 'mode 2', 'mode 3', 'mode 4', 'no', 'primitive']])

        # Biped
        biped = request.form['biped']
        features.extend([1 if biped == b else 0 for b in [ 'low probability', 'modern','yes']])

        # Arms
        arms = request.form['Arms']
        features.extend([1 if arms == a else 0 for a in [ 'manipulate','manipulate with precision', 'walk']])

        # Foots
        foots = request.form['Foots']
        features.extend([1 if foots == f else 0 for f in ['climbing', 'walk']])

        # Diet
        diet = request.form['Diet']
        features.extend([1 if diet == d else 0 for d in ['dry fruits',  'hard fruits', 'omnivore','soft fruits' ]])

        # Sexual Dimorphism
        sexual_dimorphism = request.form['Sexual_Dimorphism']
        features.extend([1 if sexual_dimorphism == s else 0 for s in [ 'medium-High', 'reduced']])

        # Hip
        hip = request.form['Hip']
        features.extend([1 if hip == h else 0 for h in ['slim', 'very modern', 'wide']])

        # Verical Front
        verical_front = request.form['Verical_Front']
        features.extend([1 if verical_front == v else 0 for v in ['no','yes']])

        # Anatomy
        anatomy = request.form['Anatomy']
        features.extend([1 if anatomy == a else 0 for a in [ 'modern','old', 'very modern']])

        # Migrated
        migrated = request.form['Migrated']
        features.extend([1 if migrated == m else 0 for m in ['yes']])

        # Skeleton
        skeleton = request.form['Skeleton']
        features.extend([1 if skeleton == s else 0 for s in ['refined', 'robust']])
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
