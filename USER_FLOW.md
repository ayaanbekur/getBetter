# Get Better - User Flow & Example

## Complete User Journey

### Step 1: Landing Page
User visits getbetter.com and sees:
- "Get Better" branding (with up arrow ↑)
- Hero section: Mission statement
- Feature cards showing:
  - 🚭 Quit Substances
  - 💪 Lifestyle & Fitness
  - ✨ Look & Feel Better
  - 📋 Multiple Goals
  - 📱 Mobile Friendly
  - 🎯 Real Information

**User Action**: Clicks "Start Your Journey" → Goes to signup

---

### Step 2: Sign Up
User creates account with:
- Email: john@example.com
- Password: (secure)

**System**: Creates user account, redirects to onboarding

---

### Step 3: Onboarding Overlay (The Key Feature!)
User sees modal asking: **"What do you need help with?"**

Options presented:
- Vaping
- Nicotine
- Alcohol
- Tobacco
- Weed
- Other Drugs
- **Lifestyle** ← NEW SELECTION
- **Looks** ← NEW SELECTION

**User selects**: Vaping + Nicotine + Lifestyle

**Dynamic forms appear below based on selections:**

### Form 1: Substance Frequency
```
How often do you use these? (times per week)
Vaping:    [  5  ]
Nicotine:  [  3  ]
```

### Form 2: Lifestyle Details
```
Tell us about yourself:
Age:               [ 24 ]
Height (cm):       [175 ]
Weight (kg):       [ 82 ]
Activity Level:    [Moderately Active ▼]
What's your goal?  [Lose Weight & Get Healthy ▼]
```

**User fills everything out and clicks**: "Create My Plan"

---

### Step 4: Dashboard (Multi-Plan View!)
User sees three collapsible plan cards:

#### Card 1: 🚭 Quit Vaping
```
Quit Vaping: Nicotine vaping dependency cessation plan

▼ View Plan
   └─ Frequency: 5x per week (estimated)
   └─ Duration: 5-week program
   └─ Focus: Breaking nicotine dependency

[Full Plan Details]
```

#### Card 2: 🚬 Quit Nicotine
```
Quit Nicotine: Comprehensive nicotine dependence treatment

▼ View Plan
   └─ Focus: Breaking physical addiction
   └─ Duration: 5-week intensive program

[Full Plan Details]
```

#### Card 3: 💪 Lifestyle & Fitness
```
Lifestyle & Fitness: Personalized fitness and health improvement

▼ View Plan
   └─ Customized for you based on your stats
   └─ Includes: Exercise + nutrition guidance

[Full Plan Details]
```

---

### Step 5: View Detailed Plan (Vaping Example)
User clicks "Full Plan Details" on Vaping card

**They see:**

```
🚭 QUIT VAPING: Your Personalized Plan

[Back to Dashboard]

WHY YOU SHOULD QUIT
Vaping isn't as safe as the industry claims. Here's what 
actually happens to your body:

  ✓ Nicotine addiction affects dopamine levels, making it 
    harder to experience pleasure naturally
  ✓ Vaping damages lung tissue and reduces oxygen capacity
  ✓ Increases heart rate and blood pressure, straining your 
    cardiovascular system
  ✓ Contains toxic chemicals that accumulate in your lungs 
    over time
  ✓ Impacts memory and cognitive function, especially in 
    developing brains

WHAT YOU'LL GAIN
  ✓ Better breathing within weeks
  ✓ Improved focus and memory
  ✓ More money in your pocket
  ✓ Better athletic performance
  ✓ Clearer skin

YOUR 5-WEEK PLAN

Week 1: Understand Your Triggers
   Understand your triggers and plan your quit date. Track when 
   you typically use and what emotions trigger it. This is where 
   awareness begins.

Week 2: Find Alternatives
   Find alternatives - exercise, breathing exercises, or hobbies. 
   Replace the habit with something positive. Create a toolkit 
   of backup strategies.

Week 3: Manage Withdrawal Symptoms
   Manage withdrawal symptoms. Stay hydrated, exercise, and reach 
   out to support systems. The hardest week - you've got this.

Week 4: Overcome Cravings
   Overcome cravings with cold water, exercise, or distraction. 
   Each craving passes in 5-10 minutes. Distraction is your friend.

Week 5+: Build a New Routine
   Build a new routine. Track your progress and celebrate 
   milestones. Join a support community. You're winning now.

---

💬 REMEMBER
Change is hard, but not changing is harder. Start today, 
be consistent, and track your progress. In 4-8 weeks, 
you'll be amazed at how much you've improved. You've got this.
```

---

### Step 6: View Lifestyle Plan
User clicks "Full Plan Details" on Lifestyle card

**They see their personalized fitness plan:**

```
💪 YOUR PERSONALIZED FITNESS & HEALTH PLAN

YOUR STATS
  • Age: 24
  • Height: 175cm
  • Weight: 82kg
  • BMI: 26.7 (Overweight)

YOUR GOAL
Goal: Lose weight and improve health. Your BMI is 26.7 - 
focusing on sustainable weight loss.

8-WEEK ACTION PLAN

Week 1-2: Create Caloric Deficit
   Create slight caloric deficit (300-500 below maintenance), 
   track food intake. Use an app like MyFitnessPal or 
   Cronometer.

Week 3-4: Establish Exercise Routine
   Establish exercise routine - 150 minutes cardio + 2 days 
   strength training. 30 min walks 5x/week is enough to start.

Week 5-8: Increase NEAT
   Increase NEAT (daily movement), prioritize whole foods. 
   Every movement counts - take stairs, park further away.

Week 9+: Monitor Progress
   Monitor progress, expect 1-2 lbs weight loss per week. 
   Consistency > intensity.

💡 KEY TIPS FOR SUCCESS
  ✓ Create a 300-500 calorie deficit through diet + exercise
  ✓ Prioritize protein to preserve muscle (0.7-0.8g per lb)
  ✓ Move more throughout the day, aim for 8,000+ steps
  ✓ Sleep 7-9 hours - poor sleep sabotages weight loss
  ✓ Be consistent, expect results in 4-6 weeks
```

