# Contributing to Xenohuru

Thank you for your interest in contributing to Xenohuru! 🎉

We're building an open platform to provide honest, accurate tourism information for Tanzania. Every contribution helps tourists make better decisions and promotes safe, informed travel.

---

## Ways to Contribute

### **1. Add New Attractions**
Know a beautiful place in Tanzania? Share it!

**What we need:**
- Attraction name
- GPS coordinates (latitude, longitude)
- Region/location
- Description (honest, factual)
- Altitude (if relevant)
- Difficulty level (easy/moderate/difficult)
- Nearest airport/town
- Best time to visit
- Photos (optional, but appreciated)

**How to submit:**
- Open an issue with "New Attraction:" prefix
- Use the attraction template
- Provide sources if possible

### **2. Update Existing Information**
Found outdated or incorrect info?

- Open an issue with "Update:" prefix
- Explain what's wrong
- Provide correct information
- Include sources/evidence

### **3. Upload Photos**
Have great photos from your travels?

**Requirements:**
- You own the photo or have permission
- High quality (min 1920x1080)
- Shows the attraction clearly
- No watermarks (except yours)
- Include: location, date taken

### **4. Improve Code**
Are you a developer?

**Backend (Django):**
- API improvements
- Database optimization
- New features
- Bug fixes
- Tests

**Frontend (Next.js):**
- UI/UX improvements
- Performance optimization
- New features
- Responsive design
- Accessibility

### **5. Write Documentation**
Help others understand the project:
- API documentation
- Setup guides
- User tutorials
- Code comments
- Translation

### **6. Report Bugs**
Found something broken?
- Check existing issues first
- Use bug report template
- Include screenshots
- Describe steps to reproduce

### **7. Suggest Features**
Have ideas for improvement?
- Open a feature request
- Explain the problem it solves
- Describe expected behavior
- Consider implementation complexity

---

## Getting Started

### **For Non-Developers (Content Contributors)**

