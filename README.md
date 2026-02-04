# Get Better - Non-Profit Substance Awareness & Lifestyle Improvement Platform

A comprehensive, personalized platform helping people quit harmful substances, improve their fitness, and enhance their appearance. Built with Flask and designed for real people who want real results—not motivational speeches.

## Features

### 🎯 Core Features
- **Multi-Select Goal System**: Choose what you need help with (substances, lifestyle, appearance) or combine multiple goals
- **Personalized Plans**: Answer a few questions, get a customized plan tailored to your situation
- **Dark Theme**: Eye-friendly dark interface for extended use
- **Mobile Optimized**: Fully responsive design with hamburger menu for mobile
- **Dropdown Plan Views**: Plans use collapsible dropdowns to save screen space
- **User Accounts**: Create accounts, save your plans, return to your progress

### 💊 Substance Support
- Vaping/E-cigarettes
- Nicotine
- Alcohol
- Tobacco/Smoking
- Cannabis/Weed
- Other Drugs

Plans include:
- Health risks explained (not just "it's bad")
- Frequency-based quit strategies
- Week-by-week action steps
- Science-backed benefits of quitting

### 💪 Lifestyle & Fitness
- Personalized plans based on age, height, weight, activity level
- Choose your goal: build muscle or lose weight
- Nutrition and exercise guidance
- 8-week transformation plan

### ✨ Appearance & Looks
- Skincare science (what works vs. what's cope)
- Fitness impact on physique
- Fashion and grooming fundamentals
- Why appearance matters + what actually works

## Tech Stack

- **Backend**: Python Flask
- **Database**: SQLAlchemy with SQLite (PostgreSQL for production)
- **Frontend**: HTML5, CSS3 (dark theme)
- **JavaScript**: Vanilla JS for interactive features
- **Deployment**: Render (or any Python hosting)

## Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. Clone the repository
```bash
git clone https://github.com/yourusername/getbetter.git
cd getbetter
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the application
```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

## Project Structure

```
getbetter/
├── app.py                 # Main Flask application
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies
├── Procfile             # Heroku/Render deployment
├── static/
│   ├── css/
│   │   └── style.css    # Dark theme CSS + responsive
│   └── js/
│       └── main.js      # Interactive features
└── templates/
    ├── base.html        # Base template with navbar
    ├── home.html        # Landing page
    ├── signup.html      # Sign up page
    ├── login.html       # Login page
    ├── onboarding.html  # Goal selection overlay
    ├── dashboard.html   # User dashboard with plans
    ├── plan_detail.html # Detailed plan view
    ├── about.html       # About page
    └── contact.html     # Contact form
```

## Usage

### For Users
1. **Sign Up**: Create a free account
2. **Answer Questions**: Select your goals and provide details
3. **Get Plan**: Receive personalized guidance
4. **Follow Plan**: Track progress and make changes

### For Developers

#### Adding a New Substance
Edit `app.py` and add to `SUBSTANCE_INFO`:
```python
'new_substance': {
    'name': 'Display Name',
    'health_risks': ['Risk 1', 'Risk 2', ...],
    'quit_benefits': ['Benefit 1', 'Benefit 2', ...]
}
```

#### Customizing Styling
Edit `static/css/style.css`. Key variables:
```css
:root {
    --bg-dark: #0a0e27;
    --accent: #00d4ff;
    --text-primary: #e0e0e0;
    /* ... */
}
```

## Deployment

### Deploy to Render

1. Push to GitHub
```bash
git push origin main
```

2. Connect to Render
   - Sign up at [render.com](https://render.com)
   - Create new Web Service
   - Connect GitHub repository
   - Set environment variables (if needed)
   - Deploy

Render will automatically read `Procfile` and deploy the app.

### Environment Variables
```
SECRET_KEY=your-secret-key-here
DATABASE_URL=your-database-url  # Optional for PostgreSQL
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home page |
| GET/POST | `/signup` | Sign up page |
| GET/POST | `/login` | Login page |
| GET | `/onboarding` | Goal selection |
| POST | `/api/save-plan` | Save user plan |
| GET | `/dashboard` | User dashboard |
| GET | `/plan/<category>` | Detailed plan view |
| GET | `/about` | About page |
| GET/POST | `/contact` | Contact form |
| GET | `/logout` | Logout |

## Features Explained

### Dark Theme
- Easy on the eyes for extended use
- Modern aesthetic
- CSS variables for easy customization
- Proper contrast ratios for accessibility

### Mobile Responsive
- Hamburger menu (3-line icon) on mobile
- Collapsible dropdown menus
- Touch-friendly buttons
- Responsive grid layouts

### Onboarding Overlay
- Appears when new users log in
- Multi-select goal system
- Conditional forms based on selections
- Frequency inputs for substances
- Personal stats for lifestyle

### Personalized Plans
- Different logic for each category
- Frequency-based customization
- Progress tracking capability
- Actionable weekly steps

## Non-Corny Approach

This platform:
- ❌ Doesn't use clichés ("You've got this!" x100)
- ✅ Explains the science behind why habits are harmful
- ✅ Provides actionable strategies, not just motivation
- ✅ Treats users like adults
- ✅ Acknowledges that change is hard but doable
- ✅ Focuses on specific health impacts

## Contributing

We welcome contributions! Areas for improvement:
- Additional substance support
- Community features (forums, peer support)
- Mobile app
- Advanced analytics
- Email reminders

## Support

- **Crisis Support**: Call 1-800-662-4357 (SAMHSA, 24/7, free)
- **Questions**: hello@getbetter.com
- **Issues**: GitHub issues page
- **Contact**: Use the contact form on the site

## License

This project is open source and available under the MIT License.

## Disclaimer

This platform is not a substitute for professional medical or psychological treatment. If you're struggling with substance abuse or mental health issues, please consult healthcare professionals and utilize the crisis resources provided.

---

**Get Better**: Because you deserve to be your best self.
