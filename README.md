# F1 Hub — Race Predictions & Blog

A full-stack Django web application that combines an F1 blog with a race predictions game. Users can read blog posts, interact through comments and likes, and compete against other fans by predicting pole position and podium finishers for each Grand Prix.

Built as Project 4 for the Code Institute Full Stack Software Development Diploma.

![Am I Responsive screenshot](documents/images/am-i-responsive.png)

**[Live Site](https://f1-blog-ci-9849428ab6fd.herokuapp.com/)** | **[GitHub Repository](https://github.com/garethrogers28/f1-blog)**

---

## Introduction

F1 Hub is a full-stack Django web application designed for Formula 1 fans who want to go beyond traditional race news and results. The platform brings together an F1 blog and an interactive race prediction system, enabling users to engage with content, compete with others, and track their performance across the racing season.

Built around weekly Grand Prix events, the application creates a community-driven experience where users can read blog posts, interact through likes and comments, and submit predictions for pole position and podium finishers to earn points on a live leaderboard.

This project was developed as Project Portfolio 4 for the Code Institute Full Stack Software Development Diploma and demonstrates key full-stack development principles, including relational database design, authentication and authorisation, CRUD functionality, responsive UI design, and deployment to a cloud-based production environment.

---

## Project Goals

The aim of this project was to create a full-stack Formula 1 community platform that combines blog content with an interactive race prediction game.

The project was designed to:
- Provide engaging Formula 1 content
- Encourage user interaction through comments and likes
- Allow users to compete via race predictions
- Demonstrate full-stack Django development skills
- Implement relational database design and user authentication

### Business Goals

- Build a community hub that keeps F1 fans returning weekly during the race season
- Drive engagement through gamification (predictions, leaderboard, points)
- Establish a platform that could be monetised in future through sponsorship or premium features

### Scope

| In Scope | Out of Scope |
|----------|-------------|
| F1 blog with full CRUD for comments | User-created blog posts (admin only) |
| Like/unlike posts | Social media login (Google, Facebook) |
| Race prediction system (pole + podium) | Fastest lap or sprint race predictions |
| Automatic scoring with points | Real-time live race data or API integration |
| Leaderboard and rankings | Season-long championship predictions |
| Personal dashboard (My Garage) | Password reset via email |
| User profile editing | Account deletion |
| Responsive design (mobile, tablet, desktop) | Native mobile app |
| Custom 404/500 error pages | Payment or subscription features |

---

## User Stories

User stories were managed using a GitHub Projects board with MoSCoW prioritisation.

[View the Project Board](https://github.com/garethrogers28/f1-blog/projects)

### Authentication

| # | User Story | Acceptance Criteria |
|---|-----------|-------------------|
| 1 | As a user, I can register an account, so that I can create posts and interact with the site | User can create an account with username, email, and password · Account is stored in the database · User is redirected after successful registration |
| 2 | As a user, I can log in, so that I can access my account | User can log in with valid credentials · Invalid login shows an error message · User is redirected after login |
| 3 | As a user, I can log out, so that I can securely end my session | User can log out successfully · Session is cleared · User is redirected to homepage |

### Blog

| # | User Story | Acceptance Criteria |
|---|-----------|-------------------|
| 4 | As a user, I can view a list of posts, so that I can browse content | Given more than one post in the database, these multiple posts are listed · When a user opens the main page a list of posts is seen |
| 5 | As a user, I can view a full post, so that I can read it in detail | Clicking a post opens full content page · Post displays title, content, author, and date |
| 6 | As a logged-in user, I can add a comment to a post, so that I can join the discussion | User can submit a comment on a post · Comment is linked to the post and user · Comment is saved in the database |
| 7 | As a logged-in user, I can edit my comment, so that my comment is relevant | User can edit and update their own comments · Comment is updated in the database · Success message when comment is updated |
| 8 | As a user, I can delete my comment, so that I can remove it if needed | User can delete their own comment · Success message appears when complete · Comment is removed from the database |
| 11 | As a logged-in user, I can like a post, so that I can show my appreciation for the content | A logged-in user can click a "Like" button on a post · A like is saved in the database · The user can only like a post once · The like count updates immediately after liking |
| 12 | As a user, I can remove my like from a post, so that I can change my preference | A logged-in user can click an "Unlike" button · The like is removed from the database · The like count updates immediately after unliking |
| 13 | As an admin, I can upload an image when creating a post, so that posts are more visually engaging | Admin can upload an image via the Django admin panel · Image is linked to the correct post · Image is stored using Cloudinary |
| 14 | As a user, I can see images on posts, so that the content is more engaging and easier to understand | Each post displays its associated image · Images render correctly on all screen sizes · A default placeholder is shown if no image is uploaded |

### UX

| # | User Story | Acceptance Criteria |
|---|-----------|-------------------|
| 9 | As a user, I can use the site on all devices, so that I can access from anywhere | Site is fully responsive · Layout adapts to mobile, tablet, and desktop |
| 10 | As a user, I need clear and simple navigation, so that I can move around the site easily | Navigation bar is visible on all pages · Links to key pages are included |
| 28 | As a user, I can see a custom 404 page when I visit a page that does not exist, so that I understand the page cannot be found and can navigate back to the site | A custom 404 page is displayed for invalid URLs · The page explains that the requested page was not found · A link is provided to return to the homepage |

### Predictions

| # | User Story | Acceptance Criteria |
|---|-----------|-------------------|
| 15 | As a user, I can view upcoming Formula 1 races, so that I can make predictions before the race weekend begins | Users can see a list of upcoming races · Each race displays its name and date · Logged-in users can select a race to view prediction options |
| 16 | As a logged-in user, I can predict pole position and podium finishers, so that I can compete against other users | Logged-in users can submit predictions · Users can choose pole position, 1st, 2nd, and 3rd place drivers · Predictions are saved to the database · Users receive feedback confirming submission |
| 17 | As a logged-in user, I can edit my prediction before the race begins, so that I can update my choices | Users can edit their own predictions · Predictions cannot be edited after the race deadline · Updated predictions save correctly |
| 18 | As an admin, I can record prediction scores, so that users can compete in a leaderboard | Predictions receive points based on accuracy · Scores are stored in the database |
| 19 | As a logged-in user, I can access a personal dashboard, so that I can view my prediction stats | Logged-in users can access dashboard from navbar · Dashboard displays prediction stats · Dashboard loads without errors |
| 20 | As a user, I can view a leaderboard, so that I can compare my prediction performance against other users | Leaderboard displays users ranked by score · Scores update when prediction results are entered · Users can see their ranking position |
| 21 | As a registered user, I can see my total points, so that I can track my performance | Total points are displayed clearly · Points updated automatically after race scoring · Points reflect all completed race weekends |
| 22 | As a registered user, I can see my current leaderboard rank, so that I can see where I am in the standings | Rank is displayed on dashboard · Rank updates automatically after scoring · Rank is based on total accumulated points |
| 23 | As a registered user, I can view my previous predictions, so that I can review my past performance quickly | Previous race predictions are listed chronologically · Each prediction displays race name and score earned · Users can access prediction details |
| 24 | As a registered user, I can see whether I have submitted a prediction, so that I know if action is required | Upcoming race is displayed · Prediction status shows submitted/not submitted · Edit link available before deadline |
| 25 | As a registered user, I can update my profile, so that I can personalise my account | User can edit profile fields · Changes save successfully · Invalid submissions show validation errors |

---

## Agile Methodology

This project was developed using Agile methodology, with a GitHub Projects Kanban board used to manage user stories and track progress throughout development.

- User stories were created as GitHub Issues with acceptance criteria
- Stories were prioritised using MoSCoW labels (Must Have, Should Have, Could Have)
- The Kanban board tracked stories through **To Do**, **In Progress**, and **Done** columns
- Work was completed in iterative sprints, with features built and tested incrementally

![Kanban Board](documents/images/kanban-board.png)

[View the Project Board](https://github.com/garethrogers28/f1-blog/projects)

---

## UX Design

### Target Audience

This application is aimed at:
- Formula 1 fans
- Sports prediction enthusiasts
- Users who enjoy competitive leaderboard systems
- Mobile-first users consuming sports content

### Wireframes

Wireframes were created in Lucidchart for both desktop and mobile views, covering all key pages of the application.

<details>
<summary>View All Wireframes (Desktop & Mobile)</summary>

![Wireframes](documents/wireframes/f1-blog-wireframes.png)
</details>

### Colour Scheme

The colour palette was inspired by Formula 1's brand identity — bold reds against dark, clean backgrounds for a modern motorsport feel. All colour combinations pass WCAG AA contrast requirements.

![Colour Palette](documents/images/colour-palette.png)

| Colour | Hex | Usage |
|--------|-----|-------|
| Black | `#1a1a1a` | Navbar, footer, headings, body text |
| Dark Grey | `#2d2d2d` | Secondary dark elements |
| F1 Red | `#e10600` | Buttons, links, accents, badges |
| Red Hover | `#b30500` | Button hover states |
| Light Grey | `#f5f5f5` | Page background |
| White | `#ffffff` | Card backgrounds, text on dark elements |

### Typography

- **Headings:** [Exo 2](https://fonts.google.com/specimen/Exo+2) (weight 600/700) — A geometric, modern typeface with a motorsport/tech feel
- **Body text:** [Roboto](https://fonts.google.com/specimen/Roboto) (weight 400/500) — Clean and highly readable at all sizes
- Both served via Google Fonts

### Entity Relationship Diagram

The database schema was designed in Lucidchart showing all models and their relationships.

![ERD](documents/images/f1-blog-erd.png)

The project uses 8 database tables across 2 apps:

**Blog App:**
- `Post` — Blog articles with title, content, author, featured image, and likes
- `Comment` — User comments linked to posts

**Predictions App:**
- `Driver` — F1 drivers (name, team, number)
- `Race` — Race events with prediction deadlines
- `Prediction` — User predictions for pole/P1/P2/P3 (unique per user per race)
- `RaceResult` — Official results (one-to-one with Race)
- `UserProfile` — Extended user info (display name, favourite team/driver)

**Django Built-in:**
- `User` — Authentication (username, email, password)

### Custom Models

The application includes several original custom models created specifically for the race prediction system.

Key custom models include:
- `Prediction`
- `Race`
- `RaceResult`
- `UserProfile`

The `Prediction` model is the core custom feature of the application. It links users to races and stores pole position and podium predictions, with associated scoring logic and leaderboard integration.

---

## Features

### Existing Features

#### Navigation
- Responsive Bootstrap navbar with links to all sections
- Active page highlighted with `aria-current="page"` for accessibility
- Conditional links based on authentication status (Login/Register vs My Garage/Logout)

<details>
<summary>Navigation Screenshots</summary>

![Navbar](documents/features/navbar.png)
![Mobile Navbar](documents/features/mobile-navbar.png)
</details>

#### Footer
- Social media links (Facebook, Instagram, X, LinkedIn) with icon-only design
- All external links open in new tabs with `rel="noopener"` for security
- Developer credit with link to GitHub profile

<details>
<summary>Footer Screenshot</summary>

![Footer](documents/features/footer.png)
</details>

#### Blog
- **Post List** — Paginated list of blog posts with excerpts and featured images
- **Post Detail** — Full article view with comments section and like button
- **Comments** — Authenticated users can create, edit, and delete their own comments
- **Likes** — Authenticated users can like/unlike posts with instant feedback

![Home page](documents/features/home.png)

<details>
<summary>Post Detail Screenshot</summary>

![Post Detail](documents/features/post-detail-like-and-comments.png)
</details>

#### Race Predictions
- **Race List** — View upcoming races with dates and prediction status
- **Submit Prediction** — Choose pole position, P1, P2, and P3 from a dropdown of current drivers
- **Edit Prediction** — Update picks any time before the prediction deadline
- **Automatic Scoring** — Points are calculated automatically by comparing user predictions against official race results entered through the admin panel
- **Leaderboard** — Ranked table of all users by total points
- **Prediction History** — View past predictions with scores earned per race

##### Prediction Scoring System

Users earn points based on prediction accuracy:

| Prediction | Points |
|------------|--------|
| Correct Pole Position | 5 |
| Correct P1 (Winner) | 10 |
| Correct P2 | 5 |
| Correct P3 | 3 |

Maximum possible score per race: **23 points**. Scores are automatically calculated when race results are entered through the admin panel.

<details>
<summary>Predictions Screenshots</summary>

![Race List](documents/features/race-list.png)
![Race Detail](documents/features/race-detail.png)
![Leaderboard](documents/features/leaderboard.png)
</details>

#### User Profile
- **My Garage (Dashboard)** — Personal stats: total points, league position, prediction history, upcoming race status
- **Edit Profile** — Update display name, favourite team, and favourite driver

<details>
<summary>Profile Screenshots</summary>

![Profile Dashboard](documents/features/profile-one.png)
![Profile History](documents/features/profile-two.png)
</details>

#### Authentication
- Register, login, and logout functionality
- Django's built-in authentication with styled templates

<details>
<summary>Login Screenshot</summary>

![Login](documents/features/log-in.png)
</details>

#### Admin Panel
- Full CRUD for posts, comments, races, drivers, and results
- Custom admin registration for all models

<details>
<summary>Admin Panel Screenshot</summary>

![Admin Panel](documents/features/admin.png)
</details>

#### Error Handling
- Custom 404 and 500 error pages with friendly messages and navigation back to home

<details>
<summary>404 Page Screenshot</summary>

![Custom 404 Page](documents/features/error-page.png)
</details>

#### Accessibility & SEO
- Semantic HTML structure (header, main, footer landmarks)
- `aria-current="page"` on active navigation links
- `aria-label` on icon-only links (social media footer links)
- `scope="col"` on all table headers
- Meta descriptions on every page
- Custom favicon (chequered flag) for browser tab identification
- Lighthouse scores: 100 Accessibility, 100 Best Practices, 100 SEO

#### Mobile Responsiveness

The site is fully responsive across all devices. Below are mobile views of key pages:

<details>
<summary>Mobile Screenshots</summary>

![Mobile - Home](documents/features/mobile-home.png)
![Mobile - Post Detail](documents/features/mobile-post-detail.png)
![Mobile - Race Detail](documents/features/mobile-race-detail.png)
![Mobile - Leaderboard](documents/features/mobile-leaderboard.png)
</details>

### Future Features

- Forgot/reset password functionality
- Delete account option
- Predict fastest lap or sprint race
- Season championship predictions
- Social sharing of predictions
- Push notifications when results are entered


---

## Technologies Used

### Languages
- Python 3.13
- HTML5
- CSS3
- JavaScript (ES6)

### Frameworks & Libraries
- [Django 5.2](https://www.djangoproject.com/) — Python web framework
- [Bootstrap 5.3.3](https://getbootstrap.com/) — Responsive front-end framework
- [Bootstrap Icons 1.11.3](https://icons.getbootstrap.com/) — Icon library
- [Cloudinary](https://cloudinary.com/) — Cloud image hosting
- [django-cloudinary-storage](https://pypi.org/project/django-cloudinary-storage/) — Django integration for Cloudinary
- [Gunicorn](https://gunicorn.org/) — Python WSGI HTTP server for production
- [Pillow](https://pillow.readthedocs.io/) — Python image processing library
- [WhiteNoise](https://whitenoise.readthedocs.io/) — Static file serving in production
- [dj-database-url](https://pypi.org/project/dj-database-url/) — Database URL parsing
- [psycopg2](https://pypi.org/project/psycopg2/) — PostgreSQL adapter

### Tools & Services
- [GitHub](https://github.com/) — Version control and project management
- [Heroku](https://heroku.com/) — Cloud deployment platform
- [PostgreSQL](https://www.postgresql.org/) — Production database (via Heroku)
- [SQLite](https://www.sqlite.org/) — Local development database
- [Lucidchart](https://www.lucidchart.com/) — Wireframes and ERD
- [Am I Responsive](https://ui.dev/amiresponsive) — Responsive mockup screenshot

---

## Validation

- Users cannot submit duplicate drivers in podium predictions
- Predictions cannot be edited after race deadlines
- Only authenticated users can submit predictions
- Empty or invalid form submissions are rejected with clear error messages
- Form validation feedback is displayed clearly to users

---

## Security Features

- **CSRF protection** — Django's `CsrfViewMiddleware` protects all POST requests from cross-site request forgery
- **Clickjacking protection** — `XFrameOptionsMiddleware` prevents the site from being embedded in iframes
- **Environment variables** — All sensitive credentials (`SECRET_KEY`, database URL, Cloudinary keys) stored in environment variables, never hardcoded
- **`env.py` excluded from version control** — Listed in `.gitignore` to prevent credential exposure
- **DEBUG disabled in production** — Defaults to `False` if the environment variable is missing, ensuring production is always safe
- **SECRET_KEY validation** — Application raises an error on startup if `SECRET_KEY` is not set in production
- **Password validation** — Django's built-in validators enforce minimum length, common password checks, numeric-only checks, and user attribute similarity checks
- **Authentication required** — `@login_required` decorator on all comment, prediction, and profile views
- **Ownership verification** — Users can only edit/delete their own comments (explicit `request.user` checks in views)
- **Prediction scoping** — All prediction queries are filtered by the authenticated user, preventing access to other users' data

---

## Testing

Manual testing was completed across all major functionality including authentication, CRUD operations, prediction submissions, leaderboard calculations, responsive design, and form validation.

Additional testing details, validator results, and bug fixes are documented in [TESTING.md](TESTING.md)

---

## Deployment

### Heroku Deployment

This project is deployed on Heroku. Steps to deploy:

1. Create a new app on [Heroku](https://heroku.com/)
2. Ensure a `Procfile` exists in the project root with: `web: gunicorn f1blog.wsgi`
3. In the app **Settings** tab, add the following Config Vars:
   | Key | Value |
   |-----|-------|
   | `SECRET_KEY` | Your secret key |
   | `DATABASE_URL` | Your PostgreSQL URL (auto-added with Heroku Postgres add-on) |
   | `CLOUDINARY_CLOUD_NAME` | Your Cloudinary cloud name |
   | `CLOUDINARY_API_KEY` | Your Cloudinary API key |
   | `CLOUDINARY_API_SECRET` | Your Cloudinary API secret |
   | `ALLOWED_HOSTS` | Your Heroku app URL (e.g. `f1-blog-ci-9849428ab6fd.herokuapp.com`) |
   | `DEBUG` | `False` |
4. In the **Deploy** tab, connect to your GitHub repository
5. Enable **Automatic Deploys** from the `main` branch (or deploy manually)
6. Run migrations: `heroku run python manage.py migrate`
7. Collect static files: `heroku run python manage.py collectstatic --noinput`
8. Create a superuser: `heroku run python manage.py createsuperuser`
9. Seed drivers: `heroku run python manage.py seed_drivers`

### Forking the Repository

1. Navigate to the [GitHub repository](https://github.com/garethrogers28/f1-blog)
2. Click the **Fork** button in the top-right corner
3. This creates a copy of the repository in your GitHub account

### Cloning the Repository

1. Navigate to the [GitHub repository](https://github.com/garethrogers28/f1-blog)
2. Click the **Code** button and copy the HTTPS URL
3. In your terminal:
   ```bash
   git clone https://github.com/garethrogers28/f1-blog.git
   cd f1-blog
   python -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```
   This will install all project dependencies listed in the requirements file.

4. Create an `env.py` file in the root directory:
   ```python
   import os

   os.environ['SECRET_KEY'] = 'your-secret-key-here'
   os.environ['DATABASE_URL'] = 'your-database-url'
   os.environ['CLOUDINARY_CLOUD_NAME'] = 'your-cloud-name'
   os.environ['CLOUDINARY_API_KEY'] = 'your-api-key'
   os.environ['CLOUDINARY_API_SECRET'] = 'your-api-secret'
   os.environ['DEBUG'] = 'True'
   ```
   Ensure `env.py` is included in `.gitignore` so sensitive credentials are not exposed publicly.
5. Run migrations and start the server:
   ```bash
   python manage.py migrate
   python manage.py seed_drivers
   python manage.py createsuperuser
   python manage.py runserver
   ```

---

## Credits

### Content
- Blog post content written by the developer using AI assistance
- F1 driver data sourced from the official [Formula 1 website](https://www.formula1.com/)

### Code
- Django documentation for authentication and class-based views
- Bootstrap documentation for responsive components
- Code Institute course material for project structure and deployment guidance

### Acknowledgements
- Code Institute for the course content and assessment framework
- The F1 fan community for inspiration

---
