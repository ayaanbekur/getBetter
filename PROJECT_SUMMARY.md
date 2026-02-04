# Get Better - Project Summary

## What Was Built

A complete, production-ready web application called **"Get Better"** - a non-profit platform helping people quit harmful substances, improve their lifestyle, and enhance their appearance.

## Key Features Delivered

### 🎯 Core Functionality
✅ **Multi-Goal Selection System** - Users can simultaneously work on multiple areas:
   - Quit substances (vaping, nicotine, alcohol, tobacco, weed, drugs)
   - Improve lifestyle (fitness, weight loss, muscle building)
   - Enhance appearance (skincare, fashion, grooming)

✅ **Personalized Plan Generation** - Each plan is customized based on:
   - Frequency of substance use (times per week)
   - Personal stats (age, height, weight, activity level)
   - User goals (bulk up, lose weight, quit habits)
   - Real science-backed recommendations

✅ **Dark Theme** - Modern, eye-friendly dark interface:
   - #0a0e27 background
   - Cyan (#00d4ff) accent colors
   - Proper contrast ratios for accessibility
   - Custom scrollbar styling

✅ **Mobile Responsive** - Fully optimized for all devices:
   - Hamburger menu (3-line icon) on mobile
   - Collapsible dropdowns save space
   - Touch-friendly interface
   - Responsive grids and layouts

✅ **Dropdown Plan Menus** - Plans don't clutter the dashboard:
   - Plans collapsed by default
   - Click to expand/see full details
   - Smooth animations
   - Works on all screen sizes

✅ **User Authentication** - Secure account system:
   - Sign up / login pages
   - Encrypted password storage
   - Session management
   - Persistent user data

✅ **Onboarding Overlay** - First-time user experience:
   - Goal selection overlay on login
   - Multi-select buttons
   - Conditional forms based on selections
   - Smooth animations

✅ **In-Depth, Non-Corny Content**:
   - Explains WHY substances harm you (not just "it's bad")
   - Specific health impacts and timeline of recovery
   - What methods work vs. what's cope
   - Practical, actionable weekly steps
   - Adult tone, no motivational clichés

✅ **Comprehensive Plan Content**:
   - Health risks (specific impacts on body/mind)
   - Benefits of quitting (what you'll gain)
   - Week-by-week action steps
   - Science-backed methods and strategies

## Technology Stack

- **Backend**: Python Flask (lightweight, perfect for this)
- **Database**: SQLAlchemy with SQLite (dev) / PostgreSQL (production)
- **Frontend**: HTML5 + CSS3 (dark theme) + Vanilla JavaScript
- **Security**: Password hashing with Werkzeug
- **Deployment**: Render-ready (Procfile included)

## File Structure

```
NonProfit/
├── app.py                    (Main Flask app - 400+ lines)
├── config.py                 (Environment configuration)
├── requirements.txt          (Python dependencies)
├── Procfile                  (For Render deployment)
├── README.md                 (Full documentation)
├── QUICKSTART.md             (Quick start guide)
├── .gitignore               (Git ignore rules)
├── .env.example             (Environment template)
├── static/
│   ├── css/
│   │   └── style.css        (1000+ lines, comprehensive styling)
│   └── js/
│       └── main.js          (Interactive features)
└── templates/
    ├── base.html            (Navigation + footer)
    ├── home.html            (Landing page)
    ├── signup.html          (Registration form)
    ├── login.html           (Login form)
    ├── onboarding.html      (Goal selection)
    ├── dashboard.html       (User plans dashboard)
    ├── plan_detail.html     (Detailed plan view)
    ├── about.html           (About page)
    └── contact.html         (Contact form)
```

## Available Substances Covered

Each substance has:
- 5+ specific health risks explained
- 5+ benefits of quitting
- Week-by-week quit plan
- Personalized based on frequency

1. **Vaping** - Nicotine dependency, lung damage, cognitive impact
2. **Nicotine** - Physical addiction, blood vessel damage, anxiety
3. **Alcohol** - Liver damage, cancer risk, brain impairment
4. **Tobacco/Smoking** - Lung disease, premature aging, COPD
5. **Cannabis/Weed** - Memory loss, motivation drop, mental health
6. **Hard Drugs** - Severe addiction, overdose risk, life destruction

## Lifestyle Options

### Fitness & Body Composition
- Takes input: age, height, weight, activity level, goal
- Two paths: "Bulk up" or "Lose weight"
- Calculates BMI and provides personalized assessment
- 8-week action plan with specific metrics
- Includes sleep, hydration, and recovery tips

### Appearance & Looks
Three sections:
1. **Skincare** - What actually works, debunked myths, science-backed methods
2. **Fitness** - How exercise transforms physique, real vs. fake progress
3. **Fashion** - Fit matters more than brands, style fundamentals
4. **Why It Matters** - Realistic take on why appearance impacts modern life

## Routes Implemented

```
GET  /                          - Home page
GET/POST /signup                - Sign up
GET/POST /login                 - Login
GET      /onboarding            - Goal selection overlay
POST     /api/save-plan         - Save personalized plan
GET      /dashboard             - User dashboard
GET      /plan/<category>       - Detailed plan view
GET      /about                 - About page
GET/POST /contact               - Contact form
GET      /logout                - Logout
```

## Database Schema

**User Table**
- id (Primary Key)
- email (Unique)
- password (Hashed)
- created_at (Timestamp)

**UserPlan Table**
- id (Primary Key)
- user_id (Foreign Key)
- category (substance/lifestyle/looks)
- selected_items (Multi-select goals)
- plan_data (Personalized plan)
- created_at (Timestamp)

## Deployment Instructions

### To GitHub
```bash
git init
git add .
git commit -m "Initial commit: Get Better platform"
git push origin main
```

### To Render
1. Create Render account
2. New Web Service
3. Connect GitHub repo
4. Select Python environment
5. Deploy (takes 2-5 minutes)
6. Live at: `your-app.onrender.com`

## CSS Highlights

- **Responsive Design**: Mobile-first approach
- **Dark Theme Variables**: Easy to customize
- **Smooth Animations**: Dropdown, overlay, button effects
- **Accessible**: Proper contrast ratios, readable fonts
- **Mobile Menu**: Hamburger icon on small screens
- **Dropdown Menus**: Save screen real estate

## JavaScript Features

- Mobile menu toggle
- Dropdown menu functionality
- Form submission handling
- Onboarding overlay management
- Multi-select goal system
- Authentication forms
- Contact form submission

## Non-Corny Approach (Key Differentiator)

❌ **What We DON'T Do**
- No "You've got this!" repeated 100 times
- No vague motivational quotes
- No fake before/after stories
- No pressure or guilt trips
- No oversimplification

✅ **What We DO Do**
- Explain the science behind why things are harmful
- Provide specific, actionable steps
- Acknowledge that change is hard
- Treat users like adults
- Discuss what actually works vs. what's cope
- Include timelines and realistic expectations

## Testing Checklist

- ✅ Home page displays correctly
- ✅ Sign up / login works
- ✅ Onboarding overlay shows on first login
- ✅ Can select multiple goals
- ✅ Frequency inputs validate correctly
- ✅ Dashboard shows all selected plans
- ✅ Dropdown menus expand/collapse
- ✅ Plan detail pages show comprehensive info
- ✅ Mobile hamburger menu works
- ✅ Mobile dropdowns work on small screens
- ✅ Dark theme is consistent throughout
- ✅ Forms submit without errors

## Next Steps for Users

1. **Test Locally**
   ```bash
   pip install -r requirements.txt
   python app.py
   # Visit http://localhost:5000
   ```

2. **Push to GitHub**
   - Initialize git repository
   - Add all files
   - Push to GitHub

3. **Deploy to Render**
   - Connect GitHub repo
   - Follow Render setup
   - Live in minutes!

4. **Customize** (Optional)
   - Add email functionality
   - Connect community features
   - Add mobile app
   - Integrate email reminders

## Support Resources Included

- SAMHSA National Helpline: 1-800-662-4357
- Crisis Text Line: Text HOME to 741741
- Narcotics Anonymous links
- Doctor referral information
- Contact form for questions

## Summary

**Get Better** is a complete, production-ready web application that helps people:
- Quit harmful substances with personalized, science-backed plans
- Improve their fitness and lifestyle simultaneously
- Enhance their appearance with real advice, not cope
- Do ALL of this at the same time through multi-goal support

Built with modern web technologies, designed for real people, deployed in minutes.

---

**Ready to deploy? See QUICKSTART.md for next steps!**