---

### Step 7: Mobile View
User opens site on phone (< 768px width)

**Navigation changes:**
```
↑ Get Better        ≡    ← Hamburger menu appears
```

**When hamburger is clicked, mobile menu slides down:**
```
Home
About
Contact
Dashboard
Logout
```

**Dashboard on mobile:**
- Plans stack vertically (1 column)
- Dropdowns fully functional
- Buttons are touch-friendly

---

### Step 8: Going Back & Editing
User wants to add "Looks" to their plan

**Action**: Clicks "Edit Plans" button on dashboard

**Redirects to**: Onboarding page again

**User can now**:
- Add "Looks" goal
- Adjust frequencies/stats
- Submit new plan

**Result**: Dashboard updates with additional "Looks" plan card

---

## Example: Looks Plan Content

User clicks "Full Plan Details" on Looks card

```
✨ LOOK BETTER: SCIENCE-BACKED GUIDE

SKINCARE FUNDAMENTALS

What Actually Works:
  ✓ Cleanse twice daily with a gentle cleanser
  ✓ Use a basic moisturizer suited to your skin type
  ✓ Apply SPF 30+ daily - sun damage is cumulative
  ✓ Avoid touching your face throughout the day
  ✓ Stay hydrated and get quality sleep for skin health

Debunked Methods (Don't Waste Your Time):
  ❌ Facial exercises don't work - focus on sun protection 
     and hydration instead
  ❌ Expensive products aren't necessary - consistency matters 
     more than price
  ❌ Over-washing damages your skin barrier - twice daily 
     is optimal

✓ Science-Backed Methods:
  ✓ Retinol/Retinoids reduce wrinkles and improve texture 
    (evidence-backed)
  ✓ Sunscreen prevents aging and skin cancer 
    (scientifically proven)
  ✓ Moisturizing maintains skin barrier health 
    (dermatologist recommended)

---

FITNESS & BODY COMPOSITION

What Actually Works:
  ✓ Strength training 3-4x per week transforms your physique
  ✓ Progressive overload (gradually increasing weight) drives 
    muscle growth
  ✓ Cardio improves cardiovascular health without excessive 
    time needed
  ✓ Consistency beats intensity - 3 months of regular training 
    beats sporadic effort
  ✓ Compound exercises (squats, bench press, deadlifts) 
    maximize results

[etc...]

WHY APPEARANCE MATTERS (REALITY CHECK)
  • First impressions are formed in milliseconds - appearance 
    is your first communication
  • Society has beauty standards whether we like it or not - 
    working with them gives you advantages
  • Taking care of your appearance correlates with discipline 
    in other life areas
  • Improved appearance boosts confidence, which improves all 
    social interactions
  • But remember: attraction beyond initial appearance is built 
    on character and competence
```

---

## Contact Page
User clicks "Contact" in nav

Sees form:
```
[Contact Form]
Name:     [ _________________ ]
Email:    [ _________________ ]
Message:  [ _________________ ]
          [ _________________ ]
          [ _________________ ]

          [Send Message]

Other Ways to Reach Us:
  • Email: hello@getbetter.com
  • GitHub: github.com/getbetter
  • Crisis: 1-800-662-4357 (SAMHSA)
```

---

## Key User Experience Points

### ✅ What Makes This Different
1. **Multi-goal**: Quit vaping AND get fit at the same time
2. **Personalized**: Plans adjust based on YOUR frequency/stats
3. **In-depth**: Explains WHY, not just "quit now"
4. **Mobile-first**: Hamburger menu, collapsible dropdowns
5. **Dark theme**: Modern, easy on eyes
6. **Non-corny**: Real information, not motivational nonsense

### ✅ Space-Saving Design
- Dashboard uses dropdowns instead of full plan details
- Mobile menu is hamburger (3 lines) not full nav
- Overlay onboarding instead of separate page
- Plans collapse by default, expand on click

### ✅ The Non-Corny Tone
- Explains vaping damages dopamine, not just "it's bad"
- Notes alcohol causes specific cancers, not "drink less"
- Acknowledges change is hard but doable
- Adult tone throughout
- No stock motivational photos

---

## Technical Implementation

All of this is implemented with:
- **Backend**: Flask routes in `app.py`
- **Database**: User + UserPlan models
- **Frontend**: 9 HTML templates
- **Styling**: 1000+ lines of responsive CSS
- **Interactivity**: Vanilla JavaScript
- **Mobile**: CSS media queries + hamburger menu toggle

**Total**: ~5000 lines of production-ready code

---

## Ready to Test?

```bash
pip install -r requirements.txt
python app.py
# Visit http://localhost:5000
# Sign up with test@test.com / password123
# Follow the flow above
```

---

**This is the complete, working Get Better platform!**