1. **Create a GitHub account** (if you don't have one)
2. **Go to Issues:** [github.com/xenohuru/xenohuru-api.git/issues](https://github.com/xenohuru/xenohuru-api.git/issues)
3. **Click "New Issue"**
4. **Choose a template:**
   - New Attraction
   - Update Information
   - Report Error
5. **Fill out the form**
6. **Submit!**

We'll review and respond within 48-72 hours.

---

### **For Developers**

#### **Step 1: Fork & Clone**
```bash
# Fork the repository on GitHub first, then:
https://github.com/xenohuru/xenohuru-api.git
cd xenohuru-api
```

#### **Step 2: Set Up Backend**
```bash
cd app
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Development tools

# Set up database
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Run tests
pytest

# Start server
python manage.py runserver
```

#### **Step 3: Set Up Frontend**
```bash
cd frontend

# Install dependencies
npm install

# Create environment file
cp .env.example .env.local

# Edit .env.local with your API URL:
# NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1

# Run tests
npm test

# Start development server
npm run dev
```

#### **Step 4: Create a Branch**
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
```

**Branch naming:**
- `feature/` — new features
- `fix/` — bug fixes
- `docs/` — documentation
- `refactor/` — code improvements
- `test/` — adding tests

#### **Step 5: Make Changes**
- Write clean, readable code
- Follow existing code style
- Add comments for complex logic
- Write tests for new features
- Update documentation

#### **Step 6: Test Your Changes**
```bash
# Backend
cd backend
pytest
python manage.py test

# Frontend
cd frontend
npm test
npm run build  # Check for build errors
```

#### **Step 7: Commit**
```bash
git add .
git commit -m "feat: add weather caching system"
```

**Commit message format:**
- `feat:` — new feature
- `fix:` — bug fix
- `docs:` — documentation
- `style:` — formatting
- `refactor:` — code restructuring
- `test:` — adding tests
- `chore:` — maintenance

#### **Step 8: Push & Create Pull Request**
```bash
git push origin feature/your-feature-name
```

Then:
1. Go to your fork on GitHub
2. Click "Pull Request"
3. Fill out the PR template
4. Submit!

---

## Pull Request Guidelines

### **Before Submitting:**
- [ ] Code follows project style
- [ ] Tests pass (`pytest` and `npm test`)
- [ ] Documentation updated (if needed)
- [ ] Commit messages are clear
- [ ] Branch is up to date with `main`

### **PR Description Should Include:**
- What problem does this solve?
- What changes were made?
- How to test the changes?
- Screenshots (for UI changes)
- Related issues (if any)

### **Review Process:**
1. Automated tests run (CI/CD)
2. Code review by maintainers
3. Requested changes (if needed)
4. Approval & merge

**Response time:** Usually within 2-3 days.

---

## Code Style Guidelines

### **Python (Backend)**
- Follow PEP 8
- Use type hints
- Write docstrings for functions
- Max line length: 100 characters
- Use `black` for formatting
- Use `flake8` for linting
```python
def get_weather_data(latitude: float, longitude: float) -> dict:
    """
    Fetch current weather data for given coordinates.
    
    Args:
        latitude: GPS latitude coordinate
        longitude: GPS longitude coordinate
        
    Returns:
        Dictionary containing weather data
        
    Raises:
        WeatherAPIError: If API request fails
    """
    # Implementation
```

### **JavaScript/TypeScript (Frontend)**
- Use TypeScript for new code
- Follow ESLint rules
- Use functional components (React)
- Use meaningful variable names
- Max line length: 100 characters
- Use Prettier for formatting
```typescript
interface WeatherData {
  temperature: number;
  condition: string;
  rain_mm: number;
}

const WeatherCard: React.FC = ({ data }) => {
  // Implementation
};
```

### **General Principles:**
- [✔] Clear, descriptive names
- [✔] Small, focused functions
- [✔] Comments for "why", not "what"
- [✔] DRY (Don't Repeat Yourself)
- [✔] Error handling
- [x] No hardcoded values
- [x] No commented-out code
- [x] No console.log() in production

---

## Testing Guidelines

### **Backend Tests (pytest)**
```python
# backend/tests/test_attractions.py
def test_attraction_list_api():
    """Test that attraction list endpoint returns data"""
    response = client.get('/api/v1/attractions/')
    assert response.status_code == 200
    assert len(response.json()) > 0
```

### **Frontend Tests (Jest)**
```typescript
// frontend/__tests__/WeatherCard.test.tsx
describe('WeatherCard', () => {
  it('renders temperature correctly', () => {
    render();
    expect(screen.getByText('25°C')).toBeInTheDocument();
  });
});
```

**Coverage Goals:**
- Backend: 80%+ coverage
- Frontend: 70%+ coverage
- Critical paths: 100% coverage

---

## Database Changes

If your PR includes database changes:

1. **Create migration:**
```bash
python manage.py makemigrations
```

2. **Test migration:**
```bash
python manage.py migrate
python manage.py migrate --fake-initial  # Test rollback
```

3. **Include migration file in PR**

4. **Document changes in PR description**

---

## Content Moderation Guidelines

When adding attractions or reviewing submissions:

### **[✔] Accept if:**
- Information is factual and verifiable
- GPS coordinates are accurate
- Description is honest (no exaggeration)
- Photos are appropriate and relevant
- Sources provided (when possible)

### **[x] Reject if:**
- Information is false or misleading
- Promotes dangerous behavior
- Contains spam or ads
- Images are copyrighted (without permission)
- Duplicate submission
- Offensive content

### **Request Changes if:**
- Missing required information
- Coordinates seem wrong
- Description needs improvement
- Better photos available

---

## Translation Guidelines

We welcome translations to make the platform accessible:

**Priority languages:**
- Swahili (Kiswahili)
- French
- German
- Chinese

**What to translate:**
- UI text
- Error messages
- Documentation
- API responses (optional)

**Don't translate:**
- Code/variable names
- Technical terms
- Proper nouns (place names)

---

## Community Guidelines

### **Be Respectful:**
- Use inclusive language
- Be patient with beginners
- Give constructive feedback
- Assume good intentions

### **Be Professional:**
- Stay on topic
- No spam or self-promotion
- No offensive content
- Respect maintainers' decisions

### **Be Helpful:**
- Answer questions
- Share knowledge
- Help review PRs
- Welcome newcomers

**Violations may result in:**
- Warning
- Temporary ban
- Permanent ban (severe cases)

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for details.

---

## Recognition

Contributors are recognized in:
- README.md (Contributors section)
- Release notes
- GitHub contributors page
- Annual report (if applicable)

**Special recognition for:**
- First-time contributors
- Major features
- Significant bug fixes
- Documentation improvements
- Active community members

---

## Need Help?

**Questions about contributing?**
- Open a [Discussion](https://github.com/xenohuru/xenohuru-api/discussions)
- Ask in issues with "question" label
- Email: cf89615f228bb45cc805447510de802dfb4bae17@proton.me

**Found a security issue?**
- DO NOT open a public issue
- Email: cf89615f228bb45cc805447510de802dfb4bae17@proton.me
- See [SECURITY.md](SECURITY.md)

---

## Resources

**Learning Resources:**
- [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- [Next.js Learn](https://nextjs.org/learn)
- [Git Basics](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)
- [REST API Design](https://restfulapi.net/)

**Project Resources:**
- [API Documentation](docs/API.md)
- [Architecture Overview](docs/ARCHITECTURE.md)
- [Deployment Guide](docs/DEPLOYMENT.md)

---

## 🙏 Thank You!

Every contribution, no matter how small, helps make tourism in Tanzania safer and more accessible.

**Thank you for being part of this project!** 🇹🇿

---

**Questions?** Open an issue or start a discussion!

