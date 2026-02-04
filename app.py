from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///getbetter.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    plans = db.relationship('UserPlan', backref='user', lazy=True, cascade='all, delete-orphan')
    
class UserPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # substance, lifestyle, looks
    selected_items = db.Column(db.String(500), nullable=False)  # JSON list of selections
    plan_data = db.Column(db.Text)  # Personalized plan data
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Sample data for plans
SUBSTANCE_INFO = {
    'vaping': {
        'name': 'Nicotine Vaping',
        'health_risks': [
            'Nicotine addiction affects dopamine levels, making it harder to experience pleasure naturally',
            'Vaping damages lung tissue and reduces oxygen capacity',
            'Increases heart rate and blood pressure, straining your cardiovascular system',
            'Contains toxic chemicals that accumulate in your lungs over time',
            'Impacts memory and cognitive function, especially in developing brains'
        ],
        'quit_benefits': ['Better breathing within weeks', 'Improved focus and memory', 'More money in your pocket', 'Better athletic performance', 'Clearer skin']
    },
    'nicotine': {
        'name': 'Nicotine',
        'health_risks': [
            'Creates powerful physical dependence within days',
            'Increases anxiety and panic attacks when withdrawing',
            'Damages blood vessels and increases stroke risk',
            'Impairs sleep quality and creates dependency for "energy"',
            'Stains teeth and causes gum disease'
        ],
        'quit_benefits': ['Lower stress naturally', 'Better sleep quality', 'Stronger immune system', 'Saved money', 'Better oral health']
    },
    'alcohol': {
        'name': 'Alcohol',
        'health_risks': [
            'Damages liver cells leading to cirrhosis and liver failure',
            'Increases risk of cancer (mouth, throat, liver, colon)',
            'Impairs brain function, reduces cognitive abilities permanently',
            'Weakens immune system, making you prone to infections',
            'Leads to weight gain and metabolic issues'
        ],
        'quit_benefits': ['Better liver function', 'Weight loss', 'Sharper mental clarity', 'Better sleep', 'Improved relationships']
    },
    'tobacco': {
        'name': 'Tobacco/Smoking',
        'health_risks': [
            'Destroys lung tissue and causes COPD',
            'Increases cancer risk (lung, throat, mouth, bladder)',
            'Reduces blood oxygen, affecting every organ',
            'Ages skin prematurely, causes wrinkles and yellowing',
            'Increases heart disease and stroke risk'
        ],
        'quit_benefits': ['Lung function improves in months', 'Better skin appearance', 'More energy', 'Saved thousands per year', 'Improved taste and smell']
    },
    'weed': {
        'name': 'Cannabis/Weed',
        'health_risks': [
            'Impairs memory formation and learning ability',
            'Increases anxiety and paranoia, especially with heavy use',
            'Regular use reduces motivation and goal pursuit',
            'Affects mental health, can trigger or worsen depression',
            'Impairs driving ability and coordination'
        ],
        'quit_benefits': ['Sharper memory and focus', 'Better motivation', 'Improved mental health', 'Better sleep quality', 'Clearer thinking']
    },
    'drugs': {
        'name': 'Hard Drugs',
        'health_risks': [
            'Causes severe physical and psychological dependence',
            'Damages brain chemistry, affecting decision-making permanently',
            'High overdose risk, can be fatal',
            'Damages cardiovascular system, can cause heart attack',
            'Destroys social relationships and opportunities'
        ],
        'quit_benefits': ['Reclaim your life', 'Repair relationships', 'Better health', 'Financial stability', 'Real mental clarity']
    }
}

# Utility functions
def generate_substance_plan(substance, frequency):
    info = SUBSTANCE_INFO.get(substance, {})
    try:
        weeks = int(float(frequency)) if frequency else 3
    except (ValueError, TypeError):
        weeks = 3
    
    plan_steps = {
        1: 'Week 1: Understand your triggers and plan your quit date. Track when you typically use and what emotions trigger it.',
        2: 'Week 2: Find alternatives - exercise, breathing exercises, or hobbies. Replace the habit with something positive.',
        3: 'Week 3: Manage withdrawal symptoms. Stay hydrated, exercise, and reach out to support systems.',
        4: 'Week 4: Overcome cravings with cold water, exercise, or distraction. Each craving passes in 5-10 minutes.',
        5: 'Week 5+: Build a new routine. Track your progress and celebrate milestones. Join a support community.',
    }
    
    return {
        'name': info.get('name', substance),
        'frequency': f"{frequency}x per week",
        'plan_steps': [plan_steps.get(i, f'Week {i}: Continue your progress and consolidate your habits') for i in range(1, weeks + 2)],
        'health_risks': info.get('health_risks', []),
        'quit_benefits': info.get('quit_benefits', [])
    }

