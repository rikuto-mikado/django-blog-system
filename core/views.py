from django.shortcuts import render


def home(request):
    """
    Homepage - Terminal-style profile display
    """
    context = {
        "page_title": "Home",
        "terminal_text": {
            "name": "Rikuto",
            "title": "Full-stack developer",
            "location": "Japan",
            "description": "Welcome to my corner of the web, where I mostly post about technical topics.",
        },
    }
    return render(request, "core/home.html", context)


def about(request):
    """
    About Page - Introduction and background
    """
    context = {
        "page_title": "About",
        "profile": {
            "name": "Rikuto",
            "title": "Full-stack Developer",
            "location": "Japan",
            "bio": "Passionate about building web applications and exploring new technologies.",
            "skills": [
                "Python",
                "Django",
                "JavaScript",
                "React",
                "PostgreSQL",
                "Docker",
                "AWS",
            ],
            "interests": [
                "Web Development",
                "Database Design",
                "Cloud Infrastructure",
                "Open Source",
            ],
        },
    }
    return render(request, "core/about.html", context)


def resume(request):
    """
    Resume Page - Display and download resume
    """
    context = {
        "page_title": "Resume",
        "contact": {
            "name": "Rikuto",
            "title": "Full-stack Developer",
            "location": "Japan",
            "email": "your.email@example.com",
            "github": "https://github.com/rikuto-mikado",
        },
        "experience": [
            {
                "title": "Full-stack Developer",
                "company": "Tech Company",
                "period": "2023 - Present",
                "description": "Developing web applications using Django and React.",
            }
        ],
        "education": [
            {
                "degree": "Computer Science",
                "school": "University Name",
                "period": "2019 - 2023",
            }
        ],
        "skills": {
            "programming": ["Python", "JavaScript", "TypeScript"],
            "frameworks": ["Django", "React", "Next.js"],
            "databases": ["PostgreSQL", "MySQL", "SQLite"],
            "tools": ["Docker", "Git", "AWS"],
        },
    }
    return render(request, "core/resume.html", context)