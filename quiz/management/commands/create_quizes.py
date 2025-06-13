import random

from django.core.management.base import BaseCommand

from quiz.models import Choice, Question, Quiz


class Command(BaseCommand):
    help = "Creates quizzes with unique questions and choices for various topics"

    # Define question banks with 5 sample questions each, and logic to generate more
    QUIZ_QUESTION_BANKS = {
        "Python": {
            "description": "A quiz to test your Python programming knowledge.",
            "time_limit": 3600,
            "questions": [
                {
                    "text": "What is the output of print(len([1, 2, 3, 4]))?",
                    "choices": [
                        {"text": "4", "is_correct": True},
                        {"text": "3", "is_correct": False},
                        {"text": "5", "is_correct": False},
                        {"text": "2", "is_correct": False},
                    ],
                },
                {
                    "text": "Which keyword is used to define a function in Python?",
                    "choices": [
                        {"text": "def", "is_correct": True},
                        {"text": "function", "is_correct": False},
                        {"text": "func", "is_correct": False},
                        {"text": "define", "is_correct": False},
                    ],
                },
                {
                    "text": "What does the 'in' operator do in Python?",
                    "choices": [
                        {
                            "text": "Checks if an element exists in a sequence",
                            "is_correct": True,
                        },
                        {"text": "Performs addition", "is_correct": False},
                        {"text": "Defines a loop", "is_correct": False},
                        {"text": "Imports a module", "is_correct": False},
                    ],
                },
                {
                    "text": "What is the result of 3 ** 2 in Python?",
                    "choices": [
                        {"text": "9", "is_correct": True},
                        {"text": "6", "is_correct": False},
                        {"text": "5", "is_correct": False},
                        {"text": "8", "is_correct": False},
                    ],
                },
                {
                    "text": "Which data type is immutable in Python?",
                    "choices": [
                        {"text": "Tuple", "is_correct": True},
                        {"text": "List", "is_correct": False},
                        {"text": "Dictionary", "is_correct": False},
                        {"text": "Set", "is_correct": False},
                    ],
                },
            ],
            "generate_question": lambda idx: {
                "text": f"What is the output of print({idx} + {idx}) in Python?",
                "choices": [
                    {"text": str(idx + idx), "is_correct": True},
                    {"text": str(idx), "is_correct": False},
                    {"text": str(idx + 1), "is_correct": False},
                    {"text": str(idx - 1), "is_correct": False},
                ],
            },
        },
        "Pandas": {
            "description": "Test your knowledge of the Pandas library in Python.",
            "time_limit": 3600,
            "questions": [
                {
                    "text": "How do you read a CSV file into a DataFrame in Pandas?",
                    "choices": [
                        {"text": "pd.read_csv()", "is_correct": True},
                        {"text": "pd.load_csv()", "is_correct": False},
                        {"text": "pd.open_csv()", "is_correct": False},
                        {"text": "pd.import_csv()", "is_correct": False},
                    ],
                },
                {
                    "text": "What does df.head() do in Pandas?",
                    "choices": [
                        {"text": "Shows the first 5 rows", "is_correct": True},
                        {"text": "Shows the last 5 rows", "is_correct": False},
                        {"text": "Shows all rows", "is_correct": False},
                        {"text": "Shows column names", "is_correct": False},
                    ],
                },
                {
                    "text": "How do you select a column named 'age' from a DataFrame?",
                    "choices": [
                        {"text": "df['age']", "is_correct": True},
                        {"text": "df.age()", "is_correct": False},
                        {"text": "df.get('age')", "is_correct": False},
                        {"text": "df.select('age')", "is_correct": False},
                    ],
                },
                {
                    "text": "What does df.drop('column_name', axis=1) do?",
                    "choices": [
                        {"text": "Drops a column", "is_correct": True},
                        {"text": "Drops a row", "is_correct": False},
                        {"text": "Renames a column", "is_correct": False},
                        {"text": "Sorts the column", "is_correct": False},
                    ],
                },
                {
                    "text": "How do you find the mean of a column in Pandas?",
                    "choices": [
                        {"text": "df['column'].mean()", "is_correct": True},
                        {"text": "df['column'].average()", "is_correct": False},
                        {"text": "df['column'].sum()", "is_correct": False},
                        {"text": "df['column'].median()", "is_correct": False},
                    ],
                },
            ],
            "generate_question": lambda idx: {
                "text": f"What does df.iloc[{idx}] return in a Pandas DataFrame?",
                "choices": [
                    {"text": f"Row {idx}", "is_correct": True},
                    {"text": f"Column {idx}", "is_correct": False},
                    {"text": f"Row {idx + 1}", "is_correct": False},
                    {"text": f"Row {idx - 1}", "is_correct": False},
                ],
            },
        },
        "Django": {
            "description": "A quiz on Django framework concepts.",
            "time_limit": 3600,
            "questions": [
                {
                    "text": "What is the purpose of 'settings.py' in Django?",
                    "choices": [
                        {"text": "To configure project settings", "is_correct": True},
                        {"text": "To define models", "is_correct": False},
                        {"text": "To create views", "is_correct": False},
                        {"text": "To manage templates", "is_correct": False},
                    ],
                },
                {
                    "text": "Which command creates a new Django project?",
                    "choices": [
                        {"text": "django-admin startproject", "is_correct": True},
                        {"text": "django-admin startapp", "is_correct": False},
                        {"text": "django createproject", "is_correct": False},
                        {"text": "django newproject", "is_correct": False},
                    ],
                },
                {
                    "text": "What does 'makemigrations' do in Django?",
                    "choices": [
                        {"text": "Generates migration files", "is_correct": True},
                        {"text": "Applies migrations", "is_correct": False},
                        {"text": "Creates a new app", "is_correct": False},
                        {"text": "Starts the server", "is_correct": False},
                    ],
                },
                {
                    "text": "What is the default database in Django?",
                    "choices": [
                        {"text": "SQLite", "is_correct": True},
                        {"text": "MySQL", "is_correct": False},
                        {"text": "PostgreSQL", "is_correct": False},
                        {"text": "MongoDB", "is_correct": False},
                    ],
                },
                {
                    "text": "What does 'urls.py' do in Django?",
                    "choices": [
                        {"text": "Maps URLs to views", "is_correct": True},
                        {"text": "Defines models", "is_correct": False},
                        {"text": "Configures settings", "is_correct": False},
                        {"text": "Manages templates", "is_correct": False},
                    ],
                },
            ],
            "generate_question": lambda idx: {
                "text": f"What does the Django command 'python manage.py runserver {8000 + idx}' do?",
                "choices": [
                    {
                        "text": f"Starts the server on port {8000 + idx}",
                        "is_correct": True,
                    },
                    {
                        "text": f"Creates a migration on port {8000 + idx}",
                        "is_correct": False,
                    },
                    {
                        "text": f"Deletes a migration on port {8000 + idx}",
                        "is_correct": False,
                    },
                    {
                        "text": f"Stops the server on port {8000 + idx}",
                        "is_correct": False,
                    },
                ],
            },
        },
        "JavaScript": {
            "description": "Test your JavaScript programming skills.",
            "time_limit": 3600,
            "questions": [
                {
                    "text": "What does 'let' do in JavaScript?",
                    "choices": [
                        {
                            "text": "Declares a block-scoped variable",
                            "is_correct": True,
                        },
                        {"text": "Declares a global variable", "is_correct": False},
                        {"text": "Declares a function", "is_correct": False},
                        {"text": "Declares a constant", "is_correct": False},
                    ],
                },
                {
                    "text": "What is the output of console.log(typeof null)?",
                    "choices": [
                        {"text": "object", "is_correct": True},
                        {"text": "null", "is_correct": False},
                        {"text": "undefined", "is_correct": False},
                        {"text": "string", "is_correct": False},
                    ],
                },
                {
                    "text": "How do you write an arrow function in JavaScript?",
                    "choices": [
                        {"text": "() => {}", "is_correct": True},
                        {"text": "function() {}", "is_correct": False},
                        {"text": "=> () {}", "is_correct": False},
                        {"text": "func() {}", "is_correct": False},
                    ],
                },
                {
                    "text": "What does '=== ' mean in JavaScript?",
                    "choices": [
                        {"text": "Strict equality", "is_correct": True},
                        {"text": "Loose equality", "is_correct": False},
                        {"text": "Assignment", "is_correct": False},
                        {"text": "Comparison", "is_correct": False},
                    ],
                },
                {
                    "text": "What is the purpose of 'setTimeout' in JavaScript?",
                    "choices": [
                        {"text": "Delays execution of a function", "is_correct": True},
                        {"text": "Repeats a function", "is_correct": False},
                        {"text": "Stops execution", "is_correct": False},
                        {"text": "Clears a timer", "is_correct": False},
                    ],
                },
            ],
            "generate_question": lambda idx: {
                "text": f"What is the output of {idx} === '{idx}' in JavaScript?",
                "choices": [
                    {"text": "false", "is_correct": True},
                    {"text": "true", "is_correct": False},
                    {"text": f"{idx}", "is_correct": False},
                    {"text": f"'{idx}'", "is_correct": False},
                ],
            },
        },
        "HTML5 and CSS3": {
            "description": "A quiz on HTML and CSS fundamentals.",
            "time_limit": 3600,
            "questions": [
                {
                    "text": "What does the HTML <div> tag do?",
                    "choices": [
                        {"text": "Defines a division or section", "is_correct": True},
                        {"text": "Creates a paragraph", "is_correct": False},
                        {"text": "Inserts an image", "is_correct": False},
                        {"text": "Defines a hyperlink", "is_correct": False},
                    ],
                },
                {
                    "text": "What CSS property sets the text color?",
                    "choices": [
                        {"text": "color", "is_correct": True},
                        {"text": "font-color", "is_correct": False},
                        {"text": "text-color", "is_correct": False},
                        {"text": "background-color", "is_correct": False},
                    ],
                },
                {
                    "text": "What does 'display: flex' do in CSS?",
                    "choices": [
                        {"text": "Enables a flexible box layout", "is_correct": True},
                        {"text": "Hides an element", "is_correct": False},
                        {"text": "Sets inline display", "is_correct": False},
                        {"text": "Centers text", "is_correct": False},
                    ],
                },
                {
                    "text": "What HTML tag is used for an unordered list?",
                    "choices": [
                        {"text": "<ul>", "is_correct": True},
                        {"text": "<ol>", "is_correct": False},
                        {"text": "<li>", "is_correct": False},
                        {"text": "<list>", "is_correct": False},
                    ],
                },
                {
                    "text": "What does the CSS 'margin' property do?",
                    "choices": [
                        {
                            "text": "Sets the space outside an element",
                            "is_correct": True,
                        },
                        {
                            "text": "Sets the space inside an element",
                            "is_correct": False,
                        },
                        {"text": "Sets the border thickness", "is_correct": False},
                        {"text": "Sets the font size", "is_correct": False},
                    ],
                },
            ],
            "generate_question": lambda idx: {
                "text": f"What does the CSS property 'padding: {idx}px' do?",
                "choices": [
                    {
                        "text": f"Sets {idx}px space inside an element",
                        "is_correct": True,
                    },
                    {
                        "text": f"Sets {idx}px space outside an element",
                        "is_correct": False,
                    },
                    {"text": f"Sets {idx}px border", "is_correct": False},
                    {"text": f"Sets {idx}px width", "is_correct": False},
                ],
            },
        },
        "Nginx Server": {
            "description": "Test your knowledge of Nginx configuration.",
            "time_limit": 3600,
            "questions": [
                {
                    "text": "What is the default port for Nginx HTTP traffic?",
                    "choices": [
                        {"text": "80", "is_correct": True},
                        {"text": "443", "is_correct": False},
                        {"text": "8080", "is_correct": False},
                        {"text": "22", "is_correct": False},
                    ],
                },
                {
                    "text": "What directive defines the root directory in Nginx?",
                    "choices": [
                        {"text": "root", "is_correct": True},
                        {"text": "directory", "is_correct": False},
                        {"text": "path", "is_correct": False},
                        {"text": "base", "is_correct": False},
                    ],
                },
                {
                    "text": "What does the 'server_name' directive do in Nginx?",
                    "choices": [
                        {"text": "Specifies the domain name", "is_correct": True},
                        {"text": "Sets the server port", "is_correct": False},
                        {"text": "Defines the server IP", "is_correct": False},
                        {"text": "Configures SSL", "is_correct": False},
                    ],
                },
                {
                    "text": "What is the purpose of 'proxy_pass' in Nginx?",
                    "choices": [
                        {
                            "text": "Forwards requests to another server",
                            "is_correct": True,
                        },
                        {"text": "Sets the server port", "is_correct": False},
                        {"text": "Enables caching", "is_correct": False},
                        {"text": "Blocks requests", "is_correct": False},
                    ],
                },
                {
                    "text": "What does 'error_log' do in Nginx?",
                    "choices": [
                        {"text": "Logs errors to a file", "is_correct": True},
                        {"text": "Logs access requests", "is_correct": False},
                        {"text": "Disables logging", "is_correct": False},
                        {"text": "Sets the error page", "is_correct": False},
                    ],
                },
            ],
            "generate_question": lambda idx: {
                "text": f"What does the Nginx directive 'listen {80 + idx}' do?",
                "choices": [
                    {
                        "text": f"Sets the server to listen on port {80 + idx}",
                        "is_correct": True,
                    },
                    {
                        "text": f"Sets the server to listen on port {80 + idx + 1}",
                        "is_correct": False,
                    },
                    {
                        "text": f"Configures proxy on port {80 + idx}",
                        "is_correct": False,
                    },
                    {"text": f"Disables port {80 + idx}", "is_correct": False},
                ],
            },
        },
        "Google Cloud Platform (GCP)": {
            "description": "A quiz on Google Cloud Platform services.",
            "time_limit": 3600,
            "questions": [
                {
                    "text": "What is Google Compute Engine used for?",
                    "choices": [
                        {"text": "Running virtual machines", "is_correct": True},
                        {"text": "Storing data", "is_correct": False},
                        {"text": "Managing networks", "is_correct": False},
                        {"text": "Hosting databases", "is_correct": False},
                    ],
                },
                {
                    "text": "What service is used for object storage in GCP?",
                    "choices": [
                        {"text": "Cloud Storage", "is_correct": True},
                        {"text": "Cloud SQL", "is_correct": False},
                        {"text": "BigQuery", "is_correct": False},
                        {"text": "Firestore", "is_correct": False},
                    ],
                },
                {
                    "text": "What does BigQuery do in GCP?",
                    "choices": [
                        {
                            "text": "Handles large-scale data analytics",
                            "is_correct": True,
                        },
                        {"text": "Manages virtual machines", "is_correct": False},
                        {"text": "Stores NoSQL data", "is_correct": False},
                        {"text": "Hosts web applications", "is_correct": False},
                    ],
                },
                {
                    "text": "What is the purpose of Cloud Functions in GCP?",
                    "choices": [
                        {"text": "Runs serverless code", "is_correct": True},
                        {"text": "Manages databases", "is_correct": False},
                        {"text": "Configures networks", "is_correct": False},
                        {"text": "Stores files", "is_correct": False},
                    ],
                },
                {
                    "text": "What does Cloud Run do in GCP?",
                    "choices": [
                        {
                            "text": "Deploys containerized applications",
                            "is_correct": True,
                        },
                        {"text": "Manages SQL databases", "is_correct": False},
                        {"text": "Analyzes data", "is_correct": False},
                        {"text": "Stores objects", "is_correct": False},
                    ],
                },
            ],
            "generate_question": lambda idx: {
                "text": f"What does the GCP service 'Compute Engine {idx}' manage?",
                "choices": [
                    {"text": f"Virtual machines {idx}", "is_correct": True},
                    {"text": f"Storage {idx}", "is_correct": False},
                    {"text": f"Networks {idx}", "is_correct": False},
                    {"text": f"Databases {idx}", "is_correct": False},
                ],
            },
        },
        "CI/CD": {
            "description": "Test your understanding of CI/CD pipelines.",
            "time_limit": 3600,
            "questions": [
                {
                    "text": "What does CI stand for in CI/CD?",
                    "choices": [
                        {"text": "Continuous Integration", "is_correct": True},
                        {"text": "Continuous Inspection", "is_correct": False},
                        {"text": "Code Integration", "is_correct": False},
                        {"text": "Continuous Installation", "is_correct": False},
                    ],
                },
                {
                    "text": "What is the purpose of a CI/CD pipeline?",
                    "choices": [
                        {
                            "text": "Automate building, testing, and deployment",
                            "is_correct": True,
                        },
                        {"text": "Manually deploy code", "is_correct": False},
                        {"text": "Write code", "is_correct": False},
                        {"text": "Debug applications", "is_correct": False},
                    ],
                },
                {
                    "text": "What tool is commonly used for CI/CD?",
                    "choices": [
                        {"text": "Jenkins", "is_correct": True},
                        {"text": "Apache", "is_correct": False},
                        {"text": "Nginx", "is_correct": False},
                        {"text": "MySQL", "is_correct": False},
                    ],
                },
                {
                    "text": "What does 'Continuous Deployment' mean?",
                    "choices": [
                        {
                            "text": "Automatically deploying code to production",
                            "is_correct": True,
                        },
                        {"text": "Manually deploying code", "is_correct": False},
                        {"text": "Testing code in staging", "is_correct": False},
                        {"text": "Writing unit tests", "is_correct": False},
                    ],
                },
                {
                    "text": "What is a 'pipeline' in CI/CD?",
                    "choices": [
                        {"text": "A series of automated steps", "is_correct": True},
                        {"text": "A manual process", "is_correct": False},
                        {"text": "A database", "is_correct": False},
                        {"text": "A server", "is_correct": False},
                    ],
                },
            ],
            "generate_question": lambda idx: {
                "text": f"What does the CI/CD pipeline step 'build-{idx}' do?",
                "choices": [
                    {"text": f"Builds the project {idx}", "is_correct": True},
                    {"text": f"Deploys the project {idx}", "is_correct": False},
                    {"text": f"Tests the project {idx}", "is_correct": False},
                    {"text": f"Lints the project {idx}", "is_correct": False},
                ],
            },
        },
        "PostgreSQL": {
            "description": "A quiz on PostgreSQL database concepts.",
            "time_limit": 3600,
            "questions": [
                {
                    "text": "What command creates a new table in PostgreSQL?",
                    "choices": [
                        {"text": "CREATE TABLE", "is_correct": True},
                        {"text": "NEW TABLE", "is_correct": False},
                        {"text": "ADD TABLE", "is_correct": False},
                        {"text": "MAKE TABLE", "is_correct": False},
                    ],
                },
                {
                    "text": "What does 'SELECT * FROM table' do in PostgreSQL?",
                    "choices": [
                        {"text": "Retrieves all rows from a table", "is_correct": True},
                        {"text": "Deletes a table", "is_correct": False},
                        {"text": "Updates a table", "is_correct": False},
                        {"text": "Creates a table", "is_correct": False},
                    ],
                },
                {
                    "text": "What is the purpose of 'PRIMARY KEY' in PostgreSQL?",
                    "choices": [
                        {"text": "Uniquely identifies each row", "is_correct": True},
                        {"text": "Stores duplicate values", "is_correct": False},
                        {"text": "Indexes a column", "is_correct": False},
                        {"text": "Sorts the table", "is_correct": False},
                    ],
                },
                {
                    "text": "What does 'DROP TABLE' do in PostgreSQL?",
                    "choices": [
                        {"text": "Deletes a table", "is_correct": True},
                        {"text": "Creates a table", "is_correct": False},
                        {"text": "Updates a table", "is_correct": False},
                        {"text": "Selects from a table", "is_correct": False},
                    ],
                },
                {
                    "text": "What is the purpose of 'JOIN' in PostgreSQL?",
                    "choices": [
                        {"text": "Combines rows from two tables", "is_correct": True},
                        {"text": "Deletes rows", "is_correct": False},
                        {"text": "Updates rows", "is_correct": False},
                        {"text": "Creates a table", "is_correct": False},
                    ],
                },
            ],
            "generate_question": lambda idx: {
                "text": f"What does the PostgreSQL command 'SELECT column{idx} FROM table' do?",
                "choices": [
                    {"text": f"Selects column{idx} from the table", "is_correct": True},
                    {
                        "text": f"Deletes column{idx} from the table",
                        "is_correct": False,
                    },
                    {"text": f"Updates column{idx} in the table", "is_correct": False},
                    {"text": f"Creates column{idx} in the table", "is_correct": False},
                ],
            },
        },
        "FastAPI": {
            "description": "Test your knowledge of FastAPI framework.",
            "time_limit": 3600,
            "questions": [
                {
                    "text": "What is FastAPI primarily used for?",
                    "choices": [
                        {"text": "Building APIs", "is_correct": True},
                        {"text": "Creating databases", "is_correct": False},
                        {"text": "Managing servers", "is_correct": False},
                        {"text": "Designing frontend", "is_correct": False},
                    ],
                },
                {
                    "text": "What decorator is used to define a GET endpoint in FastAPI?",
                    "choices": [
                        {"text": "@app.get", "is_correct": True},
                        {"text": "@app.post", "is_correct": False},
                        {"text": "@app.route", "is_correct": False},
                        {"text": "@app.endpoint", "is_correct": False},
                    ],
                },
                {
                    "text": "What does FastAPI use for automatic documentation?",
                    "choices": [
                        {"text": "Swagger UI", "is_correct": True},
                        {"text": "Postman", "is_correct": False},
                        {"text": "GraphQL", "is_correct": False},
                        {"text": "Django Admin", "is_correct": False},
                    ],
                },
                {
                    "text": "How do you define a path parameter in FastAPI?",
                    "choices": [
                        {"text": "/items/{item_id}", "is_correct": True},
                        {"text": "/items/?item_id", "is_correct": False},
                        {"text": "/items/<item_id>", "is_correct": False},
                        {"text": "/items:item_id", "is_correct": False},
                    ],
                },
                {
                    "text": "What does FastAPI use for dependency injection?",
                    "choices": [
                        {"text": "Depends()", "is_correct": True},
                        {"text": "Inject()", "is_correct": False},
                        {"text": "Require()", "is_correct": False},
                        {"text": "Use()", "is_correct": False},
                    ],
                },
            ],
            "generate_question": lambda idx: {
                "text": f"What does the FastAPI endpoint '/items/{idx}' return?",
                "choices": [
                    {"text": f"Item with ID {idx}", "is_correct": True},
                    {"text": f"Item with ID {idx + 1}", "is_correct": False},
                    {"text": f"Deletes item {idx}", "is_correct": False},
                    {"text": f"Creates item {idx}", "is_correct": False},
                ],
            },
        },
        "Rest Framework": {
            "description": "A quiz on Django REST Framework concepts.",
            "time_limit": 3600,
            "questions": [
                {
                    "text": "What does a serializer do in Django REST Framework?",
                    "choices": [
                        {"text": "Converts data to/from JSON", "is_correct": True},
                        {"text": "Creates models", "is_correct": False},
                        {"text": "Manages URLs", "is_correct": False},
                        {"text": "Renders templates", "is_correct": False},
                    ],
                },
                {
                    "text": "What is the purpose of a ViewSet in DRF?",
                    "choices": [
                        {"text": "Handles multiple related views", "is_correct": True},
                        {"text": "Defines models", "is_correct": False},
                        {"text": "Manages templates", "is_correct": False},
                        {"text": "Configures settings", "is_correct": False},
                    ],
                },
                {
                    "text": "What does 'api_view' decorator do in DRF?",
                    "choices": [
                        {
                            "text": "Marks a function as an API endpoint",
                            "is_correct": True,
                        },
                        {"text": "Renders a template", "is_correct": False},
                        {"text": "Defines a model", "is_correct": False},
                        {"text": "Creates a serializer", "is_correct": False},
                    ],
                },
                {
                    "text": "What is the purpose of 'permissions' in DRF?",
                    "choices": [
                        {"text": "Controls access to endpoints", "is_correct": True},
                        {"text": "Serializes data", "is_correct": False},
                        {"text": "Defines URLs", "is_correct": False},
                        {"text": "Renders templates", "is_correct": False},
                    ],
                },
                {
                    "text": "What does 'ModelSerializer' do in DRF?",
                    "choices": [
                        {
                            "text": "Automatically creates a serializer from a model",
                            "is_correct": True,
                        },
                        {"text": "Creates a model", "is_correct": False},
                        {"text": "Defines a view", "is_correct": False},
                        {"text": "Manages URLs", "is_correct": False},
                    ],
                },
            ],
            "generate_question": lambda idx: {
                "text": f"What does the DRF endpoint '/api/resource/{idx}' do?",
                "choices": [
                    {"text": f"Retrieves resource {idx}", "is_correct": True},
                    {"text": f"Deletes resource {idx}", "is_correct": False},
                    {"text": f"Updates resource {idx}", "is_correct": False},
                    {"text": f"Creates resource {idx}", "is_correct": False},
                ],
            },
        },
        "Data Structure": {
            "description": "Test your knowledge of data structures.",
            "time_limit": 3600,
            "questions": [
                {
                    "text": "What is the time complexity of searching in a balanced BST?",
                    "choices": [
                        {"text": "O(log n)", "is_correct": True},
                        {"text": "O(n)", "is_correct": False},
                        {"text": "O(1)", "is_correct": False},
                        {"text": "O(n^2)", "is_correct": False},
                    ],
                },
                {
                    "text": "What data structure uses LIFO?",
                    "choices": [
                        {"text": "Stack", "is_correct": True},
                        {"text": "Queue", "is_correct": False},
                        {"text": "Array", "is_correct": False},
                        {"text": "Linked List", "is_correct": False},
                    ],
                },
                {
                    "text": "What is the worst-case time complexity of QuickSort?",
                    "choices": [
                        {"text": "O(n^2)", "is_correct": True},
                        {"text": "O(n log n)", "is_correct": False},
                        {"text": "O(n)", "is_correct": False},
                        {"text": "O(1)", "is_correct": False},
                    ],
                },
                {
                    "text": "What does a linked list use to connect nodes?",
                    "choices": [
                        {"text": "Pointers", "is_correct": True},
                        {"text": "Indices", "is_correct": False},
                        {"text": "Keys", "is_correct": False},
                        {"text": "Values", "is_correct": False},
                    ],
                },
                {
                    "text": "What is the space complexity of a hash table?",
                    "choices": [
                        {"text": "O(n)", "is_correct": True},
                        {"text": "O(1)", "is_correct": False},
                        {"text": "O(log n)", "is_correct": False},
                        {"text": "O(n^2)", "is_correct": False},
                    ],
                },
            ],
            "generate_question": lambda idx: {
                "text": f"What is the time complexity of operation {idx} on a hash table?",
                "choices": [
                    {"text": "O(1)", "is_correct": True},
                    {"text": f"O({idx})", "is_correct": False},
                    {"text": "O(log n)", "is_correct": False},
                    {"text": "O(n^2)", "is_correct": False},
                ],
            },
        },
    }

    def handle(self, *args, **options):
        for quiz_name, details in self.QUIZ_QUESTION_BANKS.items():
            # Check if the quiz already exists
            quiz, created = Quiz.objects.get_or_create(
                title=quiz_name,
                defaults={
                    "description": details["description"],
                    "time_limit": details["time_limit"],
                },
            )
            if not created:
                self.stdout.write(
                    self.style.WARNING(
                        f"Quiz '{quiz_name}' already exists. Skipping creation."
                    )
                )
                continue

            self.stdout.write(self.style.SUCCESS(f"Created quiz: {quiz_name}"))

            # Use only the predefined questions
            all_questions = details["questions"].copy()

            # Create the predefined questions (5 per quiz)
            for idx, q_data in enumerate(all_questions, 1):
                question = Question.objects.create(quiz=quiz, text=q_data["text"])

                # Create 4 choices for each question
                for choice_data in q_data["choices"]:
                    Choice.objects.create(
                        question=question,
                        text=choice_data["text"],
                        is_correct=choice_data["is_correct"],
                    )

                self.stdout.write(
                    self.style.SUCCESS(
                        f"Created question {idx} for {quiz_name} with 4 choices"
                    )
                )