def generate_lifestyle_plan(age, height, weight, activity_level, goal):
    # Convert string inputs to proper numeric types
    try:
        age = int(age)
        height = float(height)
        weight = float(weight)
    except (ValueError, TypeError):
        age, height, weight = 25, 180, 75
    
    bmi = weight / ((height/100) ** 2) if height else 0
    
    plan = {
        'stats': {'age': age, 'height': height, 'weight': weight, 'bmi': round(bmi, 1)},
        'goal': goal,
        'assessment': '',
        'plan_steps': [],
        'tips': []
    }
    
    if goal == 'bulk':
        plan['assessment'] = f"Goal: Build muscle and strength. Your BMI is {round(bmi, 1)} - focusing on gaining muscle mass."
        plan['plan_steps'] = [
            'Week 1-2: Establish gym routine - 4-5 days per week, focus on compound lifts (bench, squat, deadlift)',
            'Week 3-4: Increase caloric intake by 300-500 calories, prioritize protein (0.8-1g per lb of body weight)',
            'Week 5-8: Progressive overload - increase weights each week by 2-5%',
            'Week 9+: Monitor progress, adjust diet and training based on results'
        ]
        plan['tips'] = [
            'Eat in a caloric surplus (200-500 above maintenance)',
            'Sleep 7-9 hours nightly for muscle recovery',
            'Drink 3-4 liters of water daily',
            'Track your lifts and aim for progressive overload',
            'Be patient - muscle building takes 8-12 weeks to see results'
        ]
    else:  # weight loss
        plan['assessment'] = f"Goal: Lose weight and improve health. Your BMI is {round(bmi, 1)} - focusing on sustainable weight loss."
        plan['plan_steps'] = [
            'Week 1-2: Create slight caloric deficit (300-500 below maintenance), track food intake',
            'Week 3-4: Establish exercise routine - 150 minutes cardio + 2 days strength training',
            'Week 5-8: Increase NEAT (daily movement), prioritize whole foods',
            'Week 9+: Monitor progress, expect 1-2 lbs weight loss per week'
        ]
        plan['tips'] = [
            'Create a 300-500 calorie deficit through diet + exercise',
            'Prioritize protein to preserve muscle (0.7-0.8g per lb)',
            'Move more throughout the day, aim for 8,000+ steps',
            'Sleep 7-9 hours - poor sleep sabotages weight loss',
            'Be consistent, expect results in 4-6 weeks'
        ]
    
    return plan

def generate_looks_plan():
    return {
        'sections': {
            'skincare': {
                'title': 'Skincare Fundamentals',
                'tips': [
                    'Cleanse twice daily with a gentle cleanser',
                    'Use a basic moisturizer suited to your skin type',
                    'Apply SPF 30+ daily - sun damage is cumulative',
                    'Avoid touching your face throughout the day',
                    'Stay hydrated and get quality sleep for skin health'
                ],
                'debunked': [
                    'Facial exercises don\'t work - focus on sun protection and hydration instead',
                    'Expensive products aren\'t necessary - consistency matters more than price',
                    'Over-washing damages your skin barrier - twice daily is optimal'
                ],
                'backed': [
                    'Retinol/Retinoids reduce wrinkles and improve texture (evidence-backed)',
                    'Sunscreen prevents aging and skin cancer (scientifically proven)',
                    'Moisturizing maintains skin barrier health (dermatologist recommended)'
                ]
            },
            'fitness': {
                'title': 'Fitness & Body Composition',
                'tips': [
                    'Strength training 3-4x per week transforms your physique',
                    'Progressive overload (gradually increasing weight) drives muscle growth',
                    'Cardio improves cardiovascular health without excessive time needed',
                    'Consistency beats intensity - 3 months of regular training beats sporadic effort',
                    'Compound exercises (squats, bench press, deadlifts) maximize results'
                ],
                'debunked': [
                    'Spot reduction doesn\'t exist - you can\'t target fat loss from one area',
                    'Muscle soreness isn\'t required for progress - training smart matters',
                    'You don\'t need supplements to see results - diet and training are primary'
                ],
                'backed': [
                    'Strength training increases metabolism and improves health markers',
                    'Regular exercise improves mental health and confidence',
                    'Physical fitness enhances attractiveness through posture and bearing'
                ]
            },
            'fashion': {
                'title': 'Fashion & Style',
                'tips': [
                    'Well-fitted clothes matter more than expensive brands',
                    'Maintain good posture - it instantly improves appearance',
                    'Keep clothes clean and in good condition',
                    'Find a style that matches your body type and personality',
                    'Invest in basics: plain t-shirts, well-fitting jeans, neutral colors'
                ],
                'debunked': [
                    'Following all trends makes you look worse - wear what suits you',
                    'Expensive designer clothes aren\'t necessary for looking good',
                    'Constantly changing your look doesn\'t improve attractiveness'
                ],
                'backed': [
                    'Good grooming and hygiene are the foundation of appearance',
                    'Confidence from proper fitting clothes enhances attractiveness',
                    'Clean, maintained appearance signals self-respect and maturity'
                ]
            },
            'overall': {
                'title': 'Why Appearance Matters (Reality Check)',
                'points': [
                    'First impressions are formed in milliseconds - appearance is your first communication',
                    'Society has beauty standards whether we like it or not - working with them gives you advantages',
                    'Taking care of your appearance correlates with discipline in other life areas',
                    'Improved appearance boosts confidence, which improves all social interactions',
                    'But remember: attraction beyond initial appearance is built on character and competence'
                ]
            }
        }
    }

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        
        if not email or not password:
            return jsonify({'error': 'Email and password required'}), 400
        
        if User.query.filter_by(email=email).first():
            return jsonify({'error': 'Email already exists'}), 400
        
        user = User(email=email, password=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        
        session['user_id'] = user.id
        return jsonify({'success': True, 'redirect': url_for('onboarding')})
    
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return jsonify({'success': True, 'redirect': url_for('dashboard')})
        
        return jsonify({'error': 'Invalid email or password'}), 401
    
    return render_template('login.html')

@app.route('/onboarding')
def onboarding():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('onboarding.html')

@app.route('/api/save-plan', methods=['POST'])
def save_plan():
    if 'user_id' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    data = request.get_json()
    selections = data.get('selections', [])
    
    # Clear existing plans for this user
    UserPlan.query.filter_by(user_id=session['user_id']).delete()
    
    plans_data = {}
    
    for selection in selections:
        if selection in SUBSTANCE_INFO:
            frequency = data.get(f'{selection}_frequency', 3)
            plan = generate_substance_plan(selection, frequency)
            plans_data[selection] = plan
        elif selection == 'lifestyle':
            plan = generate_lifestyle_plan(
                data.get('age', 25),
                data.get('height', 180),
                data.get('weight', 75),
                data.get('activity_level', 'moderate'),
                data.get('fitness_goal', 'weight_loss')
            )
            plans_data['lifestyle'] = plan
        elif selection == 'looks':
            plans_data['looks'] = generate_looks_plan()
    
    user_plan = UserPlan(
        user_id=session['user_id'],
        category='combined',
        selected_items=','.join(selections),
        plan_data=str(plans_data)
    )
    db.session.add(user_plan)
    db.session.commit()
    
    return jsonify({'success': True, 'redirect': url_for('dashboard')})

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    plan = UserPlan.query.filter_by(user_id=session['user_id']).first()
    
    return render_template('dashboard.html', user=user, plan=plan)

@app.route('/plan/<category>')
def plan_detail(category):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user_plan = UserPlan.query.filter_by(user_id=session['user_id']).first()
    
    if not user_plan:
        return redirect(url_for('dashboard'))
    
    import ast
    try:
        plans_data = ast.literal_eval(user_plan.plan_data)
    except:
        plans_data = {}
    
    plan_content = plans_data.get(category, {})
    
    return render_template('plan_detail.html', category=category, plan=plan_content)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.get_json()
        # In production, send email here
        return jsonify({'success': True, 'message': 'Message sent successfully'})
    
    return render_template('contact.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
